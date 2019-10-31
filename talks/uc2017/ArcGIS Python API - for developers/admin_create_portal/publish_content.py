# Publisher persona
# Script to publish content for each user.

from arcgis.gis import *
import csv
import json

try:
    url = 'https://dev005223.esri.com/portal'
    username = 'admin'
    password = 'esri.agp'

    # Read the csv containing user accounts and their territory info
    csv_path = "users.csv"

    # Read template web map
    template_webmap_dict = dict()
    with open('user_content/web_map.json', 'r') as webmap_file:
                template_webmap_dict = json.load(webmap_file)

    # Connect to the GIS
    gis = GIS(url, username, password, verify_cert=False)

    # Loop through each user and publish the content
    with open(csv_path, 'r') as csv_handle:
        reader = csv.DictReader(csv_handle)
        for row in reader:
            try:
                data_to_publish = 'user_content/' + row['assigned_zone'] + ".csv"

                print("\nPublishing " + data_to_publish, end= " # ")
                added_item = gis.content.add({}, data = data_to_publish)
                published_item = added_item.publish()

                if published_item is not None:
                    # publish web map
                    print('webmaps', end= " ## ")
                    user_webmap_dict = template_webmap_dict
                    user_webmap_dict['operationalLayers'][0].update({'itemId': published_item.itemid,
                                                                     'layerType': "ArcGISFeatureLayer",
                                                                     'title': published_item.title,
                                                                     'url': published_item.url + r"/0"})

                    web_map_properties = {'title': '{0} {1} response locations'.format(row['First Name'], row['Last Name']),
                                          'type': 'Web Map',
                                          'snippet': 'Regions under the supervision of' +\
                                                     '{0} {1}'.format(row['First Name'], row['Last Name']),
                                          'tags': 'ArcGIS API for Python',
                                          'typeKeywords': "Collector, Explorer Web Map, Web Map, Map, Online Map",
                                          'text': json.dumps(user_webmap_dict)}

                    web_map_item = gis.content.add(web_map_properties)

                    #Reassign ownership of items to current user. Transfer webmaps in a new
                    # folder with user's last name
                    print("success. Assigning to: ", end= "  #  ")
                    result1 = published_item.reassign_to(row['Username'])
                    new_folder_name = row['Last Name'] + "_webmaps"
                    result2 = web_map_item.reassign_to(row['Username'], target_folder=new_folder_name)

                    #share webmap to user's groups
                    groups_list1 = row['groups'].split(',')
                    groups_list = [gname.lstrip() for gname in groups_list1] #remove white spaces in name
                    result3 = web_map_item.share(groups=groups_list)
                    if (result1 and result2 and result3) is not None:
                        print(row['Username'])
                    else:
                        print("error")
                else:
                    print(" error publishing csv")

            except Exception as pub_ex:
                print("Error : " + str(pub_ex))
    print.close()
    print("0")
except Exception as global_ex:
    print("1")