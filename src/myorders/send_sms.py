import os
from twilio.rest import Client

account = "AC1828fe601832f6b926991691cd23e299"
auth_token = "981f47510e6d6199023ef15c49b82a3f"
client = Client(account,auth_token)
client.message.create(
    to = [""],
    from_= "+14142694902",
    body =""
)

