from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import pyautogui
import time

# Configurações iniciais
pyautogui.PAUSE = 0.3
VAGAS = []

# Função para aplicar os filtros usando PyAutoGUI
def aplicar_filtros():
    print("⌛ Aplicando filtros com pyautogui...")
    time.sleep(7)  # Espera o site carregar por completo

    # Clique na Área
    pyautogui.click(x=908, y=329)
    time.sleep(1)

    # Clique no Tipo de vaga
    pyautogui.click(x=823, y=669)
    time.sleep(1)
    pyautogui.click(x=996, y=926)
    time.sleep(1)

    # Clique na Senioridade
    pyautogui.click(x=1294, y=322)
    time.sleep(1)
    pyautogui.click(x=392, y=391)
    time.sleep(1)
    pyautogui.click(x=396, y=556)
    time.sleep(1)
    pyautogui.click(x=988, y=631)

    print("✅ Filtros aplicados.")
    time.sleep(5)  # Espera 5 segundos ANTES de continuar com o Selenium


# Inicia navegador com opções estáveis
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

navegador = webdriver.Chrome(options=options)
navegador.get("https://www.infojobs.com.br/empregos.aspx?poblacion=5208622")
time.sleep(3)

# Garante que a janela está visível e ativa
navegador.maximize_window()
navegador.switch_to.window(navegador.current_window_handle)

# Aceita cookies
try:
    espera = WebDriverWait(navegador, 10)
    botao_cookie = espera.until(EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button")))
    botao_cookie.click()
    print("🍪 Cookies aceitos.")
except:
    print("⚠️ Botão de cookies não encontrado.")

# Aplica filtros com pyautogui
aplicar_filtros()

# Scroll com Selenium
try:
    navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
except Exception as e:
    print("❌ Erro no scroll:", e)

# Espera as vagas carregarem
try:
    WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/vaga-de-")]'))
    )
except:
    print("❌ Nenhuma vaga carregada a tempo.")

# Coleta links das vagas
print("🔍 Coletando links...")
elementos = navegador.find_elements(By.XPATH, '//a[contains(@href, "/vaga-de-")]')
for el in elementos:
    href = el.get_attribute("href")
    if href and "infojobs.com.br/vaga-de" in href:
        VAGAS.append(href)
    print(f"🔗 {len(VAGAS)} links encontrados.")
    navegador.quit()

def salvar_planilha(vagas):
    if not vagas:
        print("Nenhuma vaga foi encontrada para salvar.")
        return
    df = pd.DataFrame(vagas, columns=["Link"])
    df.drop_duplicates(subset="Link", inplace=True)
    df.to_excel("vagas_infojobs.xlsx", index=False)
    print("Planilha salva com sucesso: vagas_infojobs.xlsx")

# Espera para visualização final
time.sleep(10)
salvar_planilha(VAGAS)

