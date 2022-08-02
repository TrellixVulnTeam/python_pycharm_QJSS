import _thread
import requests
import time
import datetime
import openpyxl
import pandas as pd

def sheet_method():
    wk = openpyxl.load_workbook('D:\\钉钉文件\\交付记录\\交付记录02.xlsx')
    wk.remove(wk.worksheets[0])
    wk.create_sheet(title='sheet1',index=0)
    wk.close()
    wk.save('D:\\钉钉文件\\交付记录\\交付记录02.xlsx')

# 找企业高筛获取企业id（entity_ids）
url = 'https://sales-test.tangees.com/api/advance-search'
headers = {
    "Cookie":"DISTINCT_ID=a441cf24-6758-4c90-9675-bd0f807de112; __last_enter_version=sales; sessionId=.eJw1zjsKQjEQheG9pLbIZDLJxM3IPNFCkatW4t69IFan-Dnwvcspt3icy_G5veJQThcvx-KtCaUDeAjqnL3rtCZQrU5TI5fEEHceK3kGTjZmsQ4KtMfKvWlFVIQ6yXG_-75pGbTSotNoC8lSekJTqgNs2qqrKTddFGWH3GO7yi1uzz_t9Yjtxxs1hogoioMYGTJ7Mnn5fAHbTT1m.Fbk0bQ.hBa5aCH5ruHOG4lrfLeDFsspSbM; SecurityCenterDuId=IllON0ZMcFlFMjBlRWFycitGbFFHYVdRPSI.Fbk05A.5iX6D9iVvZ9KltsyjkpSuFetE2E; _co_i=623943dce572f06e41788438; marketingSessionId=eyJ1c2VyX2lkIjoiNjJiYTczNGNlNTcyZjAzYzU3NTdhNzhlIiwiX2ZyZXNoIjpmYWxzZX0.Yternw.nSzLS1TCIOCXKSU5n97C8kvIQYk; accountCenterSessionId=.eJw9js1Kw0AURt9l1l3Mnf_brVKp2AShEOIm3Jm5Y5QkQhOtRHx3g4Lbw_k-zpeYmHM30wd3y1uXo9gXGmbeie4li71gp0NwHhN5z5EcslWBTAzBB6WQMRkkjmx1AU6Wy8YdJpkg2WQITQaLG5OF2GFw0liApDVoo7S0QCa5AsW7GAATWCoS0aM3EcixL2In3me-_MU4lT1pZ9h6VaRROWiFYOUmdeXCc_8fP__67fr42TbHtbo7Lqc1D_WNlE_NYXxo7sf6_LzU59xXr6e1atprfVuN20_qaZp42MZXjuL7B-G5VLs.Fbk9Zg.41v-sK6oBlrxqTbIH4_iOM2PVIM; doncusSessionId=eyJfZnJlc2giOmZhbHNlLCJ1c2VyX2lkIjoiNjIzOTQzZGNlNTcyZjA2ZTQxNzg4NDNjIn0.Fbk9hQ.odchsLwDEJFE8l0dgP3wEkRV8CQ"

}
payload = {"filter": "{\"must\":[{\"hasMobile\":[{\"not_exist\":\"1\"}]}]}", "relation": "0", "start": "400", "end": "450",
           "filter_advance_search_filter_pool": "1", "mode": "2"}
res = requests.post(url, data=payload, headers=headers)
# print(res.text)
# print(res.json())
res_json = res.json()['data']
num = res.json()['size']
print(num)
en_list = []
enname_list = []
for i in range(num):
    en_list.append(res_json[i]['_id'])
    enname_list.append(res_json[i]['name'])
#print(en_list)
#print(enname_list)
#删除原有表格与数据
sheet_method()
filename = "交付记录02.xlsx"
xfile = openpyxl.load_workbook('D:\\钉钉文件\\交付记录\\%s'%filename)  # 加载文件
sheet1 = xfile.worksheets[0]
#xfile.remove(sheet1)
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
xfile.save('D:\\钉钉文件\\交付记录\\%s'%filename)   #保存文件

#xlsx文件格式转换为csv格式
data_xls = pd.read_excel('D:\\钉钉文件\\交付记录\\%s'%filename, index_col=0)
data_xls.to_csv('D:\\钉钉文件\\交付记录\\交付记录02.csv', encoding='utf-8')
