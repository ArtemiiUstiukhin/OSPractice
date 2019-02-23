from aiohttp import web
import json


async def index(request):
	print(request)
	return web.Response(text='Hello Aiohttp!')

async def stat(request):
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
