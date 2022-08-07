import requests
import json

s=requests.get('http://join.navgurukul.org/api/partners')
b=s.json()

with open("project.json","w")as f:
    w=json.dump(b,f,indent=4)

with open("project.json")as f:
    t=json.load(f)
# print(t)
l=[]
for i in t:
    for j in t[i]:
        l.append(j["id"])
# print(l)        
list1=[]
user=input("enter the number:-1==Assending,2==Desending:=")
if user=='1':
    l.sort()
    # print(l)
    for k in range(len(l)):
        # print(k)
        for n in range(len(t["data"])):
            # print(n)
            if l[k]==t['data'][n]['id']:
                s=t['data'][n]
                list1.append(s)

    # print(list1)
elif user=='2':
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i]>l[j]:
                l[j],l[i]=l[i],l[j]
    # print(l)
    for k in range(len(l)):
        # print(k)
        for n in range(len(t["data"])):
            # print(n)
            if l[k]==t['data'][n]['id']:
                s=t['data'][n]
                list1.append(s)
with open("file1.json","w")as f:
    json.dump(list1,f,indent=4)
    
