import time

from selenium import webdriver
path = r"D:\Che\chromedriver.exe"
browser = webdriver.Chrome(executable_path=path)
url = "https://www.baidu.com/"
browser.get(url)
# time.sleep(3)
my_input = browser.find_element_by_id('kw')
my_input.send_keys('新垣结衣')
time.sleep(3)
button = browser.find_element_by_id('su')
button.click()
time.sleep(3)
# img = browser.find_element_by_class_name("op-img-address-link-imgs")
img = browser.find_element_by_xpath('//*[@id="2"]/div[2]/div[1]/a[1]/img')
# img = browser.find_element_by_css_selector('op-img-address-link-imgs' >. )
img.click()
time.sleep(3)
# browser.quit()