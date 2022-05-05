import requests
import time
#找企业高筛获取企业id（entity_ids）
url = 'https://sales-test.tangees.com/api/advance-search'
headers = {
    "Cookie": "DISTINCT_ID=ff7af86e-7069-4454-bc2b-a037117fd929; accountCenterSessionId=.eJw9js1KA0EQhN9lzh6m56dnOg-gEEwguCK7l6WntydZSSJko0HEd3fIwWN9VBXfj_lc9DLOk1kZhDIFTEFjctU6tIxcKnnzYMZ60eVgVpWPi7Z47yv6nDGRcEpaGEmjyxxKzik7R0oSiLVo9BVUotbGkcQKSJTAFCaI1JitrEgZbYgA4j344LyNwEGwQk1YMpBA5GqJEqVQgFFTbV5n1Wlc-EvH68c4lX_B5S44PO2--9MO-tPrddPJbXixdvMu8Nztb1vXX4e3Xdi69dx3-7jpHud2KAc-n_XYxjct5vcPMCFUVQ.FJ7Zpw.WXCk-jJmI_y1gMmpWvUbE14bQl8",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarykhUrct5LOGQ9AM2i"}
data = '''
     ------WebKitFormBoundarykhUrct5LOGQ9AM2i
Content-Disposition: form-data; name="filter"

{"must":[{"hasMobile":[{"exist":"1"}]}]}
------WebKitFormBoundarykhUrct5LOGQ9AM2i
Content-Disposition: form-data; name="relation"

0
------WebKitFormBoundarykhUrct5LOGQ9AM2i
Content-Disposition: form-data; name="start"

0
------WebKitFormBoundarykhUrct5LOGQ9AM2i
Content-Disposition: form-data; name="end"

50
------WebKitFormBoundarykhUrct5LOGQ9AM2i
Content-Disposition: form-data; name="filter_advance_search_filter_pool"

1
------WebKitFormBoundarykhUrct5LOGQ9AM2i
Content-Disposition: form-data; name="mode"

2
------WebKitFormBoundarykhUrct5LOGQ9AM2i--
'''.encode('UTF-8')
res = requests.post(url, data=data, headers=headers)
#print(res.text)
#print(res.json())
res_json = res.json()['data']
en_list = []
for i in range(0,3):
    en_list.append(res_json[i]['_id'])
print(en_list)
list01=",".join(str(i) for i in en_list)
print(list01)

#通过获取到的企业id批量添加到crm
url = 'https://sales-test.tangees.com/api/leads/unlock-and-add-to-crm'
headers02 = {
    "Cookie": "DISTINCT_ID=ff7af86e-7069-4454-bc2b-a037117fd929; accountCenterSessionId=.eJw9js1KA0EQhN9lzh6m56dnOg-gEEwguCK7l6WntydZSSJko0HEd3fIwWN9VBXfj_lc9DLOk1kZhDIFTEFjctU6tIxcKnnzYMZ60eVgVpWPi7Z47yv6nDGRcEpaGEmjyxxKzik7R0oSiLVo9BVUotbGkcQKSJTAFCaI1JitrEgZbYgA4j344LyNwEGwQk1YMpBA5GqJEqVQgFFTbV5n1Wlc-EvH68c4lX_B5S44PO2--9MO-tPrddPJbXixdvMu8Nztb1vXX4e3Xdi69dx3-7jpHud2KAc-n_XYxjct5vcPMCFUVQ.FJ7Zpw.WXCk-jJmI_y1gMmpWvUbE14bQl8",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryRUMnm4a3SjkBPac3"}
data = f'''
------WebKitFormBoundaryRUMnm4a3SjkBPac3
Content-Disposition: form-data; name="business_type"

lead
------WebKitFormBoundaryRUMnm4a3SjkBPac3
Content-Disposition: form-data; name="target_user_ids"

61a43736e572f01bde88ee91
------WebKitFormBoundaryRUMnm4a3SjkBPac3
Content-Disposition: form-data; name="entity_ids"

{list01}
------WebKitFormBoundaryRUMnm4a3SjkBPac3
Content-Disposition: form-data; name="entity_type"

enterprise
------WebKitFormBoundaryRUMnm4a3SjkBPac3
Content-Disposition: form-data; name="source"

1
------WebKitFormBoundaryRUMnm4a3SjkBPac3--
'''.encode('UTF-8')
res01 = requests.post(url, data=data, headers=headers02)
print(res01.json()['task_id'])
ba = time.localtime(int(time.time()))
print("创建任务时间：")
print(time.strftime('%Y%m%d %H:%M:%S', ba))
#创建添加到crm的任务后请求result接口查看完成时间
taskid = res01.json()['task_id']
headers03 = {
    "Cookie": "DISTINCT_ID=ff7af86e-7069-4454-bc2b-a037117fd929; accountCenterSessionId=.eJw9js1KA0EQhN9lzh6m56dnOg-gEEwguCK7l6WntydZSSJko0HEd3fIwWN9VBXfj_lc9DLOk1kZhDIFTEFjctU6tIxcKnnzYMZ60eVgVpWPi7Z47yv6nDGRcEpaGEmjyxxKzik7R0oSiLVo9BVUotbGkcQKSJTAFCaI1JitrEgZbYgA4j344LyNwEGwQk1YMpBA5GqJEqVQgFFTbV5n1Wlc-EvH68c4lX_B5S44PO2--9MO-tPrddPJbXixdvMu8Nztb1vXX4e3Xdi69dx3-7jpHud2KAc-n_XYxjct5vcPMCFUVQ.FJ7Zpw.WXCk-jJmI_y1gMmpWvUbE14bQl8"
}

while True:
    is_com = requests.get(url=f"https://sales-test.tangees.com/api/tungee-crm/export-task/{taskid}/result",headers=headers03)
    if is_com.json()['status'] == 2:
        ab = time.localtime(int(time.time()))
        print("完成时间：")
        print(time.strftime('%Y%m%d %H:%M:%S', ab))
        #print("已完成")
        print("成功数："+str(is_com.json()['lead_info']['success_count']))
        print("失败数："+str(is_com.json()['lead_info']['failure_count']))
        break;
