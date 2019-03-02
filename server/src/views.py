from aiohttp import web
from settings import config

import cx_Oracle
import json
import random

# Connect string format: [username]/[password]@//[hostname]:[port]/[DB service name]
DSN = "{user}/{password}@//{host}:{port}/{database}"

async def main(request):
    sortby_type = request.message.url.query['sortby']
    #print(sortby_type)
    if (sortby_type=='class'):
        static_path = 'static/final_class.json'
    elif(sortby_type=='group'):
        static_path = 'static/final_group.json'
    else:
        static_path = 'static/test.json'
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
    groups = dbquery(sql)
    groups = replace_groups(groups)
    for group in groups:
        group.setdefault("children",[])
    devices = get_all_devices()
    for device in devices:
        for group in groups:
            if device["grid"]==group["id"]:
                group["children"].append(device)
                break

    return web.json_response(data=groups, headers=[('Access-Control-Allow-Origin', '*')],
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
        row = cursor.execute(sql)
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

    groups_copy = groups
    with open("src/static/groups.json", "w", encoding="utf-8") as file:
        json.dump(groups_copy, file)

    #работа с девайсами

    sql = '''SELECT d.DEVICE_ID,
                    d.DEVICE_TYPE,
                    d.GROUP_ID,
                    d."remark",
                    d."device_name"
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
    with open("src/static/devices.json", "w", encoding="utf-8") as file:
        json.dump(devices_copy, file)
    #работа с классами

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
            resultc = [dict(zip([desc[0] for desc in row.description], col)) for col in row.fetchall()]
    finally:
        cursor.close()

    st = json.dumps(resultc)
    st = st.replace("DEVICE_CLASS_ID","id")
    st = st.replace("NAME","name")
    classes = json.loads(st)

    for obj in classes:
        obj.setdefault("children",[])

    with open("src/static/classes.json", "w", encoding="utf-8") as file:
        json.dump(classes, file)

    #распихиваем девайсы по группам

    for device in devices:
        for group in groups:
            if device["grid"]==group["id"]:
                group["children"].append(device)
                break

    return web.json_response(data=groups, headers=[('Access-Control-Allow-Origin', '*')],
                            content_type='application/json', dumps=json.dumps)


async def create_class_list(request):
    class_path = 'src/static/classes.json'
    device_path = 'src/static/devices.json'
    classes = json.loads(open(class_path).read())
    devices = json.loads(open(device_path).read())

    #работа с типами

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
            if types[device["type"]]==clas["id"]:
                clas["children"].append(device)
                break

    return web.json_response(data=classes, headers=[('Access-Control-Allow-Origin', '*')],
                            content_type='application/json', dumps=json.dumps)


async def create_group_list(request):
    group_path = 'src/static/groups.json'
    device_path = 'src/static/devices.json'
    groups = json.loads(open(group_path).read())
    devices = json.loads(open(device_path).read())

    for device in devices:
        for group in groups:
            if device["grid"]==group["id"]:
                group["children"].append(device)
                break

    return web.json_response(data=groups, headers=[('Access-Control-Allow-Origin', '*')],
                            content_type='application/json', dumps=json.dumps)


