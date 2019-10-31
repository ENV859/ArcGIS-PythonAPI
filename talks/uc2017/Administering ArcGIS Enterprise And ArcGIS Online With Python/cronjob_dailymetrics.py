from arcgis.gis import GIS
import datetime

# Demo on Linux machine ps0000111

# Create time stamp for past 24 hours
lastHourDateTime = datetime.datetime.now() - datetime.timedelta(hours = 24)
time24 = int(lastHourDateTime.timestamp() * 1000)
print(time24)
# Create GIS Object
gis = GIS("https://python.playground.esri.com/portal","ucdemo17", verify_cert=False)

f = open('/root/metrics/txt', 'w')
# Get all users
users = gis.users.search()
systemusers = ['esri_boundaries', 'system_publisher', 'esri_demographics', 'esri_livingatlas', 'esri_nav', 'admin']

# Find all users not logged in within past 24 hours
for user in users:
    if user.username not in systemusers:
        if user.lastLogin > time24:
            f.write("User {} logged in past 24 hours...\n".format(user.username))

# Find all WebMaps created in past 24 hours
contents = gis.content.search(query='type:"Web Map"')
for item in contents:
    if item.created > time24:
        f.write('{}\n'.format(item.title))

f.close()