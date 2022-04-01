# paid

import os
from twilio.rest import Client

client = Client()

from_whatsapp_number = "whatsapp:+919771612274"
to_whatsapp_number = "whatsapp:" + os.environ['9973610124']

message = client.messages.create(body='Check out this message', media_url="https://picsum.photos/200/300", from_=from_whatsapp_number, to=to_whatsapp_number)

print(message.sid)
