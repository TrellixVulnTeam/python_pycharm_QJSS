# import unittest
# #测试MathMethod类
# class TestMathMethod():
#     #编写测试用例
#     def test_add_two_positive(self):
#         res = TestMathMethod(1,1).add()
#         print("1+1结果是：",res)
#         self.assertEqual(2,res,"两个整数相加出错！")
# # import unittest
# # class TestDemo(unittest.TestCase):
# #     # test_sub用例
# #     def test_sub(self):
# #         self.assertEqual(2-1,1)
# #     # test_add用例
# #     def test_add(self):
# #         self.assertEqual(2+1,3)
# if __name__ == "__main__":
#     # unittest.main()是运行主函数
#     unittest.main(verbosity=2)
import unittest
#测试MathMethod类
class TestMathMethod(unittest.TestCase):
    #编写测试用例
    def test_add_two_positive(self): #测试两个正数相加
        res=TestMathMethod(1,1).add()
        print("1+1的结果是：",res)
        self.assertEqual(2,res,"两个正数相加出错！") #断言
    def test_add_two_zero(self): #测试两个0相加
        res = TestMathMethod(0, 0).add()
        print("0+0的结果是：", res)
        self.assertEqual(0, res, "两个0相加出错！") #断言
    def test_add_two_negative(self): #测试两个负数相加
        res = TestMathMethod(-1, -1).add()
        print("-1+(-1)的结果是：", res)
        self.assertEqual(-2, res, "两个负数相加出错！") #断言
if __name__ == '__main__':
    unittest.main()
