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
scrape=input("what page would you like to scrape? ")
driver = webdriver.Chrome(service=service)
driver.get(f"{scrape}")
repo="https://github.com/Rohit-YV"
time.sleep(2)
res = driver.find_elements(By.CLASS_NAME, "wb-break-all")
time.sleep(2)
link=[]
flink=[]
def going_for_raw(second_page):
    # Navigate to the second page (file page)
    driver.get(second_page)
    
    try:
        # Find and click the "Raw" button using XPath for better accuracy
        raw_button = driver.find_element(By.XPATH, '//a[contains(@href, "/raw/")]')
        raw_button.click()
        time.sleep(2)
        
        # Fetch the raw HTML content
        html_content = driver.page_source  # Correct way to get the HTML content of the page
        if "password" in html_content:
          print(f"found password{second_page}")
        
    except Exception as e:
       
        print(f"Error fetching raw content: {e}")




def loop(next_page):
          global a
          global second_page
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
