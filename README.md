#######################################################
1
חיבור לשרת TCP של
RSSH
לולאה פשוטה וריצה בכל 
post חדש
סקריפט פיתון שדוחף לטלפון


ssh qstr@62.0.30.39

Server External IP: 62.0.30.39
User: qstr
Pass: qstr##2023


>>>>>
efis@EfiSLP01 /mnt/c/work/efi_gate1/server/1$ cat l2.sh
nohup ./l1.sh &
>>>>>
efis@EfiSLP01 /mnt/c/work/efi_gate1/server/1$ cat l1.sh
#!/bin/bash
while true
do
        echo "wait"
        #socat tcp-l:22290,reuseaddr - >/dev/null 2>/dev/null
        #python3 serv.py
        socat tcp-l:22290,reuseaddr SYSTEM:'dd bs=1 count=10'
        date >> log1.txt
        echo "start"
        python3 l1.py
done
>>>>>
efis@EfiSLP01 /mnt/c/work/efi_gate1/server/1$ cat l1.py
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
efis@EfiSLP01 /mnt/c/work/efi_gate1/server/1$


#######################################################
2
אתר של רמי 
צריך רק פעם ב3 חודשים ללחוץ על הקישור


https://www.pythonanywhere.com/user/efisarusi1/consoles/35719431/

refresh 3 month
https://www.pythonanywhere.com/user/efisarusi1/webapps/#tab_id_efisarusi1_pythonanywhere_com

https://efisarusi1.pythonanywhere.com/

>>>>>

05:52 ~/mysite $ cat flask_app.py 
from flask import Flask
import subprocess
app = Flask(__name__)
@app.route('/')
def hello_world():
    ls_output = subprocess.check_output(['/home/efisarusi1/mysite/l1.sh']).decode('utf-8')
    return f'<pre>{ls_output}</pre>'
if __name__ == '__main__':
    app.run(debug=True)
05:52 ~/mysite $ 

>>>>>
05:52 ~/mysite $ cat l1.sh 
#!/bin/bash
date >> log1.txt
/home/efisarusi1/.local/bin/python3 /home/efisarusi1/mysite/l1.py 2>&1
which python3
pwd
ls -ltr

>>>>>
05:53 ~/mysite $ cat l1.py 
import firebase_admin
from firebase_admin import credentials, messaging
# Initialize the Firebase Admin SDK with your service account credentials
cred = credentials.Certificate('/home/efisarusi1/mysite/mygate-fcc6f-firebase-adminsdk-bgbfu-cc162edcfd.json')
firebase_admin.initialize_app(cred)
# Your device's FCM token
registration_token = 'dtuuGp8cRzaOx84byiYRUR:APA91bEOu8BDhYcECrx6VGl4q-cFdiKRaCxza17nq3Xw0kWy22u1696DsY8vvfCzpQoiAojLEh1aldaDE4Gt1T25eDXEG
jdRMb1fc6tj17tQjbxaBRbh5QlLgEQcGqhgQsqbR6iMxAJL'
#registration_token = 'fKh4ggb2QOSAEdLEoKkuyD:APA91bFX5eipTCSY6-2G5W5FRkuvlswWFp56PZ3lp0TysRyuoWzW-JZDzP5ur3eXOIWitb_53BjLuSsggG8MJSJuSA5D
NTkTBaa4kwj45pdvNBTmGe9fq9fNOqfgxjVtzZUGoYz-QhSu'
# Create a message with data payload only
message = messaging.Message(
    data={
        'val1': 'val1',
        'val2': 'val2',
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
05:53 ~/mysite $ 




#######################################################
#######################################################

3
https://console.firebase.google.com/u/0/

