from twilio.rest import Client

account_sid = 'AC87cf538bc580866051754c34883cd5f5'
auth_token = 'b23e84f2fac65416041fac670692ac2c'
client = Client(account_sid, auth_token)

def send_message():

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hey if you got this message type Ok.',
        to='whatsapp:Your phone number'
    )


    print(message.sid)
