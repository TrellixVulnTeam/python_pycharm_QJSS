#导入requests模块
import requests
class RequestHandler:
    def __init__(self):
        """session管理器"""
        self.session = requests.session()
    def visit(self, method, url, params=None, data=None, json=None, headers=None, **kwargs):
        return self.session.request(method,url, params=params, data=data, json=json, headers=headers,**kwargs)
    def close_session(self):
        """关闭session"""
        self.session.close()
if __name__ == '__main__':
    # 以下是测试代码
    # post请求接口
    url = 'http://user-test.tangees.com/api/individual-user/login'
    payload = {"phone":"17806533496","password":"16a9e283c0de31705b00f8e04e1a2b4d","remember":"0","code":"","area_code":"86"}
    headers = {"Referer": "http://user-test.tangees.com/users/sign-in?returnTo=%2Fhome"}
    req = RequestHandler()
    login_res = req.visit("post", url, data=payload,headers=headers)
    print(login_res.text)
