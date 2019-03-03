from aiohttp import web
import json


async def index(request):
        static_path = '../server/src/result.json'
        jobj = json.loads(open(static_path).read())
        st = json.dumps(jobj)
        st = st.replace("DEVICE_GROUP_ID","id")
        st = st.replace("GROUP_NAME","name")
        st = st.replace("GROUP_REMARK","remark")
        st = st.replace("GROUP_TYPE_ID","type")
        groups = json.loads(st)
        headers = {'Access-Control-Allow-Origin': '*'}
        return web.json_response(groups,headers=headers)

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
	with open("static/new.json", "w", encoding="utf-8") as file:
                json.dump(jobj, file)
	headers = {'Access-Control-Allow-Origin': '*'}
	return web.json_response(jobj,headers=headers)

#async def create_class(request):
#	static_path = 'static/final_class.json'
#	jobj = json.loads(open(static_path).read())
#	with open("static/new.json", "w", encoding="utf-8") as file:
#		json.dump(jobj, file)
 #       headers = {'Access-Control-Allow-Origin': '*'}
#	return web.json_response(jobj,headers=headers)
