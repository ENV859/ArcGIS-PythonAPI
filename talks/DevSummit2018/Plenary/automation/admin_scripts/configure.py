# Script to read list of groups from a csv and create them on the portal.

# region Import libs and connect to the GIS
import argparse
from arcgis.gis import *
import pandas as pd
import csv
from arcgis.geocoding import geocode

# get command line input
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', help='Enter name of event', 
                    default='State Emergency Operations Center')
args = parser.parse_args()

print("CREATING GROUPS")
print("---------------")

csv_path = "./groups.csv"

# connect to gis
gis = GIS(profile='profile_emergency')
# endregion

# region create groups from csv
df = pd.read_csv(csv_path)
print(df[["title", "access", "sortField"]])
print("====================================================================== \n")

with open(csv_path, 'r') as csv_handle:
    reader = csv.DictReader(csv_handle)
    for row in reader:
        try:
            print(" Creating group: ", row['title'], end= "  ##  ")
            result = gis.groups.create_from_dict(row)
            if result:
                print("success")

        except Exception as create_ex:
            print("Error... ", str(create_ex))
# endregion

# region create user accounts from csv
print()
print("ADDING USERS")
print("------------")

# Read CSV file
csv_path = r"./users.csv"

# Read as pandas dataframe
df = pd.read_csv(csv_path)
print(df[["First Name", "Email", "Role"]].head(5))
print("=========================================================== \n")

# loop through and create users
for index, row in df.iterrows():
    try:
        print("Creating user: ", row['First Name'], end=" ## ")
        result = gis.users.create(username=row['Username'],
                                  password=row['Password'],
                                  firstname=row['First Name'],
                                  lastname=row['Last Name'],
                                  email=row['Email'],
                                  role=row['Role'])
        if result:
            print("success  ##")
            # get group list
            print("\t Adding to groups: ", end=" # ")
            groups = row['groups']
            group_list = groups.split(",")

            # Search for the group
            for g in group_list:
                group_search = gis.groups.search(g)
                if len(group_search) > 0:
                    try:
                        group_obj = group_search[0]
                        groups_result = group_obj.add_users([row['Username']])
                        if len(groups_result['notAdded']) == 0:
                            print(g, end =" # ")

                    except Exception as groups_ex:
                        print("\n \t Cannot add user to group ", g, str(groups_ex))
            print("\n")


    except Exception as add_ex:
        print("Cannot create user: " + row['Username'])
        print(str(add_ex))

# endregion

# region style and theme portal
print("STYLING ORG HOME APP")
print("---------------------")
try:

    # Set logo
    gis.admin.ux.set_logo('style_files/logo.png')
    print("    Set org logo")

    # set background
    gis.admin.ux.set_background("style_files/background.jpg")
    print("    Set org background")

    # set banner
    gis.admin.ux.set_banner("style_files/banner.jpg")
    print("    Set org banner")

    # set name
    gis.admin.ux.name = args.name
    gis.admin.ux.description = "Official WebGIS for first responders and public awareness"

    print("    Set org name and description")

    # set extent - geocode the county's extent
    ventura_county = geocode('Ventura, USA', category='subregion')[0]

    ext = {"type": "extent",
           "xmin": ventura_county['extent']['xmin'],
           "ymin": ventura_county['extent']['ymin'],
           "xmax": ventura_county['extent']['xmax'],
           "ymax": ventura_county['extent']['ymax'],
           "spatialReference": {"wkid": 4326}
           }
    gis.update_properties({'defaultExtent': ext})
    print("    Set org extent")

    print("============================================================")

except Exception as style_ex:
    print(str(style_ex))
# endregion