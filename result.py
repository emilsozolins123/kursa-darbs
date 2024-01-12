import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument("--headless")   # headless strādā viss fonā, tā, ka neko uz ekrāna nerāda

driver = webdriver.Chrome(options=chrome_options) # saprot, kas ir jādara ar chrome, šajā gadījumā tiek norādīts, ka ir jābut headless mode

saraksts = []
sajutuSaraksts = [] # tiek izveidoti divi saraksti

print("Uzgaidiet 10 sekundes ;)")
url = "https://www.weather-atlas.com/en/latvia/riga"        # tiek piešķirta vērtība, jeb url šajā gadījumā
driver.get(url)     # tiek pateikts, ka šis ir jāatver
time.sleep(2)       # liek programmai pagaidīt 2 sekundes, pirms kaut ko tālāk darīt
find = driver.find_element(By.CLASS_NAME, "fs-2")           # mājaslapā tiek meklēta vērtība pēc norādītas klases
gradi = float(re.sub(r'[^0-9, -]', '', find.text))          # no nolasītas vērtības tiek noņemts viss izņemot skaitļi un simbols ( - )
saraksts.append(gradi)      # apstrādātā vērtība tiek pievienota sarakstam
atrast = driver.find_element(By.CLASS_NAME, "fs-5")         # tieši tas pats, kas 19. līnijā
felling = float(re.sub(r'[^0-9, -]', '', atrast.text))      # no nolasītas vērtības tiek noņemts viss izņemot skaitļi un simbols ( - )
sajutuSaraksts.append(felling)      # apstrādātā vērtība tiek pievienota sarakstam

# viss tiek atkārtots ar pārējām mājaslapām pēc tā pašā principa
url = "https://en.ilmatieteenlaitos.fi/weather/latvia/riga"
driver.get(url)
time.sleep(2)
find = driver.find_element(By.CLASS_NAME, "temperature-plus")
gradi = float(re.sub(r'[^0-9, -]', '', find.text))
saraksts.append(gradi)
atrast = driver.find_element(By.CLASS_NAME, "feelslike-value")
felling = float(re.sub(r'[^0-9, -]', '', atrast.text))
sajutuSaraksts.append(felling)

url = "https://weather.com/lv-LV/laiks/pastundam/l/R%C4%ABga?canonicalCityId=73f107eb4765da45058355aa33538590bdc5ad5eda6648a8ef2912e861ee3f5e"
driver.get(url)
time.sleep(2)
find = driver.find_element(By.CLASS_NAME, "DetailsSummary--tempValue--jEiXE")
gradi = float(re.sub(r'[^0-9, -]', '', find.text))
saraksts.append(gradi)
atrast = driver.find_element(By.CLASS_NAME, "DetailsTable--value--2YD0-")
felling = float(re.sub(r'[^0-9, -]', '', atrast.text))
sajutuSaraksts.append(felling)

url = "https://www.delfi.lv/laika-zinas/lokacija/ChIJ7T0H5bDP7kYRMP7yaM3PAAQ"
driver.get(url)
time.sleep(2)
find = driver.find_element(By.CLASS_NAME, "main-widget__temperature")
gradi = float(re.sub(r'[^0-9, -]', '', find.text))
saraksts.append(gradi)
atrast = driver.find_element(By.CLASS_NAME, "main-widget__feels-like")
felling = float(re.sub(r'[^0-9, -]', '', atrast.text))
sajutuSaraksts.append(felling)

url = "https://www.meteoprog.com/lv/weather/Riga/"
driver.get(url)
time.sleep(2)
find = driver.find_element(By.CLASS_NAME, "today-temperature")
atrast = driver.find_element(By.CLASS_NAME, "feels-like")
gradi = float(re.sub(r'[^0-9, -]', '', find.text))
felling = float(re.sub(r'[^0-9, -]', '', atrast.text))
saraksts.append(gradi)
sajutuSaraksts.append(felling)

print("Aplūkojot piecas dažādas laikapstākļu prognozes var secināt, ka:")

temperatura = sum(saraksts) / len(saraksts)         # iegūstām saraksta summu, iegūstam saraksta elementu skaitu, izrēķinam vidējo aritmētisko
print("Tagadēja temperatūra: " + str(temperatura) + " grādi")       # izprintējam, pārveidojam skaitli par string vispirms

temperaturaPecSajutam = sum(sajutuSaraksts) / len(sajutuSaraksts)           # iegūstām saraksta summu, iegūstam saraksta elementu skaitu, izrēķinam vidējo aritmētisko
print("Pēc sajūtām ārā ir: " + str(temperaturaPecSajutam) + " grādi")       # izprintējam, pārveidojam skaitli par string vispirms

driver.quit()       # aizver visas mājaslapas un beidz visas chrome darbības