import _thread
import requests
import time
import datetime
#test特斯联内嵌页企业拓客转crm线索模块
def add_to_CRM(threadName,user_id):
    # 找企业高筛获取企业id（entity_ids）
    url = 'https://sales-uat.tangees.com/api/advance-search'
    headers = {
        "Cookie": "remember_token=61dce155f13dba27c688d4f4|65f02ed908efdcd0557b38f21085394c68f15a8ce27aa1b847c5381654821a7b1f92195d914d016158f2e48ca01af111a6f7617fd85d548f696ccda88b8d38cd; DISTINCT_ID=73b973d7-a6a8-4d49-8635-8de80f0bec0d; marketingSessionId=eyJ1c2VyX2lkIjoiNjFkY2UxNTVmMTNkYmEyN2M2ODhkNGY0IiwiX2ZyZXNoIjpmYWxzZX0.Yd1MJw.QHQ6yjYVs59jR_R-W02UBFFhdSs; accountCenterSessionId=.eJw9zktLA0EQBOD_MmcP8-h55RwMC87mICLmsnRP9ySGdYXsajDifzfm4LGgqvi-1ccsp-GV1UoFwww-tWYcE4LPjnREBnWnhnaS-aBWDcdZrvHWj6wt5yDJgM0t1xApOmwhIwfPttYshgBF5-TQZfSmuQwUCJgkVAygNbBUTKR9daHGxEls0lVSgwo1ovfeBLHNx2Q8BErVCCdyNtr255pEeJjxU4blfWD6B843YH8pl7IusN2UZbu5H8uj1uXYnR-eO13sy7Jb711568fedl-745O5HtYDTpOM1_FZSP38AkE1VX8.FL7dqQ.GT9ctUk8zovzZCqPiTbOJ60yIOQ; doncusSessionId=eyJfZnJlc2giOmZhbHNlLCJ1c2VyX2lkIjoiNjE4OGU0NmVmMTNkYmE1NDIwMjU3Njc1In0.FL7duw.GuUycOx5E53sjSr1x7hkr1er474"
    }
    payload = {"filter": "{\"must\":[{\"hasMobile\":[{\"exist\":\"1\"}]}]}", "relation": "0", "start": "0", "end": "1000","filter_advance_search_filter_pool": "1","mode":"2"}
    res = requests.post(url, data=payload, headers=headers)
    #print(res.text)
    #print(res.json())
    res_json = res.json()['data']
    en_list = []
    for i in range(0, 200):
        en_list.append(res_json[i]['_id'])
    #print(en_list)
    list01 = ",".join(str(i) for i in en_list)
    #print(list01)

    # 通过获取到的企业id批量添加到crm
    url = 'https://sales-uat.tangees.com/api/leads/unlock-and-add-to-crm'
    headers02 = {
        "Cookie": "remember_token=61dce155f13dba27c688d4f4|65f02ed908efdcd0557b38f21085394c68f15a8ce27aa1b847c5381654821a7b1f92195d914d016158f2e48ca01af111a6f7617fd85d548f696ccda88b8d38cd; DISTINCT_ID=73b973d7-a6a8-4d49-8635-8de80f0bec0d; marketingSessionId=eyJ1c2VyX2lkIjoiNjFkY2UxNTVmMTNkYmEyN2M2ODhkNGY0IiwiX2ZyZXNoIjpmYWxzZX0.Yd1MJw.QHQ6yjYVs59jR_R-W02UBFFhdSs; accountCenterSessionId=.eJw9zktLA0EQBOD_MmcP8-h55RwMC87mICLmsnRP9ySGdYXsajDifzfm4LGgqvi-1ccsp-GV1UoFwww-tWYcE4LPjnREBnWnhnaS-aBWDcdZrvHWj6wt5yDJgM0t1xApOmwhIwfPttYshgBF5-TQZfSmuQwUCJgkVAygNbBUTKR9daHGxEls0lVSgwo1ovfeBLHNx2Q8BErVCCdyNtr255pEeJjxU4blfWD6B843YH8pl7IusN2UZbu5H8uj1uXYnR-eO13sy7Jb711568fedl-745O5HtYDTpOM1_FZSP38AkE1VX8.FL7dqQ.GT9ctUk8zovzZCqPiTbOJ60yIOQ; doncusSessionId=eyJfZnJlc2giOmZhbHNlLCJ1c2VyX2lkIjoiNjE4OGU0NmVmMTNkYmE1NDIwMjU3Njc1In0.FL7duw.GuUycOx5E53sjSr1x7hkr1er474"
}
    data = {"business_type": "customer", "target_user_ids": f'{user_id}', "entity_ids": f'{list01}', "entity_type": "enterprise","source": "1"}
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
        "Cookie": "remember_token=61dce155f13dba27c688d4f4|65f02ed908efdcd0557b38f21085394c68f15a8ce27aa1b847c5381654821a7b1f92195d914d016158f2e48ca01af111a6f7617fd85d548f696ccda88b8d38cd; DISTINCT_ID=73b973d7-a6a8-4d49-8635-8de80f0bec0d; marketingSessionId=eyJ1c2VyX2lkIjoiNjFkY2UxNTVmMTNkYmEyN2M2ODhkNGY0IiwiX2ZyZXNoIjpmYWxzZX0.Yd1MJw.QHQ6yjYVs59jR_R-W02UBFFhdSs; accountCenterSessionId=.eJw9zktLA0EQBOD_MmcP8-h55RwMC87mICLmsnRP9ySGdYXsajDifzfm4LGgqvi-1ccsp-GV1UoFwww-tWYcE4LPjnREBnWnhnaS-aBWDcdZrvHWj6wt5yDJgM0t1xApOmwhIwfPttYshgBF5-TQZfSmuQwUCJgkVAygNbBUTKR9daHGxEls0lVSgwo1ovfeBLHNx2Q8BErVCCdyNtr255pEeJjxU4blfWD6B843YH8pl7IusN2UZbu5H8uj1uXYnR-eO13sy7Jb711568fedl-745O5HtYDTpOM1_FZSP38AkE1VX8.FL7dqQ.GT9ctUk8zovzZCqPiTbOJ60yIOQ; doncusSessionId=eyJfZnJlc2giOmZhbHNlLCJ1c2VyX2lkIjoiNjE4OGU0NmVmMTNkYmE1NDIwMjU3Njc1In0.FL7duw.GuUycOx5E53sjSr1x7hkr1er474"
    }

    while True:
        is_com = requests.get(url=f"https://sales-uat.tangees.com/api/tungee-crm/export-task/{taskid}/result",
                              headers=headers03)
        if is_com.json()['status'] == 2:
            #ab = time.localtime(int(time.time()))
            #print("完成时间：")

            print(str(threadName)+"--完成时间："+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')))
            # print("已完成")
            print(str(threadName)+"--成功数：" + str(is_com.json()['customer_info']['success_count']))
            print(str(threadName)+"--失败数：" + str(is_com.json()['customer_info']['failure_count']))
            print(str(threadName) + "--联系人成功数：" + str(is_com.json()['contact_info']['success_count']))
            print(str(threadName) + "--联系人失败数：" + str(is_com.json()['contact_info']['failure_count']))
            is_fail = is_com.json()['customer_info']['failure_count']
            if (is_fail !=0):
                #打印出第一条线索失败的原因
                for i in range(100000):
                  print(str(threadName)+"--失败原因："+str(is_com.json()['customer_info']['failure_list'][i]['failure_msg']))
            break;
try:
    _thread.start_new_thread(add_to_CRM,("Thread-1","6188e46ef13dba5420257675",))

except:
    print("ERROR:启动线程失败")

while 1 :
    pass






