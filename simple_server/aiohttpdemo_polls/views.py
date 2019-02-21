from aiohttp import web
import json


async def index(request):
    
    return web.Response(text='Hello Aiohttp!')

async def stat(request):
   
    static_path = 'static/test.json'
    jobj = json.loads(open(static_path).read())
    headers = {'Access-Control-Allow-Origin': '*'}
    return web.json_response(jobj,headers=headers)
