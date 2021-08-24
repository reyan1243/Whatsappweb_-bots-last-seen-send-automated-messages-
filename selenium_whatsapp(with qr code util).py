
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# download the chrome Web driver in your system and copy paste the path down there in the 9th line
driver = webdriver.Chrome('C:/Users/OMA/Desktop/chromedriver')
# it will open a new chrome window and load a QR code you have to scan it to connect it with mobile WhatsApp
url = "https://web.whatsapp.com/"
driver.get(url)

# note: you must scan the qr code with in 15 seconds otherwise you can change the duration from line 17

## search/click for name to whom you want to send message
time.sleep(15)
search = driver.find_element_by_xpath("//div[@data-tab='3']")
search.click()
search.send_keys("Enter the name here")
search.send_keys(Keys.RETURN)


## for loop to send a range of messages
time.sleep(5)

# enter number of repetition
rep=10
for i in range(rep): ## jitny baar msg bhejna ha range sa control kry gy
    ## first find the messagr bar and click it and type message
    msg = driver.find_element_by_xpath("//div[@data-tab='6']")
    msg.click()


    msg.send_keys("enter your desired message here")  ## edr msg likhna ha jo b ha
    # time.sleep(0.000001)

    ## then  send message by clicking send button
    msg.send_keys(Keys.RETURN)
    # send.click()
    time.sleep(0.00000001)



