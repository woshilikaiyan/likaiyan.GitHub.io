import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBaidu(unittest.TestCase):
    """ 百度搜索测试 """

    # 类执行前调用
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.base_url = "https://www.baidu.com"
        cls.driver.maximize_window()

    # 封装百度搜索方法
    def search_result(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID,'kw').send_keys(search_key)
        self.driver.find_element(By.ID,'su').click()
        sleep(5)

    def test_search_key_selenium(self):
        """" 搜索关键字：selenium """
        search_key = 'selenium'
        self.search_result(search_key)
        # 虽然两个用例断言的结果一样，但是不建议断言放公共方法中，断言放测试用例中看的会更直观，而且有的测试用例虽然测试步骤一样，但是断言的结果未必一致
        self.assertEqual(self.driver.title, search_key+'_百度搜索')

    def test_search_key_unittest(self):
        """" 搜索关键字：unittest """
        search_key = 'unittest'
        self.search_result(search_key)
        self.assertEqual(self.driver.title, search_key + '_百度搜索')
        # 类结束执行调用

    def test_search_key_html(self):
        """" 搜索关键字：html """
        search_key = 'html'
        self.search_result(search_key)
        self.assertEqual(self.driver.title, search_key + '_百度搜索1')
        # 类结束执行调用"

    def test_search_key_python(self):
        """" 搜索关键字：python """
        search_key = 'python'
        self.search_result(search_key)
        self.assertEqual(self.driver.title, search_key + '_百度搜索2')

    # 类结束执行调用
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
