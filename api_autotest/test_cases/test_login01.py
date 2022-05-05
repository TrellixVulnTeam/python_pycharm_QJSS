import unittest
from api_autotest.common.requests_handler import RequestsHandler
from api_autotest.common.excel_handler import ExcelHandler
import ddt
import json
@ddt.ddt
class TestLogin(unittest.TestCase):
    # 读取excel中的数据
    excel = ExcelHandler('../data/login_cases.xlsx')
    case_data = excel.read_excel('login')
    print(case_data)
    def setUp(self):
        # 请求类实例化
        self.req = RequestsHandler()
    def tearDown(self):
        # 关闭session管理器
        self.req.close_session()
    @ddt.data(*case_data)
    def test_login_success(self,items):
        headers = eval(items['headers'])
        data = eval(items['data'])
        # 请求接口
        res = self.req.visit(method=items['method'],url=items['url'],data=data,headers=headers)
        print(res['stat'])
        try:
            # 断言：预期结果与实际结果对比
            self.assertEqual(res['stat'], items['expected_result'])
            result = 'Pass'
        except AssertionError as e:
            result = 'Fail'
            raise e
        finally:
            # 将响应的状态码，写到excel的第10列，即写入返回的信息
            TestLogin.excel.write_excel("../data/login_cases.xlsx", 'login', items['case_id'] + 1, 10, res['stat'])
            # 将响应的msg，写到excel的第11列，即写入返回的信息
            TestLogin.excel.write_excel("../data/login_cases.xlsx", 'login', items['case_id'] + 1, 11, res['stat'])
            # 如果断言成功，则在第11列(测试结果)写入Pass,否则，写入Fail
            TestLogin.excel.write_excel("../data/login_cases.xlsx", 'login', items['case_id'] + 1, 12, result)
if __name__ == '__main__':
    unittest.main()