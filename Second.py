from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, datetime
import pandas as pd

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument("--log-level=3")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
listofdict = list()

file = pd.read_excel('Merged file.xlsx')
listofregion = file.iloc[:, 0].tolist()
listofwebsite = file.iloc[:, 1].tolist()
time.sleep(20)
for i in range(20780,200000):
    datadict  = dict()
    driver.get(listofwebsite[i])
    time.sleep(1)
    datadict['Region'] =listofregion[i]
    datadict['Web'] =listofwebsite[i]

    try:
        driver.find_element_by_xpath('//div[@class="btndetails14_contact opt19_btncontact tel_contact"]').click()
        time.sleep(1)

        driver.find_element_by_xpath('//a[@id="btn-contactpartel"]').click()
        time.sleep(0.5)
        datadict['Phone']= driver.find_element_by_xpath('//span[@id="tel_1"]').text
        
    except:
        datadict['Phone'] =""

    print(datadict)
    listofdict.append(datadict)

    df = pd.DataFrame.from_dict(listofdict)  
    df.to_excel(f'20780_End.xlsx',index=False)
    print('Data Saved in Excel!!')
