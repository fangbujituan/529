from selenium import webdriver
import time
# 自动化访问百度，并搜索
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
print(driver.title)
time.sleep(2)
# 刷新页面
# driver.refresh()
driver.find_element_by_id("kw").send_keys("天霸")
driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit()
