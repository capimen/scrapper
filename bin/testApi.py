import requests

BASE = "http://127.0.0.1:5000/"




'''
data =  [{"likes":78, "name": "how to make raspedy", "views":1000},
         {"likes":16, "name": "My first API", "views":800},
         {"likes":45, "name": "LAST RESORT", "views":50}]
for i in range(len(data)):
    response = requests.put(BASE + "comparatorapi/"+str(i), data[i])
    print(response.json())

#input()
#response = requests.delete(BASE + "video/0")
#print(response)

input()
response = requests.get(BASE + "comparatorapi/1")
print(response.json())
'''

#input()
response = requests.get(BASE + "/comparator/product/54")
print(response.json())

input()
response = requests.get(BASE + "/comparator/list/")
print(response.json())