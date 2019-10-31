# Script that creates a group in each of the City Enterprises then establishes a collaboration with the County enterprise.

from arcgis.gis import *
import os

# region establish connections
host_gis = GIS(profile='profile_emergency')
sb_gis = GIS(profile='sb_portal', verify_cert=False)
va_gis = GIS(profile='va_portal', verify_cert=False)

# endregion

# region Create a collaboration with CalOES as host
print("=========================================================================\n")
print("ESTABLISHING COLLABORATIONS BETWEEN STATE EMERGENCY AGENCY AND COUNTY GIS")

host_group = host_gis.groups.search('Properties at risk')[0]

collab_name = 'Thomas Fire collaboration'
collab_description = "Data sharing initiative between State Emergency Agency and all counties affected by Thomas Fire"
collab_wksp = "Properties at risk"
collab_wksp_desc = 'Automated identification of properties at risk using near real-time spatial analyis'

host_collab = host_gis.admin.collaborations.create(name=collab_name,
                                                     description=collab_description,
                                                     workspace_name=collab_wksp,
                                                     workspace_description=collab_wksp_desc,
                                                     portal_group_id=host_group.id,
                                                     host_contact_first_name="Su",
                                                     host_contact_last_name="Doe",
                                                     host_contact_email_address="Su@doe.com",
                                                     access_mode='sendAndReceive')
if host_collab:
    print("   Initiated collaboration with State Emergency Agency as host")
# endregion

# region Invite Ventura County GIS to the collaboration
host_collab_wksp = host_collab.workspaces[0]
configuration = [{host_collab_wksp['id']:"sendAndReceive"}]
host_collab_invite = host_collab.invite_participant(config_json=configuration,
                                                    expiration=24,
                                                    guest_gis=va_gis,
                                                    save_path='./invitations')
if host_collab_invite:
    print("   Invited Ventura GIS to collaboration")

# accept invitation in Ventura County GIS
va_acceptance_response = va_gis.admin.collaborations.accept_invitation(first_name='Minty',
                                                                       last_name='Doe',
                                                                       email="minty@doe.com",
                                                                       invitation_file=host_collab_invite)
if va_acceptance_response:
    print("   Ventura GIS has accepted invitation")

# accept response in host GIS
va_collab = va_gis.admin.collaborations.list()[0]
invitation_response_file = va_collab.export_invitation(out_folder='./invitations')

# add approprirate Thomas Fire in Ventura GIS to workspace
participant_group = va_gis.groups.search('Thomas fire')[0]
va_collab_wksp = va_collab.workspaces[0]
group_add_result = va_collab.add_group_to_workspace(participant_group, va_collab_wksp)
if group_add_result:
    print("   Ventura GIS has added a group to collaboration workspace")

# import the response back in the host GIS portal
host_accept_status = host_collab.import_invitation_response(invitation_response_file)
if host_accept_status:
    print("   Accepted Ventura's response back in host GIS - completed 2-way handshake")

# endregion

# region Invite Santa Barbara County GIS to the collaboration
print("\n")
host_collab_wksp = host_collab.workspaces[0]
configuration = [{host_collab_wksp['id']:"sendAndReceive"}]
host_collab_invite = host_collab.invite_participant(config_json=configuration,
                                                    expiration=24,
                                                    guest_gis=sb_gis,
                                                    save_path='./invitations')
if host_collab_invite:
    print("   Invited Santa Barbara GIS to collaboration")

# accept invitation in Ventura County GIS
sb_acceptance_response = sb_gis.admin.collaborations.accept_invitation(first_name='Dexter',
                                                                       last_name='Doe',
                                                                       email="dexter@doe.com",
                                                                       invitation_file=host_collab_invite)
if sb_acceptance_response:
    print("   Santa Barbara GIS has accepted invitation")

# accept response in host GIS
sb_collab = sb_gis.admin.collaborations.list()[0]
invitation_response_file = sb_collab.export_invitation(out_folder='./invitations')

# add approprirate Thomas Fire in Santa Barbara GIS to workspace
participant_group = sb_gis.groups.search('Thomas fire')[0]
sb_collab_wksp = sb_collab.workspaces[0]
group_add_result = sb_collab.add_group_to_workspace(participant_group, sb_collab_wksp)
if group_add_result:
    print("   Santa Barbara GIS has added a group to collaboration workspace")

# import the response back in the host GIS portal
host_accept_status = host_collab.import_invitation_response(invitation_response_file)
if host_accept_status:
    print("   Accepted Santa Barbara's response back in host GIS - completed 2-way handshake")

# endregion
print("=====================================================================\n")
