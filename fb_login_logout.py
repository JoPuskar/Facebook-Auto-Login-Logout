from selenium import webdriver
import time
#launch browser
browser = webdriver.Chrome()
#goto facebook.com
browser.get('https://www.facebook.com/login/')

email = browser.find_element_by_xpath('//*[@id="email"]')
email.send_keys("Your email")

pas = browser.find_element_by_xpath('//*[@id="pass"]')
pas.send_keys("Your Password")

pas.submit()
#sleep for 15 Secs minute
time.sleep(300)

logout1 = browser.find_element_by_xpath('//*[@id="userNavigationLabel"]')
logout1.click()

time.sleep(10)

e = browser.find_element_by_xpath("//a[contains(@data-gt,'menu_logout')]")

e.click()

time.sleep(5)

browser.quit()
#browser.quit()
#logout after 1 minute
#logout = browser.find_element_by_css_selector("._w0d[action='https://www.facebook.com/logout.php?button_name=logout&button_location=settings']").submit()

