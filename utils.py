from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from datetime import datetime
import pandas as pd
import os

def iniciar_navegador(normal=True):
    if normal:
        return webdriver.Chrome()
    else:
        options = uc.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-blink-features=AutomationControlled")
        return uc.Chrome(options=options)

def salvar_planilha(df, nome_arquivo, subpasta="planilhas"):
    if df.empty:
        print(f"Nada para salvar em {nome_arquivo}.")
        return
    data_hoje = datetime.today().strftime('%Y-%m-%d')
    pasta = os.path.join(data_hoje, subpasta)
    os.makedirs(pasta, exist_ok=True)
    caminho = os.path.join(pasta, nome_arquivo)
    df.to_excel(caminho, index=False)
    print(f"📁 Planilha salva em: {caminho}")
