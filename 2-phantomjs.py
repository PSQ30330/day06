from selenium import webdriver
import time
path = r"D:\Che\phantomjs-2.1.1-windows\bin\phantomjs.exe"
browser = webdriver.PhantomJS(executable_path=path)
browser.get('https://www.baidu.com/')
time.sleep(3)
browser.save_screenshot("./pic/baidu1.png")

