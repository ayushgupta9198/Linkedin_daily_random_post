from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from datetime  import datetime
import parameters, os.path , random 


while True:
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.linkedin.com/login')
    driver.find_element('id', 'username').send_keys(parameters.linkedin_username)
    driver.find_element('id', 'password').send_keys(parameters.linkedin_password)
    driver.find_element('xpath', '//*[@type="submit"]').click()
    # import pdb;pdb.set_trace()
    box_post = driver.find_element_by_xpath('//*[@id="ember25"]/span')
    box_post.click()

    time.sleep(2)
    post_input = driver.find_elements(By.CSS_SELECTOR,"div[data-placeholder='What do you want to talk about?'] p")
    import csv
    with open('example.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        # read the first line
        line = next(reader)
        # save the line in a variable
        saved_line = line
        print(saved_line)
        # delete the line from the csv file
        with open('/home/dell/Downloads/example.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            for row in reader:
                writer.writerow(row)

    if post_input:post_input[0].send_keys(f'{saved_line[0]}')
    time.sleep(2)
    post = driver.find_element(By.XPATH,"//span[normalize-space()='Post']").click()
    time.sleep(5)
    today = datetime.now()
    date_time = today.strftime("%M/%D/%Y,%H:%M:%S")
    print("process done", date_time)
    driver.quit()
    time.sleep(random.randint(3000,5000))
