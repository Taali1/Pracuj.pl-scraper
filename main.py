from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from getData import *


def main_download(link: str, title: bool = False, level: bool = False, pay: bool = False, requirements: bool = False, company: bool = False, path: str = "/data/"):
    my_data = {}

    # Tworzenie drivera
    def get_driver(link):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(link)
        driver.set_window_size(1440, 900)
        return driver

    # Włącza przeglądarkę oraz pobiera jej dane
    driver = get_driver(link)

    # Zamyka alerty i pytania o ciasteczka
    close_pops(driver)

    # Przewija strony i pobiera dane. Potrzeba podać przeglądarkę oraz tabelę gdzie będą wpisywane dane
    get_data(driver, 2, my_data, title, level, pay, requirements, company)

    # Zamykanie drivera
    driver.close()

    # Z zebranych danych tworzy skoroszyt danych
    print("\nConverting to .csv...")
    file_name, directory = convert_to_csv(my_data, path)
    print(f"Converting finished\nFile name: {file_name}")
    print(f"File's location {directory}")