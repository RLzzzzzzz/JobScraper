from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import pandas as pd
import pyautogui
import time


VAGAS = []

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
time.sleep(1)



# Coleta links das vagas  - fazer if e else aq (provavelmente um def tb)
# Coletar links das vagas do Indeed
# Coleta os elementos com data-jk
blocos = navegador_flare.find_elements(By.XPATH, '//a[@data-jk]')

base_url = "https://br.indeed.com/viewjob?jk="
# coleta os links
for el in blocos:
    jk = el.get_attribute("data-jk")
    if jk:
        link = f"{base_url}{jk}"
        if link not in VAGAS:
            VAGAS.append(link)

print(f"🔗 {len(VAGAS)} links encontrados.")

# Salva em Excel sem sobrescrever
def salvar_planilha(vagas):
    if not vagas:
        print("Nenhuma vaga foi encontrada para salvar.")
        return

    novo_df = pd.DataFrame(vagas, columns=["Link"])
    novo_df.drop_duplicates(subset="Link", inplace=True)
    caminho_arquivo = "vagas.xlsx"

    try:
        # Lê o conteúdo existente
        df_existente = pd.read_excel(caminho_arquivo)
        # Concatena e remove duplicados
        df_final = pd.concat([df_existente, novo_df]).drop_duplicates(subset="Link")
    except FileNotFoundError:
        # Se o arquivo não existe ainda
        df_final = novo_df

    # Salva o resultado
    df_final.to_excel(caminho_arquivo, index=False)
    print("Planilha salva com sucesso: vagas.xlsx")

# Chama a função
salvar_planilha(VAGAS)

#teste

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

    DETALHES.append({
        "Link": link,
        "Título": titulo,
        "Empresa": empresa,
        "Salário": salario,
        "Descrição": descricao,
        "É Estágio?": "Sim" if estagio else "Não"
    })

print(f"✅ {len(DETALHES)} vagas com detalhes coletados.")

# salva com mais colunas no Excel
def salvar_planilha_detalhada(lista):
    if not lista:
        print("Nada para salvar.")
        return
    df = pd.DataFrame(lista)
    df.drop_duplicates(subset="Link", inplace=True)
    df.to_excel("vagas_com_detalhes.xlsx", index=False)
    print("📁 Planilha detalhada salva: vagas_com_detalhes.xlsx")

salvar_planilha_detalhada(DETALHES)




















#button_vaga = navegador_flare.find_element(By.XPATH, "//*[@id='filter-jobtype1']")


# button_estagio = navegador_flare.find_element(By.XPATH, "//*[@id='filter-jobtype1-2']")


# button_filtrar = navegador_flare.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div[3]/button[2]")


time.sleep(100)