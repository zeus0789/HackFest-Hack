from firebase.firebase import FirebaseApplication, FirebaseAuthentication
import base64

SECRET = '8qoR7r1IaoU0uvmt1kRlonby9UpnEbJu5MLPlzi4'
DSN = 'https://eyeai-cafee.firebaseio.com/'
EMAIL = 'io.satyamtg@gmail.com'
authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
firebase = FirebaseApplication(DSN, authentication)
result = firebase.get('/caption', None)
print(result)
