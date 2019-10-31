# Script to clean up the users, content and groups created for demo

from arcgis.gis import *

try:
    url = 'https://dev005514.esri.com/portal'
    username = 'admin'
    password = 'esri.agp'
    print("=====================================================================\n")
    print("RUNNING CLEANUP\n")


    gis = GIS(url, username, password, verify_cert=False)

    # region remove groups
    group_list = gis.groups.search("owner:" + username)
    print("Deleting groups\n")
    print("---------------\n")

    for group in group_list:
        try:
            print("\nDeleting " + group.title + "  ##  ")
            group.delete()
            print("success")
        except Exception as group_del_ex:
            print("Error deleting : " + str(group_del_ex))
    # endregion

    #region remove content for each user
    print("\n\nDeleting user content\n")
    print("---------------------\n")
    user_list = gis.users.search("")
    try:
        for user in user_list:
            print('\nUser : ' + user.username + " # ")
            if user.fullName in ['Administrator', 'Esri', 'Esri Navigation']:
                print('skipped')
                continue

            user_content = gis.content.search('owner:{0}'.format(user.username))
            for item in user_content:
                print('\nDeleting : '+ item.title + " # ")
                delete_status = item.delete()
                print(str(delete_status)+ " | ")
            print('empty')

    except Exception as content_del_ex:
        print(str('content_del_ex'))
    #endregion

    # region remove users
    user_list = gis.users.search()
    print("\n\nDeleting users\n")
    print("--------------\n")

    for user in user_list:
        if user.username == "admin" or user.username.startswith("esri_") or user.username.startswith("AVWORLD"):
            continue
        else:
            print("\nDeleting " + user.username + "  ##  ")
            user.delete()
            print("success")
    # endregion
    print("\n All clean")

except:
    print("1")