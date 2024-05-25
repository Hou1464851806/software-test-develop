# import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 用户打开页面
        self.browser.get("http://localhost:8000")
        # 网页标题应该有“To-Do” 头部也应该有这个词
        self.assertIn("To-Do",self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("To-Do",header_text)
        # 页面有可供输入的输入框
        inputbox = self.browser.find_element(By.ID,'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')
        # 输入了文本
        inputbox.send_keys('Buy flowers')
        # 用户按回车后会创建一个代办事项
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID,'id_list_table')
        rows = table.find_element(By.TAG_NAME,'tr')
        self.assertIn("1: Buy flowers",[row.text for row in rows])
        # 会继续出现输入框来等待创建新的代办事项

        # 用户关闭网页后，使用上次相同的url进入，应该可以看到之前创建所有的代办事项
        self.fail("Finish the test")


if __name__ == "__main__":
    unittest.main()
