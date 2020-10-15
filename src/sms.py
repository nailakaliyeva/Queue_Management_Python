# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os
if os.getenv("account_sid") is None or os.getenv("account_sid") == "":
    print("ERROR! Make sure you have created your .env file with your API credentials (look for the .evn.example as an example and replace it with your own API credentials that you got from RapidAPI)")
    exit(1)

def send(phone, body='You are next to be seated'):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = os.getenv("account_sid")
    auth_token = os.getenv("auth_token")
    #account_sid = account_sid
    #auth_token = auth_token
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=body,
                        from_='+12052365320',
                        to='+'+ phone
                    )

    print(message.sid)

