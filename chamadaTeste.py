from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "xxxxxxxxxxxxxxx"
# Your Auth Token from twilio.com/console
auth_token = "xxxxxxxxxxxxxxxxx"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5521xxx8",
    from_="+13xxxxx",
    body="Hello from Python!")

print(message.sid)
