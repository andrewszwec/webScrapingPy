###########################################################
## New Approach
###########################################################


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *
import wget

url = "http://www.bom.gov.au/jsp/ncc/cdio/weatherData/av?p_nccObsCode=136&p_display_type=dailyDataFile&p_startYear=&p_c=&p_stn_num="
station_ids = ["66000", "66002", "66003", "66010"] 

myProxy = "http://aszwec:Deloitte1!@proxy.au.deloitte.com:80"
proxy = Proxy({'proxyType': ProxyType.AUTODETECT})	


# open text file to write urls
f=open('C:/Users/aszwec/Documents/python/webScarpper/download_urls.txt','a')




# open each download page and dowload the file
for id in station_ids:
	# open firefox
	driver = webdriver.Firefox(proxy=proxy)
	# browse to page
	driver.get(url + id)
	assert "Daily Rainfall" in driver.title
	link = driver.find_element_by_link_text("All years of data")
	# Click on download link
	#link.send_keys(Keys.RETURN)
	href = link.get_attribute('href')
	
	# Save href to a textfile for download later
	f.write(href)
	f.write("\r\n")

	# download file
	#filename = wget.download(href)		
	driver.close()
	
	
f.close()
print("...................")
print("...................")
print("Closing Program....")
print("...................")
print("...................")
	