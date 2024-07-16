from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pyautogui

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M")
navegador.implicitly_wait(10)
navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys("Alex Santos")

navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys('alexalexandre1989@hotmail.com')

navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input').send_keys('31996852164')
navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/button').click

#img = pyautogui.locateCenterOnScreen(r'F:\Curso Python\HTML\midia\Selenium\capturar.png', confidence=0.7)
#pyautogui.click(img.x, img.y)


input()