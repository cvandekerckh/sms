import os
from twilio.rest import Client
from dotenv import load_dotenv
import time
from datetime import datetime



# Load env variables
load_dotenv()
TWILIO_KEY=os.getenv("TWILIO_KEY")
TWILIO_TOKEN=os.getenv("TWILIO_TOKEN")
CORENTIN_PHONE=os.getenv("CORENTIN_PHONE")
ANNESO_PHONE=os.getenv("ANNESO_PHONE")
BOT_PHONE=os.getenv("BOT_PHONE")


# Authenticate
client = Client(TWILIO_KEY, TWILIO_TOKEN)

while(True):
    time.sleep(10)
    if datetime.now() > datetime(2020, 8, 26, 13, 28, 0, 0):


        # Send message
        client.messages.create(
            to=CORENTIN_PHONE,
            from_=BOT_PHONE,
            body="Bonne course coco :)"
        )

        # Security
        time.sleep(300)
        break
