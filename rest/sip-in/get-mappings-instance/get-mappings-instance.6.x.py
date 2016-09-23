# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

# Get an object from its sid. If you do not have a sid,
# check out the list resource examples on this page
ip_access_control_list_mapping = client.sip \
        .domains("SD32a3c49700934481addd5ce1659f04d2") \
        .ip_access_control_list_mappings("AL95a47094615fe05b7c17e62a7877836c") \
        .fetch()

print(ip_access_control_list_mapping.friendly_name)
