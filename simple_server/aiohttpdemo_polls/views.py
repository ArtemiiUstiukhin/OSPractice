from aiohttp import web
import json


async def index(request):
    print(request) 
    return web.Response(text='Hello Aiohttp!')

async def stat(request):
   
#    if (request.body==1):
    print(request.message.url.query['sortby'])
    static_path = 'static/test.json'
#    else:
#	static_path = 'static/test1.json'
    jobj = json.loads(open(static_path).read())
    headers = {'Access-Control-Allow-Origin': '*'}
    return web.json_response(jobj,headers=headers)
