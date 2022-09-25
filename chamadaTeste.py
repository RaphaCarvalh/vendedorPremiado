from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACbdcf8fe36eb1ddd6c46badfc73fb72bd"
# Your Auth Token from twilio.com/console
auth_token = "bfc8347c4b848b405e8b892d22183638"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5521971786438",
    from_="+13023052921",
    body="Hello from Python!")

print(message.sid)
