#导入requests模块
import logging

import requests
#请求url
url = 'https://user-uat.tangees.com/api/individual-user/login'
headers = {"referer": "https://user-uat.tangees.com/users/sign-in"}
#请求参数
payload = {"phone":"17806533496","password":"16a9e283c0de31705b00f8e04e1a2b4d","remember":"1","code":"","area_code":"86"}
#form表单形式，参数用data
res = requests.post(url,data=payload,headers = headers)
#logging.info("This is a info level log")
#accountcentersessionid = res.cookies.values()
print(res.text)
cookies = res.cookies
#print(cookies)
#print(accountcentersessionid[0])

#进入演示企业
url = 'http://user-uat.tangees.com/api/company/enter'
payload = {'company_id':'5ff83f6c9604db3716b58314'
           }
headers = {"referer": "https://user-uat.tangees.com/home"}
enter_res = requests.post(url,data=payload,cookies =cookies,headers = headers)
print(enter_res.json())
cookies= enter_res.cookies
#print(cookies)
#获取crm全部客户tab下客户列表
url = 'https://crm-uat.tangees.com/api/customers/all-tab'
params = {'begin':'0','end':'50','return_just_id':'0'}
headers = {"referer": "https://crm-uat.tangees.com/customers/list"}
customers_all_res = requests.get(url,params=params,cookies =cookies,headers =headers)
print(customers_all_res.json())