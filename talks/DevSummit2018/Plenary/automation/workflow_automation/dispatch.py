from arcgis.gis import GIS
import json
import arrow  # time manipulation
from arcgis.features import use_proximity
from arcgis.features import manage_data
from datetime import datetime
import time
import requests
import os
from slackclient import SlackClient
from gtts import gTTS
import pygame


def slack_notify(msg):
    """
    Will send a message to the #risk-analysis channel in the Thomas Fire slack channel
    """
    with open('slack_token.txt','r') as token_file_handle:
        slack_token = token_file_handle.read().strip()
    sc = SlackClient(slack_token)

    sc.api_call("chat.postMessage", channel="#risk-analysis", text=msg, as_user='analysis-bot')
    print("Successfully sent msg '{}' to slack channel".format(msg))


def text_to_speech(msg, filename="msg_voice.mp3", try_play_audio=True):
    """Convert msg to an audio file of a computer saying that message.
    Attempt to play that audio file if specified.
    Return the full path to the audio file"""
    pygame.mixer.quit()
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                             filename)
    tts = gTTS(text=msg, lang='en')
    tts.save(file_path)
    print("Audio file written to {}".format(file_path))

    if try_play_audio:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

    return file_path


def find_properties_in_danger(fire_flayer, parcel_flayer, parcels_at_risk_flayer,
                              streets_flayer, streets_at_risk_flayer, log_handle):
    """
    Performs in-memory spatial analysis using ArcGIS API or Python. Finds property parcels that are at immediate
    risk form the raging fire. Alerts the field crew via push notification to a Collector for ArcGIS enabled map
    and also via text message on Slack and voice message that can be played over radio for the disconnected user.
    :param fire_flayer:
    :param parcel_flayer:
    :param parcels_at_risk_flayer:
    :param streets_flayer:
    :param streets_at_risk_flayer:
    :param log_handle:
    :return:
    """
    try:
        print("===============================================================")
        # create buffers around the fire area
        fire_buffer_fc = use_proximity.create_buffers(fire_flayer, distances=[100], units='Feet')
        log_handle.write("Performed buffers \n")

        # region find parcels that intersect with the fire buffers
        parcels_at_risk_fc = manage_data.overlay_layers(fire_buffer_fc, parcel_flayer, overlay_type='Intersect')
        parcels_at_risk_fset = parcels_at_risk_fc.query()
        num_parcels_at_risk = len(parcels_at_risk_fset.features)
        log_handle.write(str(num_parcels_at_risk) + " properties at risk \n")

        # truncate 'parcels at risk feature layer' to remove old data
        parcels_at_risk_flayer.manager.truncate()
        parcels_at_risk_flayer.edit_features(adds=parcels_at_risk_fset.features)
        log_handle.write("Updated 'parcels at risk' feature layer \n")

        # push notification for the connected user
        requests.post('https://hooks.zapier.com/hooks/catch/abc123456/xyz987654/',
                      data={'propertiesAtRisk': num_parcels_at_risk, 'sender': 'PythonAPIBot',
                            'appLink': "arcgis-collector://?itemID=" + webmap_item.id})
        # endregion

        # region find streets that intersect with fire buffers
        streets_at_risk_fc = manage_data.overlay_layers(fire_buffer_fc, streets_flayer, overlay_type='Intersect')
        streets_at_risk_fset = streets_at_risk_fc.query()
        num_streets_at_risk = len(streets_at_risk_fset.features)
        log_handle.write(str(num_streets_at_risk) + " streets at risk \n")

        # truncate 'streets at risk feature layer' to remove old data
        streets_at_risk_flayer.manager.truncate()
        streets_at_risk_flayer.edit_features(adds=streets_at_risk_fset.features)
        log_handle.write("Updated 'streets at risk' feature layer \n")

        # radio notification for disconnected user
        text_message = "Found {} streets in danger. List below:".format(str(num_streets_at_risk))
        for street in streets_at_risk_fset.features:
            text_message = text_message + "\n" + (str(street.attributes['L_ADD_FROM']) + " to " +
                                                        str(street.attributes['L_ADD_TO']) + " " +
                                                        street.attributes['FULL_NAME'] + ", " +
                                                        street.attributes['L_CITY'])
        slack_notify(text_message)
        text_to_speech(text_message, filename='{}.mp3'.format(last_checked), try_play_audio=False)
        # endregion

    except Exception as ex1:
        log_handle.write("Error performing spatial analysis " + str(ex1))


if __name__ == "__main__":
    # region connect to the GIS and read fire perimeter and parcel layers
    gis = GIS(profile='profile_emergency')
    print('Logged into GIS')

    # Get maps and layers
    webmap_item = gis.content.get('itemID')
    fire_perimeter_item = gis.content.get('itemID')

    # Query when the fire perimeter was last addressed
    with open('./last_checked.json', 'r') as file_handle:
        file_contents = json.loads(file_handle)
        init_last_updated = arrow.get(file_contents['lastChecked'] /1000).to('local')
        print('Last checked in PST : ' + str(init_last_updated))

    parcel_item = gis.content.get('itemID')
    parcel_flayer = parcel_item.layers[0]

    streets_item = gis.content.get('itemID')
    streets_flayer = streets_item.layers[0]

    streets_at_risk_item = gis.content.get('itemID')
    streets_at_risk_flayer = streets_at_risk_item.layers[0]

    parcels_at_risk_item = gis.content.get('itemID')
    parcels_at_risk_flayer = parcels_at_risk_item.layers[0]
    # endregion

    with open('./output.txt', 'w') as log_handle:
        log_handle.write('Logged into GIS \n')
        log_handle.write('last checked in PST: ' + str(init_last_updated))
        keep_monitoring = True

        while keep_monitoring:
            try:
                time.sleep(5)  # Check every 'n' seconds.

                # check fresh
                fire_fset = fire_flayer.query(out_fields='EditDate', return_geometry=False)
                fire_feature = fire_fset.features[0]
                last_updated = arrow.get(fire_feature.attributes['EditDate'] / 1000).to('local')  # keep in PST
                # print('Fire layer last updated in PST: ' + str(last_updated) + "\n")

                if init_last_updated < last_updated:
                    # call function to perform risk analysis
                    time.sleep(1)
                    init_last_updated = last_updated
                    print("Fire layer updated. Running dispatch process. Time in PST: " + str(last_updated))
                    log_handle.write("Fire layer updated. Running dispatch process. Time in PST: " + str(last_updated))

                    # issue dispatch
                    find_properties_in_danger(fire_flayer, parcel_flayer, parcels_at_risk_flayer,
                                              streets_flayer, streets_at_risk_flayer, log_handle)

                    # record the most recent fire for which dispatch was sent out
                    with open('./last_checked.json', 'w') as file_handle:
                        d = {'lastChecked': fire_feature.attributes['EditDate']}
                        file_contents = json.dumps(d)
                        file_handle.write(file_contents)

            except Exception as ex:
                print(str(ex))
                print("RESETTING AND CONTINUING")
                log_handle.write(str(ex))
                log_handle.write("RESETTING AND CONTINUING")

                gis = GIS(profile='profile_emergency')

                # Get maps and layers
                webmap_item = gis.content.get('itemID')
                fire_perimeter_item = gis.content.get('itemID')

                # initial check of when layer was edited
                fire_flayer = fire_perimeter_item.layers[0]
                fire_fset = fire_flayer.query(out_fields='EditDate', return_geometry=False)
                fire_feature = fire_fset.features[0]
                init_last_updated = arrow.get(fire_feature.attributes['EditDate'] / 1000).to('local')  # keep in PST
                print('last checked in PST: ' + str(init_last_updated))

                keep_monitoring = True
                continue


        log_handle.write("End of script")