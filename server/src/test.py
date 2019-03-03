import json

static_path = 'testgroups1.json'
groups = json.loads(open(static_path).read())
parid = 'PAR_GROUP_ID'
#id = 'DEVICE_GROUP_ID'
id = 'id'
i = 0
pid = {1:[0,0]}
root = None
idfd = []
print(len(groups))
count = 0
for g in groups:
    g.setdefault("children",[])
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
print(len(idfd))
print(len(root))
for g in groups:
    if g[id] in idfd:
        root.remove(g)
print(len(root))


with open("result.json", "w", encoding="utf-8") as file:
        json.dump(root, file)

