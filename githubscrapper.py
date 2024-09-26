from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
cdp = r"C:\webdrivers\chromedriver.exe" 
service = Service(cdp) 
# on = True
# while on:
#           def five_Sec():
#                     time.sleep(5)
#                     driver = webdriver.Chrome(service=service)
#                     driver.get("https://www.amazon.in/Professional-Cordless-Carrying-Accessories-Warranty/dp/B01MG68TVZ")
#                     price = driver.find_element(By.CLASS_NAME, "a-price-whole")
#                     print(price.text)
#                     driver.quit()

#           five_Sec()

driver = webdriver.Chrome(service=service)
driver.get("https://github.com/Rohit-YV")
repo="https://github.com/Rohit-YV"
time.sleep(2)
res = driver.find_elements(By.CLASS_NAME, "wb-break-all")
time.sleep(2)
link=[]
flink=[]
def going_for_raw(second_page):
          pass
          # raw=driver.find_element(By.CLASS_NAME,"gUkoLg")
          # raw.click()
          # html = driver.page_source
          # html=f"{html}"
          # print(html)



def loop(next_page):
          global a
          driver.get(next_page)
          time.sleep(2)
          res2 = driver.find_elements(By.CLASS_NAME, "Link--primary")
          for a in res2:
          
                    if "py" in a.text:
                              second_page =f"{next_page}/blob/main/{a.text}"
                              print(second_page)
                    elif "js" in a.text:
                              second_page =f"{next_page}/blob/main/{a.text}"
          going_for_raw(second_page)





for i in res:
          link.append(i.text)
# print(link)
for l in link:
          next_page = f"{repo}/{l}"
          flink.append(next_page)
          loop(next_page)
print(next_page)
# print(flink)
# loop(next_page)




driver.quit()
