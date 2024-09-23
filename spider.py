import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from urllib import *

visited_urls = set()
def get_url(url,keyword):
          try:
                    response = requests.get(url)
          except:
                    print(f"request faild{url}")
                    return
          if response.status_code == 200:

                    soup = BeautifulSoup(response.content,'html.parser')

                    a_tag = soup.find_all('a')
                    urls=[]
                    for tag in a_tag:
                              href = tag.get("href")
                              if href is not None and href  != "":
                                        urls.append(href)
                    # print(urls)
                    #finding out the unique urls

          for urls2 in urls:
                    if urls2 not in visited_urls:
                              visited_urls.add(urls2)
                              url_join=urljoin(url,urls2)
                              if keyword in url_join:
                                        print(url_join)
                                        get_url(url_join,keyword)
                              else:

                                        pass



url=input("enter the urls u want to spider:")
keyword=input("enter the keyword:")
get_url(url,keyword)

