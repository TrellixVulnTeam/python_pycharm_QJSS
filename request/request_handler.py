import requests
class Requestcommon:
    def __init__(self):
        '''session管理器'''
        #创建session会话
        self.session = requests.session()
    def go(self,method,url,params=None,data=None,json=None,headers=None,**kwargs):
        return self.session.request(method,url,params=params,data=data,json=json,headers=headers,**kwargs)
    def close_session(self):
        '''关闭session'''
        self.session.close()



if __name__ =="__main__":
    url ='https://user-uat.tangees.com/api/individual-user/login'
    payload = {"phone": "17806533496",
               "password": "16a9e283c0de31705b00f8e04e1a2b4d",
               "remember": "1",
               "code": "",
               "area_code": "86"}
    headers = {
        "referer": "https://user-uat.tangees.com/users/sign-in"
    }
    req = Requestcommon()
    login_res = req.go("post",url,data=payload,headers=headers)
    print(login_res.json())
