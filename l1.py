import firebase_admin
from firebase_admin import credentials, messaging

# Initialize the Firebase Admin SDK with your service account credentials
cred = credentials.Certificate('mygate-fcc6f-firebase-adminsdk-bgbfu-cc162edcfd.json')
firebase_admin.initialize_app(cred)

# Your device's FCM token
registration_token = 'dtuuGp8cRzaOx84byiYRUR:APA91bEOu8BDhYcECrx6VGl4q-cFdiKRaCxza17nq3Xw0kWy22u1696DsY8vvfCzpQoiAojLEh1aldaDE4Gt1T25eDXEGjdRMb1fc6tj17tQjbxaBRbh5QlLgEQcGqhgQsqbR6iMxAJL'
#registration_token = 'fKh4ggb2QOSAEdLEoKkuyD:APA91bFX5eipTCSY6-2G5W5FRkuvlswWFp56PZ3lp0TysRyuoWzW-JZDzP5ur3eXOIWitb_53BjLuSsggG8MJSJuSA5DNTkTBaa4kwj45pdvNBTmGe9fq9fNOqfgxjVtzZUGoYz-QhSu'

# Create a message with data payload only
message = messaging.Message(
    data={
        'key1': 'value1',
        'key2': 'value2',
    },
    token=registration_token,
    android=messaging.AndroidConfig(
        priority='high',  # Ensures delivery while the device is in Doze mode
    ),
)

# Send the message
response = messaging.send(message)

# Print the response
print('Successfully sent message:', response)
