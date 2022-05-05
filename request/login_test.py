# 导入requests模块
import logging
import logger
import requests
import json

'''
#请求url
url = 'http://user-test.tangees.com/api/individual-user/login'
#请求头
headers = {"Referer": "http://user-test.tangees.com/users/sign-in?returnTo=%2Fhome"}
#请求参数
payload = {"phone":"17806533496","password":"067814ab0c661115d7ba546bb81bf7a7","remember":"0","code":"","area_code":"86"}
#data形式，参数用data
login_res = requests.post(url,data=payload,headers =headers)
#获取响应结果的cookies
cookies = login_res.cookies
#cookies1 = login_res.json()['stat']
logging.warning("This is a warning log.")
print(login_res.text)
print(cookies)
#print(cookies1)
'''
url = 'https://app88879.eapps.dingtalkcloud.com/internal-api/project/announcement/search'
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; U; Android 9; zh-CN; MI 6 Build/PKQ1.190118.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 UWS/3.22.1.161 Mobile Safari/537.36 AliApp(DingTalk/6.0.30) com.alibaba.android.rimet/15213560 Channel/700159 language/zh-CN UT4Aplus/0.2.25 colorScheme/light",
    "Cookie": "__wpkreporterwid_=344a553d-29a4-4f14-858b-48fd6784b62f; userId=160441473133507477",
    "Host": "app88879.eapps.dingtalkcloud.com",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryzc13He2kQz0wn9qD"}
'''data = "------WebKitFormBoundaryzc13He2kQz0wn9qD\r\n"+
        "Content-Disposition: form-data; name=\"annc_type\"\r\n"+
        "\r\n"+
        "win\r\n"+
        "------WebKitFormBoundaryzc13He2kQz0wn9qD\r\n"+
        "Content-Disposition: form-data; name=\"begin\"\r\n"+
        "\r\n"+
        "0\r\n"+
        "------WebKitFormBoundaryzc13He2kQz0wn9qD\r\n"+
        "Content-Disposition: form-data; name=\"end\"\r\n"+
        "\r\n"+
        "20\r\n"+
        "------WebKitFormBoundaryzc13He2kQz0wn9qD\r\n"+
        "Content-Disposition: form-data; name=\"sort\"\r\n"+
        "\r\n"+
        "0\r\n"+
        "------WebKitFormBoundaryzc13He2kQz0wn9qD\r\n"+
        "Content-Disposition: form-data; name=\"filter_condition\"\r\n"+
        "\r\n"+
        "{\"searchMode\":\"全文检索\"}\r\n"+
        "------WebKitFormBoundaryzc13He2kQz0wn9qD\r\n"
        '''
data ='''
      ------WebKitFormBoundaryzc13He2kQz0wn9qD
Content-Disposition: form-data; name="annc_type"

win
------WebKitFormBoundaryzc13He2kQz0wn9qD
Content-Disposition: form-data; name="begin"

0
------WebKitFormBoundaryzc13He2kQz0wn9qD
Content-Disposition: form-data; name="end"

300
------WebKitFormBoundaryzc13He2kQz0wn9qD
Content-Disposition: form-data; name="sort"

0
------WebKitFormBoundaryzc13He2kQz0wn9qD
Content-Disposition: form-data; name="filter_condition"

{"searchMode":"全文检索"}
------WebKitFormBoundaryzc13He2kQz0wn9qD--
'''.encode('UTF-8')
res = requests.post(url, data=data, headers=headers)
print(res.json()['data'][0]['_id'])

for i in range(0,300):
    id = res.json()['data'][i]['_id']
    print(id)

    url = "https://app88879.eapps.dingtalkcloud.com/internal-api/project/announcement/info/detail"
    headers = {
        "Cookie": "__wpkreporterwid_=344a553d-29a4-4f14-858b-48fd6784b62f; userId=160441473133507477"
    }
    params = {"announcement_id": id}
    res2 = requests.get(url, params=params, headers=headers)
    print(res2.status_code)

'''
id = res.json()['data'][250]['_id']
print(id)

url = "https://app88879.eapps.dingtalkcloud.com/internal-api/project/announcement/info/detail"
headers = {
        "Cookie": "__wpkreporterwid_=344a553d-29a4-4f14-858b-48fd6784b62f; userId=160441473133507477"
    }
params = {"announcement_id": id}
res2 = requests.get(url, params=params, headers=headers)
print(res2.json())
print(res2.status_code)
'''
