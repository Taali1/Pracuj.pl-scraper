from selenium import webdriver
from getData import *

myData = {}
link = input("Please insert link for page from which data will be dowloaded: ")

# Tworzenie drivera
def get_driver(link):
    driver = webdriver.Chrome()
    driver.get(link)
    return driver

# Tworzenie tablicy opcji pobrania
data_options = {
    "title": False,
    "level": False,
    "pay": False,
    "requiments": False,
    "company": False,
}

# Włącza przeglądarkę oraz pobiera jej dane
driver = get_driver(link)

# Zamyka alerty i pytania o ciasteczka
closePops(driver)

# Przewija strony i pobiera dane. Potrzeba podać przeglądarkę oraz tabelę gdzie będą wpisywane dane
get_data(driver, 2, myData, data_options["title"], data_options["level"], data_options["pay"], data_options["requiments"], data_options["ccompany"])

# Zamykanie drivera
driver.close()

# Z zebranych danych tworzy skoroszyt danych
print("\nConverting to .csv...")
csv_file = convert_to_csv(myData, 'worl.csv')
print(f"Converting finished\nFile name: {csv_file}")