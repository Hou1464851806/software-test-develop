# import chromedriver_binary
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 用户打开页面
        self.browser.get("http://localhost:8000")
        # 网页标题应该有“To-Do”
        self.assertIn(
            "To-Do", self.browser.title
        ), "browser title was" + self.browser.title
        self.fail("Finish the test")
        # 页面有可供输入的输入框
        # 用户按回车后会创建一个代办事项
        # 会继续出现输入框来等待创建新的代办事项
        # 用户关闭网页后，使用上次相同的url进入，应该可以看到之前创建所有的代办事项


if __name__ == "__main__":
    unittest.main()
