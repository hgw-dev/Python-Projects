from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementNotVisibleException,\
    StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import chrome

#Start the clock
start_time = time.time()

#Declare all billing information
billing_name = 'Jack Jackson'
billing_email = 'jackson@jack.net'
billing_tel = 555555555
billing_address = '123'
billing_zip = '92660'
billing_city = 'Newport Beach'
billing_state = 'CA'
billing_country = 'USA'
card_number = 789456123789
card_cvv = '111'
card_exp_date_month = '12'
card_exp_date_year = '222'

#URLs for testing
#url = 'http://www.supremenewyork.com/shop/hats/o7spcadf8/'
#url = 'http://www.supremenewyork.com/shop/sweatshirts/q8xmrsd52'

#All information dealing with the item you want 
item_category = 'shirts'
item_name = 'Corduroy Shirt'
#All information dealing with style preferences for the item you want
priority_colors = ['red', 'purple', 'black']
priority_sizes = ['Large', 'Medium', 'Small']

#Start PhantomJS
#chrome_path = r"C:\PhantomJS\bin\phantomjs.exe"
chrome_path = r"C:\Users\Hunter\Desktop\chromedriver_win32\chromedriver.exe"
#chrome_path = r"C:\PhantomJS\bin\phantomjs.exe"
driver = webdriver.Chrome(chrome_path)

#Base str for everything Supreme related
supstr = 'http:www.supremenewyork.com/shop/'
driver.get(supstr + 'all/' + item_category)

a = driver.find_elements_by_class_name('name-link')
links = []
for x in a:
    #Find all new items
    #if x.get_attribute('text') == 'new':
    #Break up URL
    if x.text == item_name:
        driver.get(x.get_attribute('href'))
        break

#Find all 'color' items
a = driver.find_elements_by_css_selector('a')
available_colors = {}

for values in a:
    color = values.get_attribute('data-style-name')
    #Eliminate instances of 'None' so it is a list of colors
    if color != None:
        #Only unique entries
        if color not in available_colors:
            #Put the color name as a key and the WebDriverObject as the value
            available_colors[color.lower()] = values

#Go through all the priority colors given in order of preference
selected_item = ''
for color in priority_colors:
    #As soon as the earliest object in priority_colors matches an item in available_colors ...
    if color in available_colors:
        #... make that object the selected item
        selected_item = available_colors[color]
        break

#Click on the chosen color
if selected_item == '':
    selected_item = list(available_colors.values())[0]
selected_item.click()

#Find all drop-downs labeled size
try:
    selection = Select(driver.find_element_by_xpath('//*[@id="size"]'))
    options = selection.options
    for x in range(len(options)):
        options[x] = options[x].text
    
    #If the desired size is in options, select it
    for size in priority_sizes:
        if size in options:
            selection.select_by_visible_text(size)
            break
    #Otherwise, select the last item in the list
    else:
        selection.select_by_visible_text(options[-1])
except NoSuchElementException:
    pass

#Try to click the 'Add to Cart' button, if not take a screenshot of the page
try:
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/fieldset[2]/input').click()
except NoSuchElementException:
    driver.save_screenshot('C:Users/Hunter/Desktop/test0.png')

#Try to click the 'Checkout' button, if not take a screenshot of the page
try:
    driver.find_element_by_link_text('checkout now').click()
except NoSuchElementException:
    driver.get('www.supremenewyork.com/checkout')

name = driver.find_element_by_id('order_billing_name')
email = driver.find_element_by_id('order_email')
tel = driver.find_element_by_id('order_tel')
address = driver.find_element_by_id('bo')
zip = driver.find_element_by_id('order_billing_zip')
city = driver.find_element_by_id('order_billing_city')
state = driver.find_element_by_id('order_billing_state')
country = driver.find_element_by_id('order_billing_country')
number = driver.find_element_by_id('cnb')
exp_month = driver.find_element_by_id('credit_card_month')
exp_year = driver.find_element_by_id('credit_card_year')
cvv = driver.find_element_by_id('vval')
terms = driver.find_element_by_id('order_terms')

name.send_keys(billing_name)
email.send_keys(billing_email)
tel.send_keys(str(billing_tel))
address.send_keys(billing_address)
zip.send_keys(billing_zip)
city.send_keys(billing_city)
Select(state).select_by_visible_text(billing_state)
Select(country).select_by_visible_text(billing_country)
number.send_keys(str(1))
number.send_keys(str(2))
exp_month.send_keys(card_exp_date_month)
exp_year.send_keys(card_exp_date_year)
cvv.send_keys(card_cvv)
terms.click()

driver.save_screenshot('test.png')

#Print the final time
print('---%s seconds ---' % (time.time() - start_time))






















