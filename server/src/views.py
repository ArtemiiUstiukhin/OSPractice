from aiohttp import web
from settings import config

import cx_Oracle
import json
import random

# Connect string format: [username]/[password]@//[hostname]:[port]/[DB service name]
DSN = "{user}/{password}@//{host}:{port}/{database}"

async def main(request):
    sortby_type = request.message.url.query['sortby']

    static_path = 'src/result.json'

    jobj = json.loads(open(static_path).read())
    headers = {'Access-Control-Allow-Origin': '*'}
    return web.json_response(jobj,headers=headers)

async def object_classes(request):
    sql = """select dc.device_class_id, dc.name
             from device_classes dc
             where dc.root_device = '1'"""
    result = dbquery(sql)
    for obj in result:
        obj.setdefault("children",[])
    result = adddevices(result)
    return web.json_response(data=replace_classes(result), headers=[('Access-Control-Allow-Origin', '*')],
                            content_type='application/json', dumps=json.dumps)


async def object_types(request):
    sql = '''select dt.device_class,
                    dt.device_type_id, 
                    dt.name, 
                    dt.remark
             from os_eqm.device_types dt
          '''
    try:
        db_url = DSN.format(**config['oracle'])
        conn = cx_Oracle.connect(db_url)
        cursor = conn.cursor()
        row = cursor.execute(sql)
        result = None
        if row:
            result = [dict(zip([desc[0] for desc in row.description], col)) for col in row.fetchall()]
    finally:
        cursor.close()
    return web.json_response(data=result, headers=[('Access-Control-Allow-Origin', '*')],
                            content_type='application/json', dumps=json.dumps)

async def representation(request):
    sql = '''select g.device_group_id,
                    g.par_group_id,
                    g.group_name,
                    g.group_remark,
                    g.group_type_id
             from os_eqm.device_groups g
             where g.group_type_id = 1
          '''
    try:
        db_url = DSN.format(**config['oracle'])
        conn = cx_Oracle.connect(db_url)
        cursor = conn.cursor()
        row = cursor.execute(sql)
        result = None
        if row:
            result = [dict(zip([desc[0] for desc in row.description], col)) for col in row.fetchall()]
    finally:
        cursor.close()
    return web.json_response(data=result, headers=[('Access-Control-Allow-Origin', '*')],
                            content_type='application/json', dumps=json.dumps)

async def group_representation_old(request):
    sql = '''select dg.device_group_id,
                    dg.par_group_id,
                    dg.group_name,
                    dg.group_remark,
                    dg.group_type_id
             from os_eqm.device_groups dg
             connect by prior dg.device_group_id = dg.par_group_id
          '''
    try:
        db_url = DSN.format(**config['oracle'])
        conn = cx_Oracle.connect(db_url)
        cursor = conn.cursor()
        row = cursor.execute(sql)
        result = None
        if row:
            result = [dict(zip([desc[0] for desc in row.description], col)) for col in row.fetchall()]
    finally:
        cursor.close()

    return web.json_response(data=result, headers=[('Access-Control-Allow-Origin', '*')],
                            content_type='application/json', dumps=json.dumps)

async def group_representation(request):

    #работа с группами 

    sql_recurce = '''select dg.device_group_id,
                    dg.par_group_id,
                    dg.group_name,
                    dg.group_remark,
                    dg.group_type_id
             from os_eqm.device_groups dg
             connect by prior dg.device_group_id = dg.par_group_id
          '''

    sql = '''select dg.device_group_id,
                    dg.par_group_id,
                    dg.group_name,
                    dg.group_remark,
                    dg.group_type_id
             from os_eqm.device_groups dg
          '''

    try:
        db_url = DSN.format(**config['oracle'])
        conn = cx_Oracle.connect(db_url)
        cursor = conn.cursor()
        row = cursor.execute(sql_recurce)
        result = None
        if row:
            result = [dict(zip([desc[0] for desc in row.description], col)) for col in row.fetchall()]
    finally:
        cursor.close()

    st = json.dumps(result)
    st = st.replace("DEVICE_GROUP_ID","id")
    st = st.replace("GROUP_NAME","name")
    st = st.replace("GROUP_REMARK","remark")
    st = st.replace("GROUP_TYPE_ID","type")
    groups = json.loads(st)

    for group in groups:
        group.setdefault("children",[])

#    groups_copy = groups
#    with open("src/static/groups.json", "w", encoding="utf-8") as file:
#        json.dump(groups_copy, file)

    #работа с девайсами

    sql = '''SELECT d.DEVICE_ID,
                    d.DEVICE_TYPE,
                    d.GROUP_ID,
                    d."REMARK",
                    d."DEVICE_NAME"
            from OS_EQM.DEVICES d
          '''
    try:
        db_url = DSN.format(**config['oracle'])
        conn = cx_Oracle.connect(db_url)
        cursor = conn.cursor()
        row = cursor.execute(sql)
        resultd = None
        if row:
            resultd = [dict(zip([desc[0] for desc in row.description], col)) for col in row.fetchall()]
    finally:
        cursor.close()

    st = json.dumps(resultd)
    st = st.replace("DEVICE_ID","id")
    st = st.replace("DEVICE_TYPE","type")
    st = st.replace("DEVICE_NAME","name")
    st = st.replace("device_name","name")
    st = st.replace("GROUP_ID","grid")
    st = st.replace("REMARK","remark")
    devices = json.loads(st)

    for device in devices:
        notes = []
        for i in range(1,random.randint(2,4)):
            note = {}
            note.setdefault("id",i)
            events = []
            note.setdefault("events",events)
            for j in range(1,random.randint(2,4)):
                event = {}
                event.setdefault("id",j)
                event_data = str(random.randint(1,30))+"."+str(random.randint(1,12))+"."+str(random.randint(2000,2018))
                event.setdefault("data",event_data)
                device_name = "device"+str(j)
                event.setdefault("device",device_name)
                event_ip = str(random.randint(1,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,256))
                event.setdefault("ip",event_ip)
                priority = random.randint(0,100)
                event.setdefault("priority",priority)
                events.append(event)
            note.setdefault("events",events)
            notes.append(note)
        device.setdefault("notes",notes)

    devices_copy = devices
#    with open("src/static/devices.json", "w", encoding="utf-8") as file:
#        json.dump(devices_copy, file)

  #распихиваем девайсы по группам

    for device in devices:
        for group in groups:
            if device["grid"]==group["id"]:
                group["children"].append(device)
                break

    parid = 'PAR_GROUP_ID'
    id = 'id'
    i = 0
    pid = {1:[0,0]}
    root = None
    idfd = []
    print(len(groups))
    count = 0
    for g in groups:
        #g.setdefault("children",[])
        i = len(pid)-1
        while i!=0:
            if pid[i][0]==g[parid]:
                index = pid.setdefault(i+1,[g[id],-1])
                pid[i+1]=[g[id],index[1]+1]
                pid[i+2]=[0,len(g["children"])-1]
                break
            else:
                if pid.get(i+1)!=None:
                    pid.pop(i+1)
                i = i-1
        if i==0:
            pid[1]=[g[id],groups.index(g)]
            pid[2]=[0,len(g["children"])-1]
            continue
        j = i
        root = groups
        while i!=0:
            root = root[pid[j-i+1][1]]["children"]
            i = i-1
        root.append(g)
        idfd.append(g[id])
    count = 0
    idfd.sort()
    root = groups.copy()
    for g in groups:
        if g[id] in idfd:
            root.remove(g)


    return web.json_response(data=root, headers=[('Access-Control-Allow-Origin', '*')],
                            content_type='application/json', dumps=json.dumps)


async def create_class_list(request):
    #class_path = 'src/static/classes.json'
    #device_path = 'src/static/devices.json'
    #classes = json.loads(open(class_path).read())
    #devices = json.loads(open(device_path).read())

    #загружаем девайсы 

    sql = '''SELECT d.DEVICE_ID,
                    d.DEVICE_TYPE,
                    d.GROUP_ID,
                    d."REMARK",
                    d."DEVICE_NAME"
            from OS_EQM.DEVICES d
          '''
    try:
        db_url = DSN.format(**config['oracle'])
        conn = cx_Oracle.connect(db_url)
        cursor = conn.cursor()
        row = cursor.execute(sql)
        resultd = None
        if row:
            resultd = [dict(zip([desc[0] for desc in row.description], col)) for col $
    finally:
        cursor.close()

    st = json.dumps(resultd)
    st = st.replace("DEVICE_ID","id")
    st = st.replace("DEVICE_TYPE","type")
    st = st.replace("DEVICE_NAME","name")
    st = st.replace("device_name","name")
    st = st.replace("GROUP_ID","grid")
    st = st.replace("REMARK","remark")
    devices = json.loads(st)

    #создаем события

    for device in devices:
        notes = []
        for i in range(1,random.randint(2,4)):
            note = {}
            note.setdefault("id",i)
            events = []
            note.setdefault("events",events)
            for j in range(1,random.randint(2,4)):
                event = {}
                event.setdefault("id",j)
                event_data = str(random.randint(1,30))+"."+str(random.randint(1,12))+"."+str(random.randint(2000,2018))
                event.setdefault("data",event_data)
                device_name = "device"+str(j)
                event.setdefault("device",device_name)
                event_ip = str(random.randint(1,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,256))
                event.setdefault("ip",event_ip)
                priority = random.randint(0,100)
                event.setdefault("priority",priority)
                events.append(event)
            note.setdefault("events",events)
            notes.append(note)
        device.setdefault("notes",notes)

    #загружаем классы

    sql = """select dc.device_class_id, dc.name
             from os_eqm.device_classes dc
          """
    try:
        db_url = DSN.format(**config['oracle'])
        conn = cx_Oracle.connect(db_url)
        cursor = conn.cursor()
        row = cursor.execute(sql)
        resultd = None
        if row:
            resultc = [dict(zip([desc[0] for desc in row.description], col)) for col row.fetchall()]
    finally:
        cursor.close()

    st = json.dumps(resultc)
    st = st.replace("DEVICE_CLASS_ID","id")
    st = st.replace("NAME","name")
    classes = json.loads(st)

    for obj in classes:
        obj.setdefault("children",[])

    # загружаем типы

    sql = '''select dt.device_class,
                    dt.device_type_id,
                    dt.name,
                    dt.remark
             from os_eqm.device_types dt
          '''
    try:
        db_url = DSN.format(**config['oracle'])
        conn = cx_Oracle.connect(db_url)
        cursor = conn.cursor()
        row = cursor.execute(sql)
        result = None
        if row:
            result = [dict(zip([desc[0] for desc in row.description], col)) for col in row.fetchall()]
    finally:
        cursor.close()

    types = {}
    for type in resilt:
        types.setdefault(type["DEVICE_TYPE_ID"],type["DEVICE_CLASS"])

    for device in devices:
        for clas in classes:
            if device["type"] in types.keys():
                if types[device["type"]]==clas["id"]:
                    clas["children"].append(device)
                    break

    return web.json_response(data=classes, headers=[('Access-Control-Allow-Origin', '*')],
                            content_type='application/json', dumps=json.dumps)


async def create_group_list(request):
    #group_path = 'src/static/groups.json'
    #device_path = 'src/static/devices.json'
    #groups = json.loads(open(group_path).read())
    #devices = json.loads(open(device_path).read())

    for device in devices:
        for group in groups:
            if device["grid"]==group["id"]:
                group["children"].append(device)
                break

    return web.json_response(data=groups, headers=[('Access-Control-Allow-Origin', '*')],
                            content_type='application/json', dumps=json.dumps)


