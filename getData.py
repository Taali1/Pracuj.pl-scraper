import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd

def closePops(driver):
    # Zamyka popup
    driver.find_element(By.CLASS_NAME, "ptv5q7l").click()
    print("Popup closed")
    # Akceptuje ciasteczka
    cookies = driver.find_element(By.CLASS_NAME, "cmulq7z")
    btn_cookies = cookies.find_element(By.TAG_NAME, "button")
    # Jeżeli nie ma ciasteczek, akceptuje
    if btn_cookies:
        btn_cookies.click()
    print("Cookies accepted")
    time.sleep(3)
    # Zamyka regulamin
    driver.find_element(By.CLASS_NAME, "pwehynj").find_element(By.CLASS_NAME, "bzd9ar4").click()

# Pobiera dane (obecnie jedynie tytuły) z boxów ofert pracy
def get_offerts(source):
    doc = BeautifulSoup(source, "html.parser")
    # Pobiera wszystkie boxy ofert
    offer_list = doc.find("div", {"class": "csipjg8"}).find_all("div", {"class": "ceqyuft"})
    return offer_list

def get_title(offer_list):
    title = []
    # Pobiera wszystkie tytuły ofert
    for element in offer_list:
        title.append(element.find("h2").text)
    return title

def get_level(offer_list):
    level = []
    # Pobiera wszystkie pozimy stanowisk ofert pracy
    for element in offer_list:
        level.append(element.find("li", {"class": "iq8b4w2"}).text)
    return level

def get_pay(offer_list):
    # Pobiera wszystkie płace ofert pracy
    pass

def get_requiments(offer_list):
    # Pobiera wszystkie wymagania na stanowisko
    pass

def get_company(offer_list):
    company = []
    # Pobiera nazwy firm
    for element in offer_list:
        company.append(element.find("h4").text)
    return company



# Przwija storny oraz pobiera dane z pomocą funkcji get_offerts
def get_data(driver, iterations, final_data, title=False, level=False, pay=False, requiments=False, company=False):
    loop = 0
    while True:
        loop += 1

        print(f"\nLoop number {loop} has started. Computing...")

        # Pobiera obecne źródło strony
        offers = get_offerts(driver.page_source)

        # Pobiera wybrane dane
        if title:
            final_data['title'] = get_title(offers)
            print("Titles picked")
        if level:
            final_data['level'] = get_level(offers)
            print("Levels picked")
        if pay:
            final_data['pay'] = get_pay(offers)
            print("Pays picked")
        if requiments:
            final_data['requiments'] = get_requiments(offers)
            print("Requiments picked")
        if company:
            final_data['company'] = get_company(offers)
            print("Company names picked")    

        # Szuka przycisku następnej strony
        pagination = driver.find_element(By.CLASS_NAME, "w1h4nogz")
        next_page_button = pagination.find_elements(By.TAG_NAME, "button")

        print(f"Loop number {loop} has ended")

        # Naciska przycisk zmiany stony, jeżeli istnieje, inaczej zatrzymuje pętle
        if next_page_button[-1].text == "Następna":
            next_page_button[-1].click()
        else:
            return final_data

        time.sleep(3)
        if loop == iterations:
            return final_data
        
def convert_to_csv(data, file_name): 
    df = pd.DataFrame(data)   
    df.to_csv(file_name)
    return file_name