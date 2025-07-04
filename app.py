from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

VAGAS = []
navegador = webdriver.Chrome()

# INFOJOBS - url do site 
navegador.get("https://www.infojobs.com.br/empregos.aspx?poblacion=5208622")
navegador.maximize_window()

def cookies_infojobs(): 
    espera = WebDriverWait(navegador, 10)
    button_cookie = espera.until(EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button")))
    button_cookie.click()
    print("🍪 Cookies aceitos.")

cookies_infojobs()


def filtros_infojobs ():
    print("⌛ Aplicando filtros com Selenium...")
    button_area = navegador.find_element(By.XPATH, "//*[@id='facetCategory1']/div[1]/a")
    button_area.click()

    # XPath que busca a label contendo o texto
    button_TI = WebDriverWait(navegador, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(., 'Informática, TI, Telecomunicações')]"))
    )
    button_TI.click()

    apply_changes1 = navegador.find_element(By.XPATH, "//*[@id='facetCategory1']/div[2]/div[2]/div[2]/a" ) 
    apply_changes1.click()

    button_seniority = navegador.find_element(By.XPATH, "//*[@id='facetManagerialLevel']/div[1]/a")
    button_seniority.click()

    button_intern = navegador.find_element(By.XPATH, "//label[contains(., 'Estagiário')]" ) 
    button_intern.click()
    
    #input_trainee = navegador.find_element(By.ID, "ManagerialLevel-5")
    #navegador.execute_script("arguments[0].click();", input_trainee)

    apply_changes2 = navegador.find_element(By.XPATH, "//*[@id='facetManagerialLevel']/div[2]/div[2]/div[2]/a")
    apply_changes2.click()

filtros_infojobs()

# Coleta links das vagas
elementos = navegador.find_elements(By.XPATH, '//a[contains(@href, "/vaga-de-")]')
for el in elementos:
    href = el.get_attribute("href")
    if href and "infojobs.com.br/vaga-de" in href:
        VAGAS.append(href)
    print(f"🔗 {len(VAGAS)} links encontrados.")

def salvar_planilha(vagas):
    if not vagas:
        print("Nenhuma vaga foi encontrada para salvar.")
        return
    df = pd.DataFrame(vagas, columns=["Link"])
    df.drop_duplicates(subset="Link", inplace=True)
    df.to_excel("vagas.xlsx", index=False)
    print("Planilha salva com sucesso: vagas.xlsx")


time.sleep(10)
salvar_planilha(VAGAS)
navegador.quit

# Salva as planilhas em outra pasta 

# import os

# def salvar_planilha(vagas):
#     if not vagas:
#         print("Nenhuma vaga foi encontrada para salvar.")
#         return

#     df = pd.DataFrame(vagas, columns=["Link"])
#     df.drop_duplicates(subset="Link", inplace=True)

#     # Pega o caminho da area de Trabalho do usuario
#     desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    
#     # Define a pasta onde quer salvar
#     pasta = os.path.join(desktop, "Vagas")
    
#     # Cria a pasta se nao existir
#     if not os.path.exists(pasta):
#         os.makedirs(pasta)
    
#     # Define o caminho completo do arquivo Excel
#     caminho_arquivo = os.path.join(pasta, "vagas.xlsx")
    
#     df.to_excel(caminho_arquivo, index=False)
#     print(f"Planilha salva com sucesso: {caminho_arquivo}")
