import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random
import time

cred = credentials.Certificate('firefile.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://miniprojectdatabase-12f1b-default-rtdb.firebaseio.com/'
})

ref = db.reference('/')
i = 0
while True:
    randNum = random.randint(0,12)
    randNum1 = random.randint(0,12)
    ref.set({
        'Car_Count_Simulation': randNum,        # naam change nahi karna
        'Car_Count_Hardware' : randNum1
    })
    time.sleep(2)
    print(randNum)
