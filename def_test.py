import time

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


'''
一个登录的小demo，请在下方配置自己的账户和密码。
'''

username = "YOURUSERNAME"
password = "YOURPASSWORD"



if __name__ == '__main__':
    driver = uc.Chrome()
    driver.get('https://login.taobao.com/member/login.jhtml')
    # 寻找用户名和密码输入框，键入用户名和密码
    driver.find_element(By.XPATH,'//*[@id="fm-login-id"]').send_keys(username)
    driver.find_element(By.XPATH,'//*[@id="fm-login-password"]').send_keys(password)

    time.sleep(4)
    # document.querySelector("#login-form > div.fm-btn > button")
    # 淘宝登录按钮用普通的click无法点击，这里采取js命令点击
    driver.execute_script('document.querySelector("#login-form > div.fm-btn > button").click()')

    time.sleep(9999)