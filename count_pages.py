from bs4 import BeautifulSoup

def pages_count(source) -> int:
    doc = BeautifulSoup(source, "html.parser")
    # Znajduje pierwszy div z liczbą stron
    pages_div = doc.find("div", {"class": "w1jm3gvb"})
    # Znajduje kolejny div z liczbą stron
    pages_div = pages_div.find("div", {"class": "text-wrapper wws23ky"})
    # Zanajduje spany w div'ie wraz z liczbą stron
    pages_num = pages_div.find_all("span")
    return pages_num[-1].text

def offers_count(source) -> str:
    doc = BeautifulSoup(source, "html.parser")
    # Jest tylko jeden span z taką klasą, zawiera on liczbę znalezionych ofert
    offers_num = doc.find("span", {"class": "j1lr4pyy"}).text
    return offers_num
