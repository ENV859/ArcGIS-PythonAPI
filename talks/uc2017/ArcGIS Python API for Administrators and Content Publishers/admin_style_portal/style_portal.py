# Script to theme your ArcGIS Enterprise
from arcgis.gis import GIS

dept_url = 'https://dev005223.esri.com/portal'
admin_username = 'admin'
admin_password = 'esri.agp'

#create a GIS connection
dept_gis = GIS(dept_url, admin_username, admin_password, verify_cert=False)
print("    Connected to the city's ArcGIS Enterprise")

try:

    # Set logo
    dept_gis.admin.ux.set_logo('style_files/logo.png')
    print("    Set Enterprise logo")

    # set background
    dept_gis.admin.ux.set_background("style_files/background.png")
    print("    Set Enterprise background")

    # set banner
    dept_gis.admin.ux.set_banner("style_files/banner.png")
    print("    Set Enterprise banner")

    # set name
    dept_gis.admin.ux.set_name_description("Pasadena City Fire Dept. GIS",
                                     "Official WebGIS of Fire Department of the city of Pasadena")
    print("    Set Enterprise name")

    # set extent
    ext = {"type": "extent", "xmin": -13159633.604126614, "ymin": 4044388.6476039286, "xmax": -13145941.30675904,
           "ymax": 4053939.28118214, "spatialReference": {"wkid": 102100}
           }
    dept_gis.update_properties({'defaultExtent': ext})
    print("    Set Enterprise extent")

    # set featured groups
    search_result = dept_gis.groups.search("central_services")
    featured_group = None
    if len(search_result) > 0:
        featured_group = search_result[0]

        param_dict = {"homePageFeaturedContent": "id:{}".format(featured_group.groupid),
                      "homePageFeaturedContentCount": 12}

        dept_gis.update_properties(param_dict)
        print("    Set home page featured content")

    print("============================================================")

except Exception as style_ex:
    print(str(style_ex))