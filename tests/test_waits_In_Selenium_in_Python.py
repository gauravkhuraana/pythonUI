import requests
import random

import json
import getpass
from os import path
#from tests.configurations import client_id, client_secret, username, password, scope, grant_type , resource  
from tests.configurations import authentication_url#,alias
#from tests.globalVariables import auth_url_token
from tests.helper.API import API
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from tests.helper.json import jsonOps
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By

#For running in a pipeline, where we need username, password
#from tests.configurations import username,password
username=""
password=""
 
# Using user directory to login to azure with /.auth/me so user need not to enter username and password everytime
def getAccessTokenViaUI(self):        
      options = webdriver.ChromeOptions() 
      #options.headless = True
      alias = getpass.getuser()
      options.add_argument(f"user-data-dir=C:\\Users\\{alias}\\AppData\\Local\\Google\\Chrome\\User Data")
      #options.add_argument('--profile-directory=Default')
      driver=webdriver.Chrome(ChromeDriverManager().install(), options=options)
      
      # URL to get token in Azure via UI
      driver.get(f"{authentication_url}/.auth/me")

      #explicit wait to handle the page of azure
      wait=WebDriverWait(driver, 8)
      try:
        # you can change @test.com to the domain of your AAD in Azure 
        selectProfile=wait.until(EC.visibility_of_element_located((By.XPATH,"//small[contains(text(),'@test.com')]")))
        selectProfile.click()
      except:
        print(" User profile selection was not needed, since the user was already logged in")  
     
      ## Implicit wait
      driver.implicitly_wait(10)
      
      # Tag name where token comes
      element = driver.find_element_by_tag_name('pre')
      #instead of gettext in python we use text
      tokens= element.text

      #
      jsonObj= json.loads(tokens)
      access_token=jsonObj[0]['access_token']
      #print(" \n access_token is \n", access_token)
      return access_token
 

#When you have username and password to login to Azure Websites, use this code for page which is like /.auth/me

def getAccessTokenViaUIWithUserNameandPassword(self):        
      #options = webdriver.ChromeOptions() 
      driver=webdriver.Chrome(ChromeDriverManager().install())
      
      driver.get(f"{authentication_url}.auth/me")
      #driver.implicitly_wait(20)

      #userNameTextBox = driver.find_element_by_name('loginfmt')
      wait=WebDriverWait(driver, 20)
      
      userNameTextBox=wait.until(EC.visibility_of_element_located((By.NAME, "loginfmt")))
      userNameTextBox.send_keys(username)
      #userNameTextBox.
      #gakhuran@microsoft.com
      infomationMessage=wait.until(EC.visibility_of_element_located((By.ID,'idSIButton9')))       
      infomationMessage.click()

      passwordOption = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='Password']")))
      passwordOption.click()

      passwordEnter = wait.until(EC.visibility_of_element_located((By.ID,'passwordInput')))
      passwordEnter.send_keys(password)
      #//div[@id="passwordArea"]
      
      submitButton = driver.find_element_by_id('submitButton')
      submitButton.click()
      #//span[@id="submitButton"]

      infomationMessage = driver.find_element_by_id('idSIButton9')      
      infomationMessage.click()

      element = driver.find_element_by_tag_name('pre')
      tokens= element.text
      driver.quit()
      jsonObj= json.loads(tokens)
      access_token=jsonObj[0]['access_token']
      #print(" \n access_token is \n", access_token)
      return access_token
    
