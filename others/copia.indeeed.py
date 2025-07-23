from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from datetime import datetime
import pandas as pd
import pyautogui
import time
import os






# TEM O INFO JOBS E O INDEED, VERIFICAR ANTES CASO PRECISE DO INDEED 









































VAGAS = []

navegador = webdriver.Chrome()

def inciar_navegador(normal = true):
    if normal
        return webdriver.Chrome
    else:
        options = uc.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-blink-features=AutomationControlled")
        return uc.Chrome(options=options)

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
time.sleep(10)

# Inicializa o navegador "disfarçado", por conta de cloudflare
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features=AutomationControlled")
navegador_flare = uc.Chrome(options=options)

navegador_flare.get("https://br.indeed.com/jobs?q=&l=Rio+de+Janeiro%2C+RJ&from=searchOnHP&vjk=c90816dc02590f14")
navegador_flare.maximize_window()
time.sleep(9)

cookie_indeed = navegador_flare.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']")
cookie_indeed.click()

#area
pyautogui.click(x=877, y=281)
time.sleep(1)
#estagio 
pyautogui.click(x=815, y=479)
time.sleep(1)
#filtrar
pyautogui.click(x=1119, y=777)
time.sleep(3)
# setor
pyautogui.click(x=1477, y=285)
time.sleep(2)

# Caso queira filtrar vaga por TI
# #ti indeed
# pyautogui.click(x=704, y=669)
# time.sleep(1)
# # aplicar filtro
# pyautogui.click(x=1199, y=807)
# time.sleep(3)

DETALHES = []

for link in VAGAS:
    navegador_flare.get(link)
    time.sleep(3)  # tempo para carregar a página da vaga

    try:
        titulo = navegador_flare.find_element(By.TAG_NAME, 'h1').text
    except:
        titulo = ""

    try:
        empresa = navegador_flare.find_element(By.CLASS_NAME, 'jobsearch-InlineCompanyRating').text
    except:
        empresa = ""

    try:
        salario = navegador_flare.find_element(By.XPATH, '//span[@class="salary-snippet"]').text
    except:
        salario = ""

    try:
        descricao = navegador_flare.find_element(By.ID, 'jobDescriptionText').text[:300]  # limitar para evitar textos gigantes
    except:
        descricao = ""

    # tenta detectar se é estágio (por palavra-chave)
    estagio = "estágio" in descricao.lower() or "estágio" in titulo.lower()
    trainee = "trainee" in descricao.lower() or "trainee" in titulo.lower()

    DETALHES.append({
        "Link": link,
        "Título": titulo,
        "Empresa": empresa,
        "Salário": salario,
        "Descrição": descricao,
        "É Estágio?": "Sim" if estagio else "Não",
        "É Trainee?": "Sim" if trainee else "Não"
    })

print(f"✅ {len(DETALHES)} vagas com detalhes coletados.")

# salva com mais colunas no Excel
def salvar_planilha_detalhada(lista):
    if not lista:
        print("Nada para salvar.")
        return
    df = pd.DataFrame(lista)
    df.drop_duplicates(subset="Link", inplace=True)

    # Obtemos a data de hoje no formato YYYY-MM-DD
    data_hoje = datetime.today().strftime('%Y-%m-%d')

    # Montamos o caminho da pasta principal e da subpasta
    pasta_principal = data_hoje
    subpasta = os.path.join(pasta_principal, "planilhas")

    os.makedirs(subpasta, exist_ok=True)  # Cria as pastas automaticamente, se não existirem

    caminho_arquivo = os.path.join(subpasta, "vagas_com_detalhes.xlsx")
    df.to_excel(caminho_arquivo, index=False)
    print(f"📁 Planilha detalhada salva em: {caminho_arquivo}")

salvar_planilha_detalhada(DETALHES)

#teste 2 
# import pandas as pd
# from openpyxl import load_workbook

# # Coleta os links
# VAGAS = []
# for el in blocos:
#     jk = el.get_attribute("data-jk")
#     if jk:
#         link = f"{base_url}{jk}"
#         if link not in VAGAS:
#             VAGAS.append(link)

# print(f"🔗 {len(VAGAS)} links encontrados.")

# # Salva em Excel sem sobrescrever
# def salvar_planilha(vagas):
#     if not vagas:
#         print("Nenhuma vaga foi encontrada para salvar.")
#         return

#     novo_df = pd.DataFrame(vagas, columns=["Link"])
#     novo_df.drop_duplicates(subset="Link", inplace=True)
#     caminho_arquivo = "vagas.xlsx"

#     try:
#         # Lê o conteúdo existente
#         df_existente = pd.read_excel(caminho_arquivo)
#         # Concatena e remove duplicados
#         df_final = pd.concat([df_existente, novo_df]).drop_duplicates(subset="Link")
#     except FileNotFoundError:
#         # Se o arquivo não existe ainda
#         df_final = novo_df

#     # Salva o resultado
#     df_final.to_excel(caminho_arquivo, index=False)
#     print("Planilha salva com sucesso: vagas.xlsx")

# # Chama a função
# salvar_planilha(VAGAS)
