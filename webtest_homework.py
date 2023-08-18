from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import os
import unittest, time
import HTMLTestRunner
from time import sleep
class webtest_php(unittest.TestCase):  # 測試項目
    def setUp(self):
        self.verificationErrors=[]
        self.test=webdriver.Firefox()
        self.url="https://flipclass.stust.edu.tw/"  # 要執行自動測試的網站
    def test_login(self):
        pa=self.test
        pa.get(self.url)
        user=pa.find_element("name", "account")
        user.send_keys('4A9G0009')
        passwd=pa.find_element("name", "password")
        passwd.send_keys('s02070207')

        pa.find_element("xpath", "//button[@data-role='form-submit']").click() #點擊登入按鈕
        sleep(1)
        try:
            pa.find_element("xpath", "//*[@id='categoryForm']/div[3]/div/a[2]").click() #如果有登入過就點擊按鈕 否則沒偵測到就是沒重複登入
        except:
            print("無重複登入")
            
        sleep(2)
        pa.find_element("xpath","//*[@id='xbox2-inline']/div[2]/div/div[2]/div/ul/li[4]/div/div/div[2]/div/div[1]/a").click() #跳到軟體工程
        sleep(1)
        pa.find_element("xpath","//*[@id='mbox-inline']/div/div[9]/ul/li[8]/a/span[2]").click() #跳到作業頁面
        sleep(1)
        pa.find_element("xpath","//*[@id='homeworkListTable']/tbody/tr[6]/td[2]/div/div/div[2]").click() #跳到加分作業
        
        #pa.get("https://flipclass.stust.edu.tw/course/homework/70264")                        #跳轉到作業頁面
        sleep(2)

        press_button=pa.find_element("xpath","//a[@data-modal-title='交作業']").click()       #點擊交作業
        sleep(2)

        iframe = pa.find_element("xpath","//*[@id='lgIframeModalId']/div/div/div[2]/iframe")  #第一層iframe
        pa.switch_to.frame(iframe)
        title=pa.find_element("xpath","//*[@id='title']/div/div/div/input") #找到標題並修改名稱
        title.clear()
        title.send_keys("4A9G0009 謝明軒")
        sleep(1)
        pa.find_element(By.CLASS_NAME,"btn.btn-default").click() #上傳檔案
        sleep(1)
        send_document=pa.find_element("xpath","/html/body/div[2]/div/div/div/div/div/div/div[2]/div/form/div[3]/div/div/div/div[2]/div/div/div[2]/div/input") #抓視窗並丟py檔案
        send_document.send_keys(os.getcwd()+"\webtest_homework.py") #os.getcwd是目前的目錄+檔案
        sleep(1)
        pa.find_element("xpath","/html/body/div[2]/div/div/div/div/div/div/div[2]/div/form/div[3]/div/div/div/div[2]/div/div/div[3]/div[2]/button").click() #關閉視窗
        sleep(1)
        pa.find_element("xpath","/html/body/div[2]/div/div/div/div/div/div/div[2]/div/form/div[6]/div/button[1]").click()#按下繳交
        pa.switch_to.default_content() #跳出iframe

    def tearDown(self):
        pass

if __name__== "__main__":
    testsuite=unittest.TestSuite()
    testsuite.addTest(webtest_php("test_login"))

fp=open("result.html",'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="測試報告",description="測試情況如下：")
runner.run(testsuite)
fp.close()