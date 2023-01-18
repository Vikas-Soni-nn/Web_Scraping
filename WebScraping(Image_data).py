import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
url ='https://www.veromoda.in/tops-t-shirts-vm/tops-t-shirts-t-shirts-vm'
# url = 'https://www.veromoda.in/tops-t-shirts-vm'
browser.get(url)
size = browser.get_window_size()



for i in range(1,2000):
    if i % 4 == 0:
        # browser.execute_script("window.scrollTo(0,{})".format(size['height'])) 
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    a = ActionChains(browser)
    m= browser.find_element("xpath","//body/div[4]/div[1]/div[1]/div[2]/div[{}]/div[1]/div[1]/a[1]/img[1]".format(i))
    a.move_to_element(m).perform()
    button = browser.find_element("xpath","//body/div[4]/div[1]/div[1]/div[2]/div[{}]/div[1]/div[1]/a[1]/img[2]".format(i))
    browser.execute_script("arguments[0].click();", button)
    time.sleep(4)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(4)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    div_tag = soup.find('div',{'class':"col-sm-2 zoom-thumbnails scrollThumb"})
    count = len(div_tag.find_all('div'))
    try:
        browser.execute_script("window.scrollTo(0, 250)")
        time.sleep(2)
        browser.find_element("xpath","//body/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[{}]/a[1]".format(count)).click()
        time.sleep(2)
        href = browser.find_element("xpath","//body/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[{}]/a[1]".format(count)).get_attribute("href")
        f = open(f'img-{i}.png','wb')
        f.write(requests.get(href).content)
        f.close()
        time.sleep(2)
    except Exception as e: print(e)
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
browser.quit()













