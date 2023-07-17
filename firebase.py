import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('firefile.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://miniprojectdatabase-12f1b-default-rtdb.firebaseio.com/'
})

ref = db.reference('/')
i = 0
def data_send(i):
    ref.set({
        'Car_Count_Hardware':i
    })
    
