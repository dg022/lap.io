# we import the Twilio client from the dependency we just installed
from twilio.rest import Client
import secret

# the following line needs your Twilio Account SID and Auth Token
client = Client(secret.x, secret.y)

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+15879984626", 
                       from_="+12568671753", 
                       body="Somebody is at your LAPTOP!!!!")
