from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


def load_data(year):
    # Configurações do WebDriver headless
    options = Options()
    options.headless = True  # Roda o navegador em modo headless
    options.add_argument('--disable-gpu')  # Desativa uso da GPU para otimização em headless
    options.add_argument('--no-sandbox')  # Requerido para algumas distribuições Linux
    driver = webdriver.Chrome(options=options)

    try:
        # Acessa a página
        year = int(str(year)[-2:])
        url = f"https://fbref.com/pt/comps/{year}/stats/Serie-A-Estatisticas"
        driver.get(url)

        # Espera o link "Estatísticas Padrão" aparecer e clica
        estatisticas_padrao_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[@href='/pt/comps/{year}/stats/Serie-A-Estatisticas']"))
        )
        estatisticas_padrao_link.click()

        # Espera o botão "Trocar para visualização em widescreen" aparecer e clica
        widescreen_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'tooltip') and contains(text(), 'Trocar para visualização em widescreen')]"))
        )
        widescreen_button.click()

        # Espera a tabela "stats_standard" ser carregada
        stats_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "stats_standard"))
        )

        # Extrai a tabela e converte para um DataFrame do pandas
        table_html = stats_table.get_attribute('outerHTML')
        df = pd.read_html(table_html)[0]

        return df

    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return None

    finally:
        # Fecha o driver
        driver.quit()
