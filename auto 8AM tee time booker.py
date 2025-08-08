# This script has not been updated to function on the updated site.  Site and other personal/login info removed for
# privacy and security

# imports
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# explicit wait imports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException


# Open site
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('##################################')


# login to the website
try:
    USERNAME = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'p_lt_PageContent_pageplaceholder_p_lt_zoneLeft_CHOLogin_LoginControl_ctl00_Login1_UserName')))

    PASSWORD = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'p_lt_PageContent_pageplaceholder_p_lt_zoneLeft_CHOLogin_LoginControl_ctl00_Login1_Password')))

    RETURN = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'p_lt_PageContent_pageplaceholder_p_lt_zoneLeft_CHOLogin_LoginControl_ctl00_Login1_LoginButton')))

    USERNAME.send_keys('#######')
    PASSWORD.send_keys('#######')
    RETURN.click()
except NoSuchElementException:
    driver.quit()


# gather the date boxes and select the date 2 weeks out
driver.maximize_window()
try:
    WebDriverWait(driver, 20).until(expected_conditions.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="module"]')))
    today = WebDriverWait(driver, 30).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'date')))
    # CHANGE THE DAY THAT THE DRIVER IS SELECTING
    WebDriverWait(driver, 8).until(expected_conditions.element_to_be_clickable(today[8])).click()
    time.sleep(4)
    today[13].click()
    time.sleep(4)
    today[14].click()

except NoSuchElementException or TimeoutException:
    driver.quit()


# initiate booking
try:
    dropdowns = WebDriverWait(driver, 15).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'dropdown-display')))
    dropdowns[1].click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="form1"]/div[3]/div[1]/div/div/div/div[3]/div/div[5]/div[3]/div/ul/li[2]'))).click()

    is_7 = False
    while is_7 is False:
        q = time.asctime()
        if '07:00:00' in q:
            is_7 = True

    driver.refresh()
    WebDriverWait(driver, 5).until(expected_conditions.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="module"]')))

    dropdowns = WebDriverWait(driver, 15).until(
        expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'dropdown-display')))
    dropdowns[1].click()
    book_time = WebDriverWait(driver, 10).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'time')))
    book_time[0].click()
except NoSuchElementException or TimeoutException:
    driver.quit()


# add other players, notes and book time
notes = ''
try:
    amb = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'ADD MEMBER')))
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(amb)).click()
    try:
        member_input = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located(
            (By.XPATH, '/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/div[1]/div/div[1]/div[2]/div/input')))
    except TimeoutException:
        amb.click()
        member_input = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
            (By.XPATH, '/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/div[1]/div/div[1]/div[2]/div/input')))
    member_input.send_keys('###########')
    time.sleep(1)
    member_input.send_keys('#########')
    time.sleep(1)
    member_input.send_keys('#########')
    time.sleep(1)
    member_located = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'roster-avatar')))
    # print(member_located)
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(member_located[0]))
    member_located[0].click()

    try:
        WebDriverWait(driver, 5).until(expected_conditions.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="module"]')))
        atbd = WebDriverWait(driver, 8).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, 'ADD To Be Determined')))
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(atbd)).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(atbd)).click()
        time.sleep(2)
    except TimeoutException or NoSuchElementException:
        member_located[0].click()
        atbd = WebDriverWait(driver, 8).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, 'ADD To Be Determined')))
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(atbd)).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(atbd)).click()
        time.sleep(2)
    try:
        atbd = WebDriverWait(driver, 8).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, 'ADD To Be Determined')))
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(atbd)).click()
    except:
        pass
    # add notes if assigned a value
    try:
        notes_text_area = WebDriverWait(driver, 2).until(
            expected_conditions.presence_of_element_located((By.ID, 'txtNotes')))
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(notes_text_area))
        if notes != '':
            notes_text_area.send_keys(notes)
    except TimeoutException or NoSuchElementException:
        member_located[0].click()
        notes_text_area = WebDriverWait(driver, 8).until(
            expected_conditions.presence_of_element_located((By.ID, 'txtNotes')))
        WebDriverWait(driver, 8).until(expected_conditions.element_to_be_clickable(notes_text_area))
        if notes != '':
            notes_text_area.send_keys(notes)
    # press book now
    book_now_button = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.LINK_TEXT, 'BOOK NOW')))
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(book_now_button))
    print('done')
    try:
        book_now_button.click()
    except ElementClickInterceptedException:
        time.sleep(1.5)
        book_now_button.click()
except NoSuchElementException or TimeoutException:
    driver.quit()


time.sleep(20)

