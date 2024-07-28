from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time

def tirar_screenshot_objeto():

    url = 'https://app.powerbi.com/view?r=eyJrIjoiOTZlNWFhYTktN2Y1Yy00NjM1LWIzNDItZmIyMTY2N2FmMDY0IiwidCI6ImFkY2JiMThhLWE3NzEtNDU5OS04YjllLWFiM2IzNmE3NWY1MSJ9'
    xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container/transform/div/div[3]/div/div'  # Substitua pelo XPath do objeto

    # Configuração do Chrome WebDriver
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # Aguarda a página carregar
    time.sleep(3)

    # Encontra o objeto específico
    objeto = driver.find_element(By.XPATH, xpath)

    # Tira uma captura de tela da página inteira
    screenshot_path = 'screenshot_page.png'
    driver.save_screenshot(screenshot_path)

    # Obtém as dimensões do objeto
    location = objeto.location
    size = objeto.size

    # Abre a captura de tela com o Pillow
    imagem = Image.open(screenshot_path)

    # Define a área do objeto
    left = location['x'] + 70
    top = location['y']
    right = location['x'] + size['width'] - 170
    bottom = location['y'] + size['height'] - 180

    # Recorta a imagem para apenas a área do objeto
    imagem_objeto = imagem.crop((left, top, right, bottom))

    # Salva a imagem do objeto
    objeto_screenshot_path = 'screenshot_objeto.png'
    imagem_objeto.save(objeto_screenshot_path)

    # Fecha o WebDriver
    driver.quit()

    return objeto_screenshot_path

