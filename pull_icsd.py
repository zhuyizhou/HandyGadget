from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

coll = 183684

driver = webdriver.Chrome()  

driver.get('https://icsd.fiz-karlsruhe.de/search/basic.xhtml');
search_box = driver.find_element_by_name('content_form:uiCodeCollection:input:input')
search_box.clear()
search_box.send_keys(str(i))
search_box.send_keys(Keys.RETURN)
try:
    button = driver.find_element_by_id("display_form:listViewTable:0:btnEntryDownloadCif")
    button.click()
except NoSuchElementException:
    pass
driver.quit()
