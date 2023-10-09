import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("littlevisions-firebase-adminsdk-k4594-a1e531b667.json")
firebaseConfig = {
    "apiKey": "AIzaSyBy34e1q5g0MKM4rdXpdVcpim6ZqHve4Z0",
    "authDomain": "littlevisions.firebaseapp.com",
    "projectId": "littlevisions",
    "storageBucket": "littlevisions.appspot.com",
    "messagingSenderId": "936806799910",
    "appId": "1:936806799910:web:5f5c0ea39d752f1016a4e7",
}
app = firebase_admin.initialize_app(cred,firebaseConfig)
