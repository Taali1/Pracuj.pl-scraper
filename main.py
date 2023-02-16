from selenium import webdriver
from selenium.webdriver.common.by import By

def myApp():
    driver = webdriver.Chrome()
    driver.get("https://www.pracuj.pl")


    # Zamyka popup
    driver.find_element(By.CLASS_NAME, "ptv5q7l").click()
    print("Popup closed")
    # Akceptuje ciasteczka
    cookies = driver.find_element(By.CLASS_NAME, "cmulq7z")
    btn_cookies = cookies.find_element(By.TAG_NAME, "button")
    if btn_cookies:
        btn_cookies.click()
    print("Cookies accepted")

    # Znajduje div z inputami
    search_div = driver.find_element(By.CLASS_NAME, "b1lrqsa6")
    search_div.find_element(By.CLASS_NAME, "b1vlkyp2")
    print("Inputs founded")

    # Znajduje input kategorii
    inputs = search_div.find_elements(By.CLASS_NAME, "io2rxbl")
    inputs[1].click()
    print("Categories clicked")

    # Znajduje listę kategorii
    category = inputs[1].find_element(By.CLASS_NAME, "ckx1t3o")
    print("Category list found") if category else print("Couldn't find a category list")

    # Wybiera kategorie: IT - Rozwój oprogramowania
    left_category_list = category.find_elements(By.TAG_NAME, "div")[0]
    print(left_category_list.find_elements(By.TAG_NAME, "ceww55h"))
    print("Category checked")

    # Chowa listę kategorii
    search_div.find_element(By.CLASS_NAME, "b1vlkyp2")
    print("Category list hidden")

    # Znajduje div z przyciskami
    button_div = driver.find_element(By.CLASS_NAME, "s1f6riqa")

    # Klika przycisk Szukaj
    button_div.find_element(By.CLASS_NAME, "bzd9ar4").click()
    print("Searching...")


if __name__ == '__main__':
    myApp()