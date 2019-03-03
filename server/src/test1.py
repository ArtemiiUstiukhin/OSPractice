arr = [{1:"q",2:"w"},{1:"e",2:"r"},{1:"t",2:"y"}]
arr[0].setdefault("child",[])
arr[0]["child"].append({1:"e",2:"r"})
print(arr)
for a in arr:
    print(a)
    if a=={1:"e",2:"r"}: arr.remove({1:"e",2:"r"})
    #print(a)
print(arr)
