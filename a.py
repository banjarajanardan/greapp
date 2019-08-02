import csv
import json
from firebase import firebase

firebase = firebase.FirebaseApplication('https://gre-application.firebaseio.com/', None)

result = firebase.get('/', '')
count = 0
for i in result:
    print(i['word'].lower())
    if count == 5:
        break
    count += 1