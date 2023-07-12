import requests

def send_sms(message, recipient):
    # Replace 'YOUR_TWILIO_ACCOUNT_SID' and 'YOUR_TWILIO_AUTH_TOKEN' with your actual Twilio account credentials
    account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
    auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
    twilio_number = 'YOUR_TWILIO_PHONE_NUMBER'
    
    # Replace 'YOUR_SMS_GATEWAY_URL' with the URL provided by your SMS gateway provider
    sms_gateway_url = 'YOUR_SMS_GATEWAY_URL'
    
    payload = {
        'account_sid': account_sid,
        'auth_token': auth_token,
        'twilio_number': twilio_number,
        'message': message,
        'recipient': recipient
    }
    
    response = requests.post(sms_gateway_url, json=payload)
    
    if response.status_code == 200:
        print('SMS sent successfully.')
    else:
        print('Failed to send SMS. Error:', response.text)