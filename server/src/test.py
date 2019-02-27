import json 

str = "{Hello:Hi}"
#print(str)
str = str.replace("Hello","Hi there")
#print(str)


js = [{"DEVICE_CLASS": 1, "DEVICE_TYPE_ID": 1, "NAME": "Routers", "REMARK": "nice"}, {"DEVICE_CLASS": 2, "DEVICE_TYPE_ID": 2, "NAME": "Switch", "REMARK": "cool"}]
str = json.dumps(js)
#print(type(str))
#print(type(js))
#print(str)
str = str.replace("DEVICE_CLASS","class_id")

final = json.loads(str)

for elem in final:
  #  print(elem)
    elem.setdefault("children",[])
 #   print(elem)
#    print(elem["children"])
adict = None
keys = ('name', 'age', 'food')
values = ('Monty', 42, 'spam')
adict = dict(zip(keys,values))
print(adict)
print(type(adict))
print(json.dumps(adict))
print(type(json.dumps(adict)))
str = json.dumps(adict)
str = str.replace("name","NAMEw")
final = json.loads(str)
print(final)
print(type(final))
