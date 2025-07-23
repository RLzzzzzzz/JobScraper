from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from utils import iniciar_navegador

def aceitar_cookies_indeed(driver):
    espera = WebDriverWait(driver, 10)
    botao = espera.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    botao.click()
    print("🍪 Cookies Indeed aceitos.")

def coletar_links_indeed(driver):
    print("🔍 Coletando links do Indeed...")
    elementos = driver.find_elements(By.XPATH, '//a[contains(@href, "/pagead/clk") or contains(@href, "/rc/clk")]')
    links = []
    for el in elementos:
        href = el.get_attribute("href")
        if href:
            links.append(href)
    print(f"🔗 {len(links)} links encontrados no Indeed.")
    return links

def detalhes_indeed(driver, links):
    detalhes = []
    espera = WebDriverWait(driver, 10)
    for link in links:
        driver.get(link)
        try:
            titulo = espera.until(EC.presence_of_element_located((By.TAG_NAME, 'h1'))).text
        except:
            titulo = ""
        try:
            empresa = driver.find_element(By.CLASS_NAME, 'jobsearch-InlineCompanyRating').text
        except:
            empresa = ""
        try:
            salario = driver.find_element(By.XPATH, '//span[@class="salary-snippet"]').text
        except:
            salario = ""
        try:
            descricao = driver.find_element(By.ID, 'jobDescriptionText').text[:300]
        except:
            descricao = ""

        estagio = "estágio" in titulo.lower() or "estágio" in descricao.lower()
        trainee = "trainee" in titulo.lower() or "trainee" in descricao.lower()

        detalhes.append({
            "Link": link,
            "Título": titulo,
            "Empresa": empresa,
            "Salário": salario,
            "Descrição": descricao,
            "É Estágio?": "Sim" if estagio else "Não",
            "É Trainee?": "Sim" if trainee else "Não"
        })
    print(f"✅ {len(detalhes)} detalhes coletados.")
    return detalhes

def executar_indeed():
    driver = iniciar_navegador(normal=False)
    driver.get("https://br.indeed.com/jobs?q=&l=Rio+de+Janeiro%2C+RJ&from=searchOnHP")
    driver.maximize_window()

    aceitar_cookies_indeed(driver)
    links = coletar_links_indeed(driver)
    detalhes = detalhes_indeed(driver, links)

    driver.quit()
    driver.__del__ = lambda: None  # Silencia o __del__ do UC
    if detalhes:
        df_detalhes = pd.DataFrame(detalhes)
        return df_detalhes
    else:
        return None
