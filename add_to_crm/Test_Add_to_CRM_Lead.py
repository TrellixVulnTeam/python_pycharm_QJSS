import _thread
import requests
import time
import datetime
#test特斯联内嵌页企业拓客转crm线索模块
def add_to_CRM(threadName,user_id):
    # 找企业高筛获取企业id（entity_ids）
    url = 'https://sales-test.tangees.com/api/advance-search'
    headers = {
        "Cookie": "DISTINCT_ID=ff7af86e-7069-4454-bc2b-a037117fd929; accountCenterSessionId=.eJw9js1KA0EQhN9lzh6m56dnOg-gEEwguCK7l6WntydZSSJko0HEd3fIwWN9VBXfj_lc9DLOk1kZhDIFTEFjctU6tIxcKnnzYMZ60eVgVpWPi7Z47yv6nDGRcEpaGEmjyxxKzik7R0oSiLVo9BVUotbGkcQKSJTAFCaI1JitrEgZbYgA4j344LyNwEGwQk1YMpBA5GqJEqVQgFFTbV5n1Wlc-EvH68c4lX_B5S44PO2--9MO-tPrddPJbXixdvMu8Nztb1vXX4e3Xdi69dx3-7jpHud2KAc-n_XYxjct5vcPMCFUVQ.FJ7Zpw.WXCk-jJmI_y1gMmpWvUbE14bQl8"
    }
    payload = {"filter": "{\"must\":[{\"hasMobile\":[{\"exist\":\"1\"}]}]}", "relation": "0", "start": "0", "end": "200","filter_advance_search_filter_pool": "1","mode":"2"}
    res = requests.post(url, data=payload, headers=headers)
    #print(res.text)
    #print(res.json())
    res_json = res.json()['data']
    en_list = []
    for i in range(0, 50):
        en_list.append(res_json[i]['_id'])
    #print(en_list)
    list01 = ",".join(str(i) for i in en_list)
    #print(list01)

    # 通过获取到的企业id批量添加到crm
    url = 'https://sales-test.tangees.com/api/leads/unlock-and-add-to-crm'
    headers02 = {
        "Cookie": "DISTINCT_ID=ff7af86e-7069-4454-bc2b-a037117fd929; accountCenterSessionId=.eJw9js1KA0EQhN9lzh6m56dnOg-gEEwguCK7l6WntydZSSJko0HEd3fIwWN9VBXfj_lc9DLOk1kZhDIFTEFjctU6tIxcKnnzYMZ60eVgVpWPi7Z47yv6nDGRcEpaGEmjyxxKzik7R0oSiLVo9BVUotbGkcQKSJTAFCaI1JitrEgZbYgA4j344LyNwEGwQk1YMpBA5GqJEqVQgFFTbV5n1Wlc-EvH68c4lX_B5S44PO2--9MO-tPrddPJbXixdvMu8Nztb1vXX4e3Xdi69dx3-7jpHud2KAc-n_XYxjct5vcPMCFUVQ.FJ7Zpw.WXCk-jJmI_y1gMmpWvUbE14bQl8"
}
    data = {"business_type": "lead", "target_user_ids": f'{user_id}', "entity_ids": f'{list01}', "entity_type": "enterprise","source": "1"}
    res01 = requests.post(url, data=data, headers=headers02)
    print(str(threadName)+"--:"+str(res01.json()['task_id']))
    #ba = time.localtime(int(time.time()))
    #print("创建任务时间：")
    #dt_ms = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')  # 含微秒的日期时间，来源 比特量化
    #print(dt_ms)
    print(str(threadName)+"--创建任务时间："+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')))# 含微秒的日期时间，来源 比特量化
    # 创建添加到crm的任务后请求result接口查看完成时间
    taskid = res01.json()['task_id']
    headers03 = {
        "Cookie": "DISTINCT_ID=ff7af86e-7069-4454-bc2b-a037117fd929; accountCenterSessionId=.eJw9js1KA0EQhN9lzh6m56dnOg-gEEwguCK7l6WntydZSSJko0HEd3fIwWN9VBXfj_lc9DLOk1kZhDIFTEFjctU6tIxcKnnzYMZ60eVgVpWPi7Z47yv6nDGRcEpaGEmjyxxKzik7R0oSiLVo9BVUotbGkcQKSJTAFCaI1JitrEgZbYgA4j344LyNwEGwQk1YMpBA5GqJEqVQgFFTbV5n1Wlc-EvH68c4lX_B5S44PO2--9MO-tPrddPJbXixdvMu8Nztb1vXX4e3Xdi69dx3-7jpHud2KAc-n_XYxjct5vcPMCFUVQ.FJ7Zpw.WXCk-jJmI_y1gMmpWvUbE14bQl8"
    }

    while True:
        is_com = requests.get(url=f"https://sales-test.tangees.com/api/tungee-crm/export-task/{taskid}/result",
                              headers=headers03)
        if is_com.json()['status'] == 2:
            #ab = time.localtime(int(time.time()))
            #print("完成时间：")

            print(str(threadName)+"--完成时间："+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')))
            # print("已完成")
            print(str(threadName)+"--成功数：" + str(is_com.json()['lead_info']['success_count']))
            print(str(threadName)+"--失败数：" + str(is_com.json()['lead_info']['failure_count']))
            is_fail = is_com.json()['lead_info']['failure_count']
            if (is_fail !=0):
                #打印出第一条线索失败的原因
                print(str(threadName)+"--失败原因："+str(is_com.json()['lead_info']['failure_list'][0]['failure_msg']))
            break;
try:
    _thread.start_new_thread(add_to_CRM,("Thread-1","61a43736e572f01bde88ee91",))
    _thread.start_new_thread(add_to_CRM,("Thread-2","6183a1e0e572f0694e1e23aa",))
    _thread.start_new_thread(add_to_CRM,("Thread-3","61b83c4de572f06008a78800",))
    _thread.start_new_thread(add_to_CRM,("Thread-4","6155304ee572f05510a3dbff",))
    _thread.start_new_thread(add_to_CRM,("Thread-5","61a09778e572f00a6fa11ef3",))
except:
    print("ERROR:启动线程失败")

while 1 :
    pass






