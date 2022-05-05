import unittest
import re
from api_autotest.common.requests_handler import RequestsHandler
from api_autotest.common.excel_handler import ExcelHandler
import ddt
import json
from api_autotest.common.logger_handler import logger
from api_autotest.common.phone_helper import generate_mobile

@ddt.ddt
class TestLogin(unittest.TestCase):
    #读取excel中的数据
    excel = ExcelHandler('../data/login_cases.xlsx')
    case_data = excel.read_excel('login')
    case_data02 = excel.read_excel('login_test')
    print(case_data)
    print(case_data02)
    def setUp(self):
        #请求实例化
        self.req = RequestsHandler()
    def tearDown(self):
        #关闭session管理器
        self.req.close_session()
    @ddt.data(*case_data)
    def test_login_success(self,items):
        logger.info('-'*150)
        logger.info('这是第{}条用例：{}'.format(items['case_id'],items['case_title']))
        logger.info('当前用例测试数据：{}'.format(items))
        #headers = eval(items['headers'])
        #data = eval(items['data'])
        #请求接口
        res = self.req.visit(method=items['method'],
                             url=items['url'],
                             data=json.loads(items['data']),
                             headers=json.loads(items['headers']))
        # print(res['stat'])
        print(res)
        print(type(res))
        login_res = str(res).encode('utf-8')
        print(type(login_res))


        try:
            #断言：预期与实际结果对比
            self.assertEqual(res['stat'],items['expected_result'])
            logger.info('响应结果:{}'.format(res))
            result = 'Pass'
        except AssertionError as e:
            logger.error('用例执行失败,响应结果stat与预期不同：{}'.format(e))
            result = 'Fail'
            raise e

        finally:
            # 将响应的状态码，写到excel的第11列，即写入返回的响应状态码信息
            TestLogin.excel.write_excel("../data/login_cases.xlsx", 'login', items['case_id'] + 1, 11, res['stat'])
            # 将响应信息，写到excel的第12列，即写入返回的信息
            TestLogin.excel.write_excel("../data/login_cases.xlsx", 'login', items['case_id'] + 1, 12, login_res)
            # 如果断言成功，则在第13列(测试结果)写入Pass,否则，写入Fail
            TestLogin.excel.write_excel("../data/login_cases.xlsx", 'login', items['case_id'] + 1, 13, result)

    @ddt.data(*case_data02)
    def test_login_fail(self,items):
        """判断#new_phone#是否存在与用例数据中"""
        if "#new_phone" in items['data']:
            mobile = generate_mobile()
            #将#new_phone#代替为生成的手机号
            items['data'] = items['data'].replace('#new_phone#',mobile)
        logger.info('-' * 150)
        logger.info('这是第{}条用例：{}'.format(items['case_id'], items['case_title']))
        logger.info('当前用例测试数据：{}'.format(items))
        # headers = eval(items['headers'])
        # data = eval(items['data'])
        # 请求接口
        res = self.req.visit(method=items['method'],
                             url=items['url'],
                             data=json.loads(items['data']),
                             headers=json.loads(items['headers']))
        print(res['msg'])
        print(res)
        print(type(res))
        login_res = str(res).encode('utf-8')
        print(type(login_res))

        try:
            # 断言：预期与实际结果对比
            self.assertEqual(res['msg'], items['expected_result'])
            logger.info('响应结果:{}'.format(res))
            result = 'Pass'
        except AssertionError as e:
            logger.error('用例执行失败,响应结果msg与预期不同：{}'.format(e))
            result = 'Fail'
            raise e

        finally:
            # 将响应的状态码，写到excel的第11列，即写入返回的响应状态码信息
            TestLogin.excel.write_excel("../data/login_cases.xlsx", 'login_test', items['case_id'] + 1, 11, res['msg'])
            # 将响应信息，写到excel的第12列，即写入返回的信息
            TestLogin.excel.write_excel("../data/login_cases.xlsx", 'login_test', items['case_id'] + 1, 12, login_res)
            # 如果断言成功，则在第13列(测试结果)写入Pass,否则，写入Fail
            TestLogin.excel.write_excel("../data/login_cases.xlsx", 'login_test', items['case_id'] + 1, 13, result)
            # 将实际传入data参数，写在excel的第14列
            TestLogin.excel.write_excel("../data/login_cases.xlsx", 'login_test', items['case_id'] + 1, 14, items['data'])




if __name__ =='__main__':
    unittest.main()

