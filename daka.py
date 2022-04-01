import requests
s=requests.Session()
r=s.get("https://cn.bing.com/search?q=gitpod%E5%AE%9A%E6%97%B6%E8%BF%90%E8%A1%8C%E8%84%9A%E6%9C%AC&cvid=548f5d615250414d9c50d1760cdfbb6f&aqs=edge.0.0l5j69i57j69i60l3.1733j0j1&pglt=163&FORM=ANSPA1&PC=U531")
print(r.status_code)
# print(r.text)
with open("1.html",'w') as f:
    f.write(r.text)