from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('6_TuW_v7ESmbm3fkV9h9DLaiGqIfvhOne2RKdOfptm-I')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/098a4481-0a2e-48a4-8d14-d43f7f5c74c0')

text_to_speech.set_disable_ssl_verification(True)

with open('STT.txt', 'r') as f:
    text = f.readlines()

    text = [line.replace('\n','') for line in text]
    text = ''.join(str(line) for line in text)

    with open('./TTS.mp3', 'wb') as audio_file:
     res = text_to_speech.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
     audio_file.write(res.content)
