from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from utils import iniciar_navegador

def aceitar_cookies_infojobs(driver):
    espera = WebDriverWait(driver, 10)
    botao = espera.until(EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button")))
    botao.click()
    print("🍪 Cookies InfoJobs aceitos.")

def aplicar_filtros_infojobs(driver):
    print("🎯 Aplicando filtros no InfoJobs...")
    driver.find_element(By.XPATH, "//*[@id='facetCategory1']/div[1]/a").click()
    espera = WebDriverWait(driver, 5)
    espera.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(., 'Informática, TI, Telecomunicações')]"))).click()
    driver.find_element(By.XPATH, "//*[@id='facetCategory1']/div[2]/div[2]/div[2]/a").click()
    driver.find_element(By.XPATH, "//*[@id='facetManagerialLevel']/div[1]/a").click()
    driver.find_element(By.XPATH, "//label[contains(., 'Estagiário')]").click()
    driver.find_element(By.XPATH, "//*[@id='facetManagerialLevel']/div[2]/div[2]/div[2]/a").click()

def coletar_links_infojobs(driver):
    print("🔍 Coletando links do InfoJobs...")
    elementos = driver.find_elements(By.XPATH, '//a[contains(@href, "/vaga-de-")]')
    links = []
    for el in elementos:
        href = el.get_attribute("href")
        if href and "infojobs.com.br/vaga-de" in href:
            links.append(href)
    print(f"🔗 {len(links)} links encontrados no InfoJobs.")
    return links

#tenho que pegar os caminhos de cada coluna
def detalhes_infojobs(driver, links):
    detalhes = []
    espera = WebDriverWait(driver, 10)

    for link in links:
        driver.get(link)
        # Título da vaga
        try:
            titulo = espera.until(
                EC.presence_of_element_located((By.TAG_NAME, 'h1'))
            ).text
        except:
            titulo = ""
        # Nome da empresa
        try:
            empresa = driver.find_element(
                By.CLASS_NAME, 'profile-company-name'
            ).text
        except:
            empresa = ""
        # Salário (se disponível)
        try:
            salario = driver.find_element(
                By.XPATH, '//span[contains(@class, "salary")]'
            ).text
        except:
            salario = ""
        # Descrição da vaga
        try:
            descricao = driver.find_element(
                By.ID, 'job-description'
            ).text[:300]
        except:
            descricao = ""

        # Classificação de estágio/trainee
        estagio = 'estágio' in titulo.lower() or 'estágio' in descricao.lower()
        trainee = 'trainee' in titulo.lower() or 'trainee' in descricao.lower()

        detalhes.append({
            'Link': link,
            'Título': titulo,
            'Empresa': empresa,
            'Salário': salario,
            'Descrição': descricao,
            'É Estágio?': 'Sim' if estagio else 'Não',
            'É Trainee?': 'Sim' if trainee else 'Não'
        })

    print(f"✅ {len(detalhes)} detalhes coletados.")
    return detalhes

def executar_infojobs():
    driver = iniciar_navegador()
    driver.get("https://www.infojobs.com.br/empregos.aspx?poblacion=5208622")
    driver.maximize_window()

    aceitar_cookies_infojobs(driver) 
    aplicar_filtros_infojobs(driver)
    links = coletar_links_infojobs(driver)

    detalhes = detalhes_infojobs(driver, links)
    df_detalhes = pd.DataFrame(detalhes)

    driver.quit()
    driver.__del__ = lambda: None  

    return df_detalhes
