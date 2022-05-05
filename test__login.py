import unittest
from api_autotest.common.excel_handler import ExcelHandler

class TestLogin(unittest.TestCase):
    #读取excel中的数据
    excel = ExcelHandler('')
    case_data = excel.read_excel('')