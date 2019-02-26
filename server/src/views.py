from aiohttp import web
from settings import config

import cx_Oracle
import json

# Connect string format: [username]/[password]@//[hostname]:[port]/[DB service name]
DSN = "{user}/{password}@//{host}:{port}/{database}"

async def devices(request):
    id = request.message.url.query['id']
    sql = '''SELECT d.DEVICE_ID,
                    d.DEVICE_TYPE,
                    d.GROUP_ID,
                    d."remark",
                    d."device_name"
            from OS_EQM.DEVICES d
            where d.group_id = {id}
          '''.format(id=id)
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

async def object_classes(request):
    sql = """select dc.device_class_id, dc.name
                from device_classes dc
                where dc.root_device = '1'
             """
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

async def group_representation(request):
    par_id = request.message.url.query['par_id']
    sql = '''select dg.device_group_id,
                    dg.par_group_id,
                    dg.group_name,
                    dg.group_remark,
                    dg.group_type_id
             from os_eqm.device_groups dg
             connect by prior dg.device_group_id = dg.par_group_id
             start with dg.device_group_id = {par_id}
          '''.format(par_id=par_id)
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