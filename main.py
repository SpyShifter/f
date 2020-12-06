from keep_alive import keep_alive
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://test.luchezarkotsev.repl.co")
keep_alive()

while True:
  time.sleep(120)
  driver.refresh()