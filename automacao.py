from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
import time

# automatizar romaneios e nro de carga com 
# notepad
romaneios = []
service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=service)
browser.get('https://gfl.sinclog.com.br/EntregasRelatorios/RelatorioGeralEntregas')


# login
browser.find_element('xpath', '//*[@id="login"]').send_keys('gustavo.varadi1')
browser.find_element('xpath', '//*[@id="senha"]').send_keys('Lokalti3601!!!')
browser.find_element('xpath', '//*[@id="formLogin"]/button').click()

# relatorio v2

# romaneio
# primeiro coloca os numeros de entrega e depois seleciona
time.sleep(4)
browser.find_element('xpath', 'form-control input-sm').click()
romaneio = browser.find_element('xpath', 'option[value=nro_lista]')
time.sleep(0.5)
select_romaneio = browser.find_element('xpath', 'tipoBusca')
select = Select(select_romaneio)
select.select_by_value('nro_lista')


