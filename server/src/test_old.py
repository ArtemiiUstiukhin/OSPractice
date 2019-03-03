import json
import random


#print(type(ty))
#print(ty["nice"])

ran = random.randint(1,100)
print(ran)

notes = []
for i in range(1,random.randint(2,4)):
    note = {}
    note.setdefault("id",i)
    events = []
    note.setdefault("events",events)
    for j in range(1,random.randint(2,4)):
        event = {}
        event.setdefault("id",j)
        event_data = str(random.randint(1,30))+"."
        event_data = event_data + str(random.randint(1,12))+"."
        event_data = event_data + str(random.randint(2000,2018))
        event.setdefault("data",event_data)
        device = "device"+str(j)
        event.setdefault("device",device)
        event_ip = str(random.randint(1,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))
        event.setdefault("ip",event_ip)
        priority = random.randint(0,100)
        event.setdefault("priority",priority)
        events.append(event)
    note.setdefault("events",events)
    notes.append(note)

for note in notes:
    print(note["id"])
    for event in note["events"]:
        print(event)


#with open("static/groups.json", "w", encoding="utf-8") as file:
#    print("good")

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'static/')
print(dirname)
print(filename)

path = '../../simple_server/static/final_group.json'
groups = json.loads(open(path).read())
print(groups)

