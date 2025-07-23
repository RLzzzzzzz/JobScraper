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

# Acessa o site com os filtros já definidos (pode ajustar o link direto)
navegador_flare.get("https://br.indeed.com/jobs?q=est%C3%A1gio&l=Rio+de+Janeiro%2C+RJ")
navegador_flare.maximize_window()
time.sleep(9)

# Tenta clicar no botão de cookies, se existir
try:
    cookie_indeed = WebDriverWait(navegador_flare, 5).until(
        EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
    )
    cookie_indeed.click()
except:
    print("Cookie já aceito ou botão não encontrado.")

#(opcional) Se quiser manter os cliques do pyautogui, mantenha aqui:
pyautogui.click(x=877, y=281)
pyautogui.click(x=815, y=479)
pyautogui.click(x=1119, y=777)

# Espera o carregamento dos elementos da vaga
time.sleep(3)

# Coleta os elementos com data-jk
blocos = navegador_flare.find_elements(By.XPATH, '//a[@data-jk]')

base_url = "https://br.indeed.com/viewjob?jk="

for el in blocos:
    jk = el.get_attribute("data-jk")
    if jk:
        link = f"{base_url}{jk}"
        if link not in VAGAS:
            VAGAS.append(link)

print(f"🔗 {len(VAGAS)} links encontrados.")

# Salva em Excel
def salvar_planilha(vagas):
    if not vagas:
        print("Nenhuma vaga foi encontrada para salvar.")
        return
    df = pd.DataFrame(vagas, columns=["Link"])
    df.drop_duplicates(subset="Link", inplace=True)
    df.to_excel("vagas.xlsx", index=False)
    print("Planilha salva com sucesso: vagas.xlsx")

salvar_planilha(VAGAS)
