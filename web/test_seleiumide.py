# Generated by Selenium IDE

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTest():
    def setup_method(self, method):
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.debugger_address = "127.0.0.1:9222"  # 用本机的端口9222进行Chrome调试窗口
        self.driver = webdriver.Chrome(chrome_options=chrome_opts)
        # self.driver = webdriver.Chrome()

    def teardown_method(self, method):
        self.driver.quit()

    def test_test(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.NAME,"os_username")