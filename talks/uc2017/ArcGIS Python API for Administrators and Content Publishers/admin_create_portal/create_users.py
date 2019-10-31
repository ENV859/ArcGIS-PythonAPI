# Script to read account list from a csv file and create appropriate users in the portal.
import csv
from arcgis.gis import *

try:
    url = 'https://dev005223.esri.com/portal'
    username = 'admin'
    password = 'esri.agp'

    print("CREATING USER ACCOUNTS")

    # Connect to the GIS
    gis = GIS(url, username, password, verify_cert=False)

    # loop through and create users
    with open("users.csv", 'r') as users_csv:
        users = csv.DictReader(users_csv)
        for user in users:
            try:
                print("\nCreating user: " + user['Username'] + " ## ")
                result = gis.users.create(username=user['Username'],
                                          password=user['Password'],
                                          firstname=user['First Name'],
                                          lastname=user['Last Name'],
                                          email=user['Email'],
                                          role =user['Role'])
                if result:
                    print("success  ##\n")

                    print("\t Adding to groups:  # ")
                    groups = user['groups']
                    group_list = groups.split(",")

                    # Search for the group
                    for g in group_list:
                        group_search = gis.groups.search(g)
                        if len(group_search) > 0:
                            try:
                                group = group_search[0]
                                groups_result = group.add_users([user['Username']])
                                if len(groups_result['notAdded']) == 0:
                                    print(g + " # ")

                            except Exception as groups_ex:
                                print("\n \t Cannot add user to group ", g, str(groups_ex))
            except Exception as add_ex:
                print("\nCannot create user: " + user['Username'])
                print("\n")
                print(str(add_ex))

except:
    print("1")