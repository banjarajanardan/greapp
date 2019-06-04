import csv
import json
from firebase import firebase

firebase = firebase.FirebaseApplication('https://collins-gre-8f1e6.firebaseio.com/', None)

# f = open('./abc.csv','r')
# reader = csv.DictReader(f, fieldnames = ( "word","meaning","example"))
# a = firebase.get('/', '')
# if a == None:
#     a = []

# for i in reader:
#     flag = 1
#     words = {}
#     words['word'] = i['word']
#     words['meaning'] = i['meaning']
#     words['example'] = i['example']
#     for j in a:
#         if j['meaning'] == words['meaning']:
#             flag = 0
#             break
#     if flag == 1:
#         a.append(words)

# firebase.put('/','/', a)
# print(a)

a = firebase.get('/', '')
print(a)
# for i in a:
#     if i['word'] == 'cafe':
#         a.remove(i)
# print(len(a))

# firebase.delete('','1')
print(sorted(a))