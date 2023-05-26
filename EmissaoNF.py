import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    UnexpectedAlertPresentException,
    NoSuchElementException)


options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    'download.default_directory': r'C:\Users\lucas\Downloads',
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
})

servico = Service(ChromeDriverManager().install())
drive = webdriver.Chrome(service=servico, options=options)
drive.maximize_window()
marktime = WebDriverWait(drive, 90)

arquivo = r'login.html'
caminho = os.path.realpath(arquivo)
drive.get(caminho)
pre_selecao = drive.find_element(By.TAG_NAME,'form')

lista_opcoes = pre_selecao.find_elements(By.TAG_NAME,'input')
login, senha = lista_opcoes

botao_login = pre_selecao.find_element(By.TAG_NAME, 'button')


login.send_keys('lucas@lourenco.com')
senha.send_keys('123456789')

botao_login.click()
def calculo():
    quantidade = drive.find_element(By.NAME, 'quantidade')
    quantidade = quantidade.get_attribute('value')
    
    valor_unitario = drive.find_element(By.NAME, 'valor_unitario')
    valor_unitario = valor_unitario.get_attribute('value')
    
    
    return quantidade, valor_unitario
xpath_aux = '//*[@id="formulario"]/h1'

marktime.until(
    EC.presence_of_element_located(
        (By.XPATH, xpath_aux)
    )
)

nome_xpath = '//*[@id="nome"]'
campo_nome = drive.find_element(By.XPATH, nome_xpath)
campo_nome.clear()
campo_nome.send_keys('Lucas Lourenco')
print(campo_nome.get_attribute('value'))



endereco_xpath = '/html/body/div/form/input[2]'
campo_endereco = drive.find_element(By.XPATH, endereco_xpath)
campo_endereco.clear()
campo_endereco.send_keys('Alguma Rua')
print(campo_endereco.get_attribute('value'))



bairro_xpath = '//*[@id="formulario"]/input[3]'
campo_bairro = drive.find_element(By.XPATH, bairro_xpath)
campo_bairro.clear()
campo_bairro.send_keys('Algum Lugar')
print(campo_bairro.get_attribute('value'))



campo_municipio = drive.find_element(By.NAME, 'municipio')
campo_municipio.clear()
campo_municipio.send_keys('Niterói')
print(campo_municipio.get_attribute('value'))



campo_cep = drive.find_element(By.NAME, 'cep')
campo_cep.clear()
campo_cep.send_keys('00000-000')
print(campo_cep.get_attribute('value'))



lista_suspensa_uf = drive.find_element(By.NAME, 'uf')
lista_suspensa_uf = Select(lista_suspensa_uf)
lista_suspensa_uf.select_by_visible_text('RJ')



campo_cnpj = drive.find_element(By.NAME, 'cnpj')
campo_cnpj.clear()
campo_cnpj.send_keys('12345678912345')
print(campo_cnpj.get_attribute('value'))



campo_inscricao = drive.find_element(By.NAME, 'inscricao')
campo_inscricao.clear()
campo_inscricao.send_keys('ABC123')
print(campo_inscricao.get_attribute('value'))



with open('descricao.txt', 'r') as f:
    texto_arquivo = f.read()

campo_descricao = drive.find_element(By.NAME, 'descricao')
campo_descricao.clear()
campo_descricao.send_keys(texto_arquivo)
print(campo_descricao.get_attribute('value'))



campo_quantidade = drive.find_element(By.NAME, 'quantidade')
campo_quantidade.clear()
campo_quantidade.send_keys(10)
print(campo_quantidade.get_attribute('value'))



campo_valor_unitario = drive.find_element(By.NAME, 'valor_unitario')
campo_valor_unitario.clear()
campo_valor_unitario.send_keys(15)
print(campo_valor_unitario.get_attribute('value'))


q_u = calculo()
valor = int(q_u[0]) * int(q_u[1])

campo_valor_total = drive.find_element(By.NAME, 'total')
campo_valor_total.clear()
campo_valor_total.send_keys(valor)
campo_valor_total.get_attribute('value')

drive.find_element(By.CLASS_NAME,'registerbtn').click()
