## www.udzial.com 

## Udzial Means Share 

### www.gauravkhurana.in

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import json
import time
#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())

alias="gauravkhurana"
def test_browserStart():
   driver = webdriver.Firefox()
   driver.get("https://duckduckgo.com/")

def test_viaWebDriverManager():
   options = webdriver.ChromeOptions() 
   options.add_argument("--headless")
   #options.headless = True
   options.add_argument(f"user-data-dir=C:\\Users\\{alias}\\AppData\\Local\\Google\\Chrome\\User Data")
   driver=webdriver.Chrome(ChromeDriverManager().install(), options=options)
   #driver.get("https://gmail.com")
   #driver.get("https://portal.azure.com")
   #driver.get("https://outlook.live.com/")
   #driver.get("https://stackoverflow.com/")
   
   driver.implicitly_wait(15)
   
   driver.save_screenshot("image.png")   
   element = driver.find_element_by_tag_name('pre')
   tokens= element.text
   driver.save_screenshot("image.png") 
   #time.sleep(3000)
   print(" \n \n The full response is as ", tokens)
   jsonObj= json.loads(tokens)
   id_token=jsonObj[0]['id_token']
   print(" \n \n id_token is \n", id_token)

def test_openGmailHeadless():
   options = webdriver.ChromeOptions() 
   options.add_argument("--headless")
   #options.headless = True
   options.add_argument(f"user-data-dir=C:\\Users\\{alias}\\AppData\\Local\\Google\\Chrome\\User Data")
   driver=webdriver.Chrome(ChromeDriverManager().install(), options=options)
   driver.get("https://gmail.com")
   # Getting current URL source code
   get_title = driver.title
   # Printing the title of this URL
   print("Title is ",get_title)
   driver.save_screenshot("gmail1.png") 
   driver.quit()


def test_openGmail():
   options = webdriver.ChromeOptions() 
   #options.add_argument("--headless")
   #options.headless = True
   options.add_argument(f"user-data-dir=C:\\Users\\{alias}\\AppData\\Local\\Google\\Chrome\\User Data")
   driver=webdriver.Chrome(ChromeDriverManager().install(), options=options)
   driver.get("https://gmail.com")
   # Getting current URL source code
   get_title = driver.title
   # Printing the title of this URL
   print("Title is ",get_title)
   driver.save_screenshot("gmail.png") 
   driver.quit()
      