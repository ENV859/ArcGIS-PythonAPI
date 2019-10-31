# Script to read list of groups from a csv and create them on the portal.
from arcgis.gis import *
import csv

try:
    url = 'https://dev005223.esri.com/portal'
    username = 'admin'
    password = 'esri.agp'

    print("\n")
    print("=====================================================================\n")
    print("CREATING GROUPS")

    # connect to gis
    gis = GIS(url, username, password, verify_cert=False)

    with open("groups.csv", 'r') as groups_csv:
        groups = csv.DictReader(groups_csv)
        for group in groups:
            try:
                print("\nCreating group: "+ group['title'] + "  ##  ")
                result = gis.groups.create_from_dict(group)
                if result:
                    print("success")

            except Exception as create_ex:
                print("Error... ", str(create_ex))

except:
    print("1")