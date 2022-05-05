import _thread
import requests
import time
import datetime
import openpyxl
import pandas as pd

# 找企业高筛获取企业id（entity_ids）
url = 'https://sales-uat.tangees.com/api/advance-search'
headers = {
    "Cookie": "remember_token=61dce155f13dba27c688d4f4|65f02ed908efdcd0557b38f21085394c68f15a8ce27aa1b847c5381654821a7b1f92195d914d016158f2e48ca01af111a6f7617fd85d548f696ccda88b8d38cd; DISTINCT_ID=73b973d7-a6a8-4d49-8635-8de80f0bec0d; sessionId=.eJw1zjuOgjEMBOC7pN4ituM44TIofmkpQKsfqBB3JxLaaorRjL5XOecR999yehzP-Cnni5dTccTF6QAei1SkNRXDBdWqmBr7SorlPvrMIUEybIxlDRR4l3U01EqkBFXYac99Z1oGz7Ro3HESW66WgMq1g4nNOlEH6uQoG_IXx3Xd4vb4pz3vcXx5HUjaYpuboWP2hrhvBpX3B8muPB8.FL543w.7jZwi_GtQkL1VP7H2lEGzh7FGjE; marketingSessionId=eyJ1c2VyX2lkIjoiNjFkY2UxNTVmMTNkYmEyN2M2ODhkNGY0IiwiX2ZyZXNoIjpmYWxzZX0.Ydznmw.EXcOfyAUNZSeZzZJ8hYW53rm6hI; accountCenterSessionId=.eJw9zs1OwzAQBOB38ZmDf9b2uldSDohE4gBRe4ns3bXatASpCSCBeHeiHDiONDP6ftTHLLfhzGqngmES4301jku2kQIiQwV1p4Z6k_mkdjVfZ1nj1o-sLacgaMCmmijEEl2uIWUOni1RElMgi07oskvZm-oSlFCAiwTKAbQGFspYtCcXKCKjWNQkWIGAYvbemyC2-ojGQyhIRhiLs9FurkmEhzl_yrC8D1z-gfMGbJuDa5uL78bD0vV7aO-1br-Pb0_9w_k4vizd-Axt_zq24-Ola_ZuPaRTnia5ruMvKer3D0QRVZI.FL55Lg.gmmxqNZnkK95zcRmO8izrxozTL0; doncusSessionId=eyJfZnJlc2giOmZhbHNlLCJ1c2VyX2lkIjoiNjE4OGU0NmVmMTNkYmE1NDIwMjU3Njc1In0.FL55Lg.-U4UC2Q4aRwuYXfoGxQKjSVwd_4"
}
payload = {"filter": "{\"must\":[{\"hasMobile\":[{\"not_exist\":\"0\"}]}]}", "relation": "0", "start": "0", "end": "1000",
           "filter_advance_search_filter_pool": "1", "mode": "2"}
res = requests.post(url, data=payload, headers=headers)
# print(res.text)
# print(res.json())
res_json = res.json()['data']
print(res.json()['size'])
en_list = []
enname_list = []
for i in range(1000):
    en_list.append(res_json[i]['_id'])
    enname_list.append(res_json[i]['name'])
#print(en_list)
#print(enname_list)
xfile = openpyxl.load_workbook('D:\\钉钉文件\\交付记录\\交付记录01.xlsx')  # 加载文件
sheet1 = xfile.worksheets[0]
sheet1.cell(1, 1).value = "entity_id"
sheet1.cell(1, 2).value = "entity_name"
sheet1.cell(1, 3).value = "entity_type"
sheet1.cell(1, 4).value = "rate"
for i in range(len(en_list)):
    sheet1.cell(i + 2, 1).value = en_list[i]
    sheet1.cell(i + 2, 2).value = enname_list[i]
    sheet1.cell(i + 2, 3).value = "enterprise"
    sheet1.cell(i + 2, 4).value = "1"
# 保存数据，如果提示权限错误，需要关闭打开的excel
xfile.save('D:\\钉钉文件\\交付记录\\交付记录01.xlsx')

#xlsx文件格式转换为csv格式
data_xls = pd.read_excel('D:\\钉钉文件\\交付记录\\交付记录01.xlsx', index_col=0)
data_xls.to_csv('D:\\钉钉文件\\交付记录\\交付记录01.csv', encoding='utf-8')
