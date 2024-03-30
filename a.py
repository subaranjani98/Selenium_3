from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

#Settng Up URL 's:
url = 'https://www.saucedemo.com/'
url2 = 'https://www.zenclass.in/login'
url3 = 'https://www.zenclass.in/dashboard'

# Setting up Firefox WebDriver
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(url)

# Displaying cookies before login for Saucedemo
print("Cookies before login saucedemo:")
print(driver.get_cookies())
print(driver.current_url)
sleep(3)

# Entering credentials and logging in for Saucedemo
element_of_name = driver.find_element(By.ID, "user-name")
element_of_name.send_keys("standard_user")
element_of_first_password = driver.find_element(By.ID, "password")
element_of_first_password.send_keys("secret_sauce")
xpath_of_login_button = "//input[@id='login-button']"
element_of_login_first = driver.find_element(By.XPATH, xpath_of_login_button)
element_of_login_first.click()
sleep(5)

# Displaying cookies after login for Saucedemo
print("Cookies after login saucedemo:")
print(driver.get_cookies())
print(driver.current_url)
driver.get(url2)

# Displaying cookies before login for Zenclass
print("Cookies before login Zenportal:")
print(driver.get_cookies())
print(driver.current_url)
sleep(3)

# Entering credentials and logging in for Zenclass
element_of_username = driver.find_element(By.NAME, 'email')
element_of_username.send_keys('subashanmugam1998@gmail.com')
element_of_password = driver.find_element(By.NAME, 'password')
element_of_password.send_keys('Ranju@123')
Xpath_of_login_button = '//button[@type="submit"]'
element_of_login = driver.find_element(By.XPATH, Xpath_of_login_button)
element_of_login.click()

# Displaying cookies after login for Zenclass
print("Cookies after login Zenportal:")
print(driver.get_cookies())
print(driver.current_url)
sleep(5)

# Displaying cookies after login for Zenclass dashboard
driver.get(url3)
print("Cookies after login dashboard:")
print(driver.get_cookies())
print(driver.current_url)
sleep(3)

# Entering and logging out for Zenclass dashboard
Xpath_of_Dashboard_logout = ' //span[@data-toggle="dropdown"]'
element_dashboard_logout = driver.find_element(By.XPATH, Xpath_of_Dashboard_logout)
sleep(5)
element_dashboard_logout.click()
element_dashboard_logout_final = driver.find_element(By.XPATH, '/html/body/div[1]/nav/div/div/div/div/button[2]')
sleep(5)
element_dashboard_logout_final.click()
print("Cookies after full logout of Zenportal :")
print(driver.get_cookies())
sleep(3)