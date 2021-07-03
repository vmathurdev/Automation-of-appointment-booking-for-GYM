from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

import os
import getpass
url= "https://athletics.smu.ca/"

driver = webdriver.Chrome()
sign_in= ''
driver.get(url)
sign_in = driver.find_element_by_xpath('//*[@id="loginLink"]')
sign_in.click()
time.sleep(1)
smu_port= driver.find_element_by_xpath('//*[@id="divLoginOptions"]/div[2]/div[2]/div/button')
smu_port.click()
# sNumber= input("Enter your S-Number ")
# sPassword= input('Password: ')
sNumberBox= driver.find_element_by_xpath('//*[@id="username"]')
sPasswordBox= driver.find_element_by_xpath('//*[@id="password"]')
sNumberBox.clear()
sNumberBox.send_keys('')   ########ENTER YOUR SMU s-Number inside quotess inside send_keys || Example: sNumberBox.send_keys('s1321122')
sPasswordBox.clear()
sPasswordBox.send_keys('')   ########ENTER YOUR SMU s-Number password quotess inside send_keys || Example: sNumberBox.send_keys('password')
login_button= driver.find_element_by_xpath('//*[@id="loginSubmit"]')
login_button.click()
time.sleep(1)

menuOpen= driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]")
menuOpen.click()

time.sleep(2)
goReservation= driver.find_element_by_xpath('//*[@id="sidebar"]/ul[1]/li[1]/a/span[2]')
goReservation.click()


bookingSelector= driver.find_element_by_xpath('//*[@id="20d5f45c-8ba1-4162-ab6a-d6c8ec13e693"]')
bookingSelector.click()

#days= ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

day= input("Enter the day you want to join Gym [First three alphabet (eg: sun): ")
select_day= ''
if (day== 'Mon' or day== 'mon' or day== 'MON'):
    select_day= driver.find_element_by_xpath('//*[@id="list-group"]/div[1]/div/div[2]/div[1]/h4')
elif (day== 'Tue' or day== 'tue' or day== 'TUE' ):
    select_day= driver.find_element_by_xpath('//*[@id="list-group"]/div[2]/div/div[2]/div[1]/h4')
elif (day== 'Wed' or day== 'wed' or day== 'WED' ):
    select_day= driver.find_element_by_xpath('//*[@id="list-group"]/div[3]/div/div[2]/div[1]/h4')
elif (day== 'Thu' or day== 'thu' or day== 'THU' ):
    select_day= driver.find_element_by_xpath('//*[@id="list-group"]/div[4]/div/div[2]/div[1]/h4')
elif (day== 'Fri' or day== 'fri' or day== 'FRI' ):
    select_day= driver.find_element_by_xpath('//*[@id="list-group"]/div[5]/div/div[2]/div[1]/h4')
elif (day== 'Sat' or day== 'sat' or day== 'SAT'):
    select_day= driver.find_element_by_xpath('//*[@id="list-group"]/div[6]/div/div[2]/div[1]/h4')
elif (day== 'Sun' or day== 'sun' or day== 'SUN' ):
    select_day= driver.find_element_by_xpath('//*[@id="list-group"]/div[7]/div/div[2]/div[1]/h4')
else:
    print('Invalid input. Enter something such as: sun mon tue wed thu fri sat')

select_day.click()

time.sleep(1)

time_slot= int(input ("Check the screen and select the workout slot (1-9 sequentially {Count Horizontally)"))

if time_slot == 1:
    select_time= driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[7]/div[1]/div/div/div/button')
elif time_slot == 2:
    select_time= driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[7]/div[3]/div/div/div/button')
elif time_slot == 3:
    select_time= driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[7]/div[5]/div/div/div/button')
elif time_slot == 4:
    select_time= driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[7]/div[7]/div/div/div/button')
elif time_slot == 5:
    select_time= driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[7]/div[9]/div/div/div/button')
elif time_slot == 6:
    select_time= driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[7]/div[11]/div/div/div/button')
elif time_slot == 7:
    select_time= driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[7]/div[13]/div/div/div/button')
elif time_slot == 8:
    select_time= driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[7]/div[15]/div/div/div/button')
elif time_slot == 9:
    select_time= driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[7]/div[17]/div/div/div/button')
else:
    print("Invalid input")

select_time.click()

time.sleep(1)

code_of_conduct_1= driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/form[2]/div[1]/div[1]/div/div[2]/div/div/label[1]')
code_of_conduct_1.click()


code_of_conduct_2= driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/form[2]/div[1]/div[3]/div/div[2]/div/div/label[2]')
code_of_conduct_2.click()


code_of_conduct_3= driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/form[2]/div[1]/div[4]/div/div[2]/div/div/label[2]')
code_of_conduct_3.click()


code_of_conduct_4= driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/form[2]/div[1]/div[5]/div/div[2]/div/div/label[2]')
code_of_conduct_4.click()

code_of_conduct_5= driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/form[2]/div[1]/div[7]/div/div[2]/div/div/label[1]')
code_of_conduct_5.click()

time.sleep(0.5)

add_to_cart= driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/form[2]/div[2]/button[2]')
add_to_cart.click()
time.sleep (1)

checkout_button= driver.find_element_by_xpath('//*[@id="checkoutButton"]')
checkout_button.click()

time.sleep (0.7)

checkout_final= driver.find_element_by_xpath('//*[@id="CheckoutModal"]/div/div[2]/button[2]')
checkout_final.click()
print("You have made a booking! Check your email.")
time.sleep(2)
driver.quit()
