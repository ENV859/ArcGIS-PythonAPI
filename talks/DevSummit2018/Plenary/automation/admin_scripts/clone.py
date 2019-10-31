# Script to clone disaster management templates from ArcGIS Online solutions

# region Import libs and connect to the GIS
from arcgis.gis import GIS
from arcgis.mapping import WebMap, MapImageLayer

# connect to gis
target_gis = GIS(profile='profile_emergency')
source_gis = GIS()
print("=====================================================================\n")
print("CLONING DISASTER MANAGEMENT SOLUTION TEMPLATES")

# search for informative web layers
modis_hotspots = MapImageLayer('https://utility.arcgis.com/usrsvcs/servers/3dba28abdadd4b4a9b39aaa6e79dcb21/rest/'
                               'services/LiveFeeds/MODIS_Thermal/MapServer')
parcels_at_risk_item = target_gis.content.get('55755e4103374bac9aacd42ef78271f6')  # empty at first
parcels_at_risk_flayer = parcels_at_risk_item.layers[0]
# endregion

# Specify the damage assessment web map and dashboard items
item_ids = ['19d2496962714c0e805004cd9ff9df2d', '8ed4a4fa19d94171b838e9af2e5d8996']
source_items = [source_gis.content.get(item_id) for item_id in item_ids]

# Clone items
new_items = target_gis.content.clone_items(source_items, folder='Forest Fire',
                                           copy_data=False, search_existing_items=False)
print("Cloning items complete. Renaming items")

# Customize items for current emergency
target_group = target_gis.groups.search('Properties at risk')[0]
for new_item in new_items:
    if new_item.type == 'Web Map':
        new_item.update({'title': 'Thomas fire responder map',
                         'snippet': 'Web map for assessing damage and saving properties at risk'})
        new_item.share(groups=[target_group])
        print('Renamed web map -> Thomas fire responder map')

        # add informative web layers to the web map
        wm = WebMap(new_item)
        wm.add_layer(modis_hotspots)
        wm.add_layer(parcels_at_risk_item)  # empty web layer at first
        print('   Added informative web layers')

    elif new_item.type == 'Operation View':
        new_item.update({'title': 'Thomas fire response dashboard',
                         'snippet': 'Operations dashboard for assessing damage and saving properties at risk'})
        new_item.share(groups=[target_group])
        print('Renamed dashboard -> Thomas fire response dashboard')

    elif new_item.type == 'Feature Service':
        new_item.update({'title': 'Thomas fire assessment layer',
                         'snippet': 'Feature layer for collecting assessment report'})
        new_item.share(groups=[target_group])
        print('Renamed web layer -> Thomas fire assessment layer')

