# This script has not been updated to function on the updated site.  Some site and other personal/login info removed for
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

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('###################################################')


def actually_book_time(note, include_member):
    if include_member == 'Y' or 'y':
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="form1"]/div[3]/div[1]/div/div/div/div[3]/div/div[4]/div[2]/div/div[1]/span[2]/span/span/div/div[1]/div[1]/a'))).click()
        member_input = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'col-sm-4 link')))
        members_located = []
        while len(members_located) != 2:
            for letter in 'member #############':
                member_input.send_keys(letter)
                members_located = WebDriverWait(driver, 5).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'thumbnail')))
                time.sleep(0.2)
                if len(members_located) == 2:
                    members_located[1].click()

    notes_text_area = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, 'txtNotes')))
    # WebDriverWait(driver, 10).until(expected_conditions.frame_to_be_available_and_switch_to_it((By.ID, 'module')))
    book_now_button = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'btn btn-primary ng-binding')))

    notes_text_area.send_keys(note)
    book_now_button.click()


try:
    # First login to the website
    USERNAME = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'p_lt_PageContent_pageplaceholder_p_lt_zoneLeft_CHOLogin_LoginControl_ctl00_Login1_UserName')))

    PASSWORD = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'p_lt_PageContent_pageplaceholder_p_lt_zoneLeft_CHOLogin_LoginControl_ctl00_Login1_Password')))

    RETURN = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'p_lt_PageContent_pageplaceholder_p_lt_zoneLeft_CHOLogin_LoginControl_ctl00_Login1_LoginButton')))

    USERNAME.send_keys('##################')
    PASSWORD.send_keys('##################')
    RETURN.click()
except NoSuchElementException:
    driver.quit()


try:
    # obtain date and course/range statuses
    date_and_course_status = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/div/div/div[2]/p[3]/span/span[1]/strong[1]/span'))).text
    cart_restrictions_status = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/div/div/div[2]/p[3]/span/span[1]/span'))).text
    driving_range_status = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/div/div/div[2]/p[3]/span/span[2]'))).text

    print(date_and_course_status, '\n', cart_restrictions_status, '\n', driving_range_status)
except NoSuchElementException or TimeoutException:
    driver.quit()


book_time = input('Do you want to book a tee time? Y or N?')
if book_time == 'Y' or 'y':
    driver.get('####################################')
    driver.maximize_window()
    try:
        WebDriverWait(driver, 20).until(expected_conditions.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="module"]')))
        today = WebDriverWait(driver, 30).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'date')))
        # CHANGE THE DAY THAT THE DRIVER IS SELECTING
        today[0].click()
        # time.sleep(3)
        # today[12].click()

    except NoSuchElementException or TimeoutException:
        driver.quit()
elif book_time == 'N' or 'n':
    driver.quit()
else:
    print('invalid input')
    driver.quit()

times_list = []
available_list = []
try:
    dropdowns = WebDriverWait(driver, 15).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'dropdown-display')))
    dropdowns[1].click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="form1"]/div[3]/div[1]/div/div/div/div[3]/div/div[5]/div[3]/div/ul/li[2]'))).click()
    times = WebDriverWait(driver, 20).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'time')))
    available = WebDriverWait(driver, 20).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'value')))

    for count in available:
        available_list.append(count.text)
    for number in times:
        times_list.append(number.text[5:])
    print()
    i = 0
    for string in times_list:
        print(times_list[i], '- Available:', available_list[i])
        i += 1
    book_input = input("Enter the time you would like to book (matching the way it was displayed above) or 'n' to cancel without booking a time: ")
    if book_input in times_list:
        time_index = times_list.index(book_input)
        add_member = input("Add member ######### to tee time?  Enter a 'y' or 'n' to indicate choice: ")
        notes = input('Notes added to booking (Enter to skip): ')
        times[time_index].click()
        try:
            times[time_index].click()
        except:
            pass

        if add_member == 'y':
            amb = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,'ADD MEMBER')))
            WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(amb)).click()
            try:
                member_input = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/div[1]/div/div[1]/div[2]/div/input')))
            except TimeoutException:
                amb.click()
                member_input = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/div[1]/div/div[1]/div[2]/div/input')))
            member_input.send_keys('member #')
            time.sleep(1)
            member_input.send_keys('#####')
            time.sleep(1)
            member_input.send_keys('###')
            time.sleep(1)
            members_located = WebDriverWait(driver, 10).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'roster-avatar')))
            # print(members_located)
            WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(members_located[0]))
            members_located[0].click()

        try:
            notes_text_area = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.ID, 'txtNotes')))
            WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(notes_text_area))
            notes_text_area.send_keys(notes)
        except TimeoutException or NoSuchElementException:
            members_located[0].click()
            notes_text_area = WebDriverWait(driver, 8).until(expected_conditions.presence_of_element_located((By.ID, 'txtNotes')))
            WebDriverWait(driver, 8).until(expected_conditions.element_to_be_clickable(notes_text_area))
            notes_text_area.send_keys(notes)

        # WebDriverWait(driver, 5).until(expected_conditions.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe.module')))
        # book_now_button = WebDriverWait(driver, 12).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[text()='BOOK NOW']")))
        book_now_button = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'BOOK NOW')))
        # print(book_now_button)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(book_now_button))
        try:
            book_now_button.click()
        except ElementClickInterceptedException:
            time.sleep(2)
            book_now_button.click()
        print('booked')
except NoSuchElementException or TimeoutException or ElementClickInterceptedException:
    driver.quit()

# confirm the booking was made by displaying the confirmation information back
try:
    confirmation_txt = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'banner-title')))
    date_txt = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="form1"]/div[3]/div[1]/div/div/div/div[3]/div/div[2]/div/div[1]/div[1]/p/span[1]')))
    time_txt = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="form1"]/div[3]/div[1]/div/div/div/div[3]/div/div[2]/div/div[1]/div[1]/p/span[2]')))
    print(confirmation_txt.text, date_txt.text, time_txt.text)
except NoSuchElementException or TimeoutException:
    pass


close = input("Exit program? 'y' or 'n'?")
if close == 'y' or 'Y':
    driver.quit()

