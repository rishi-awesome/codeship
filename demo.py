from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome()
driver.get("https://www.google.co.in/flights/#search;f=RPR;t=BOM;d=2015-12-21;r=2015-12-29;tt=o;sel=RPRBOM09W378")
if not "Flights to Mumbai - Google Flights" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_css_selector("div.tooltipUseHtml div")
fare = elem.text()
print fare
driver.quit()
