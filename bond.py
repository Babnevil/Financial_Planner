from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get('https://www.treasurydirect.gov/BC/SBCPrice')
series = Select(driver.find_element_by_name('Series'))
denom = Select(driver.find_element_by_name('Denomination'))
serial = driver.find_element_by_name('SerialNumber')
issue = driver.find_element_by_name('IssueDate')
send = driver.find_element_by_name('btnAdd.x')

#elements = driver.find_element_by_name("Series")
#all_options = elements.find_element_by_tag_name("option")

#ToDo, create method that accepts 0-3 as args.
series.select_by_index(1)

#ToDo, create method that accepts 0-9 as args.
denom.select_by_index(7)

#ToDo, replace hardcoded string values with variable passed through arg
serial.send_keys("1121212")

issue.send_keys("11/2000")

send.click()

#ToDo, slice and format the results
results = driver.find_element_by_id("ta1")
print(results.text)
values = results.text
values = values.split()

print("Your bond is currently worth: ", values[9])
print("It has accumliated: ", values[11], " in interest this year, and ",
      values[10], " in interest over the life of the bond.")
