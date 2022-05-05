import unittest

from api_autotest.common.requests_handler import RequestsHandler


class LoginTest(unittest.TestCase):
    def setUp(self):
        # 请求类实例化
        self.req = RequestsHandler()

    def tearDown(self):
        self.req.close_session()

    def test_login_success(self):
        login_url = 'http://user-test.tangees.com/api/individual-user/login'
        payload = {"phone": "17806533496",
                   "password": "16a9e283c0de31705b00f8e04e1a2b4d",
                   "remember": "0",
                   "code": "",
                   "area_code": "86"}
        headers = {"Referer": "http://user-test.tangees.com/users/sign-in?returnTo=%2Fhome"}
        res = self.req.visit('post', login_url, data=payload,headers=headers)

        #print(res['msg'])
        self.assertEqual(1, res['stat'])
    def test_login_fail(self):
        #密码错误
        login_url = 'http://user-test.tangees.com/api/individual-user/login'
        payload = {"phone": "17806533496",
                   "password": "067814ab0c661115d7ba546bb81bf7a",
                   "remember": "0",
                   "code": "",
                   "area_code": "86"}
        headers = {"Referer": "http://user-test.tangees.com/users/sign-in?returnTo=%2Fhome"}
        res = self.req.visit('post', login_url, data=payload,headers=headers)

        self.assertEqual("Account or pwd error", res['msg'])
    def test_login_account_fail(self):
        #账号不存在,没有注册过
        login_url = 'http://user-test.tangees.com/api/individual-user/login'
        payload = {"phone": "17806533488",
                   "password": "16a9e283c0de31705b00f8e04e1a2b4d",
                   "remember": "0",
                   "code": "",
                   "area_code": "86"}
        headers = {"Referer": "http://user-test.tangees.com/users/sign-in?returnTo=%2Fhome"}
        res = self.req.visit('post', login_url, data=payload,headers=headers)

        self.assertEqual("mobile not register", res['msg'])


if __name__ == '__main__':
    unittest.main()
