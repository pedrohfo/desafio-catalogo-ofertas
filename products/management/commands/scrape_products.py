from django.core.management.base import BaseCommand
from products.models import Product
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import time

class Command(BaseCommand):
    help = 'Scrape products from a website using Selenium and save them to the database'

    def handle(self, *args, **kwargs):
        # Configure Selenium options
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # Run in headless mode (no browser UI)
        chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
        chrome_options.add_argument("--no-sandbox")  # Disable sandboxing for Linux

        # Path to your ChromeDriver (update this to your ChromeDriver path)
        chrome_driver_path = r"C:\Users\pedro\OneDrive\Área de Trabalho\desafio-catalogo-ofertas\chromedriver\chromedriver.exe"

        # Initialize the WebDriver
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        try:
            # Replace with the URL of the website you want to scrape
            url = 'https://www.mercadolivre.com.br'
            search_string = 'Computador Gamer i7 16gb ssd 1tb'
            driver.get(url)

            # Wait for the page to load (adjust the sleep time as needed)
            time.sleep(2)

            # Example: Find product elements using Selenium
            search_input = driver.find_element(By.ID, 'cb1-edit')
            search_input.send_keys(search_string)
            time.sleep(0.5)
            search_input.send_keys(Keys.ENTER)
            time.sleep(4)

            # Get the initial scroll height
            last_height = driver.execute_script("return document.body.scrollHeight")
            current_position = 0
            scroll_step = 400  # Scroll 200 pixels at a time
            scroll_delay = 0.2  # Wait 1 second between scrolls

            page = 1
            while page != -1:
                last_height = driver.execute_script("return document.body.scrollHeight")
                current_position = 0
                driver.execute_script("window.scrollTo(0, 0);")
            # Scroll slowly to the bottom
                while current_position < last_height:
                    # Scroll down by `scroll_step` pixels
                    driver.execute_script(f"window.scrollTo(0, {current_position});")
                    current_position += scroll_step

                    # Wait for the delay
                    time.sleep(scroll_delay)

                    # Update the last height in case new content is loaded
                    last_height = driver.execute_script("return document.body.scrollHeight")

                products = driver.find_elements(By.CSS_SELECTOR, 'div.product')

                # Locate the product list container
                product_list = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[3]/section/ol')

                # Find all product elements within the list
                products = product_list.find_elements(By.XPATH, './li')

                for index, product in enumerate(products, start=1):

                    # test if there is an evaluation div
                    ev_xpath = f'/html/body/main/div/div[3]/section/ol/li[{index}]/div/div/div[2]/div[1]/span[1]'
                    ev = 0
                    try:
                        if (str(driver.find_element(By.XPATH, ev_xpath).text).startswith('Avaliação')):
                            ev = 1
                    except Exception as e:
                        ev = 0
                        self.stdout.write(self.style.WARNING(f'Error finding eval path of product {index}: {str(e)}'))

                    # Construct the XPath for the image element of the current product
                    # image_xpath = f'/html/body/main/div/div[3]/section/ol/li[{index}]/div/div/div[1]/section/div[2]/div/div/div[1]/a/img'
                    image_xpath = f'/html/body/main/div/div[3]/section/ol/li[{index}]/div/div/div[1]/img'
                    # image_opt_xpath = f'/html/body/main/div/div[3]/section/ol/li[{index}]/div/div/div[1]/section/div[2]/div/div/div[1]/a/img'
                    nome_xpath = f'/html/body/main/div/div[3]/section/ol/li[{index}]/div/div/div[2]/h3/a'
                    preco_xpath = f'/html/body/main/div/div[3]/section/ol/li[{index}]/div/div/div[2]/div[{str(1+ev)}]/div/span[1]/span[2]'
                    parcelas_xpath = f'/html/body/main/div/div[3]/section/ol/li[{index}]/div/div/div[2]/div[{str(1+ev)}]/span'  #/text()[1]' # N DE PARCELAS
                    # juros_xpath = f'/html/body/main/div/div[3]/section/ol/li[{index}]/div/div/div[2]/div[{str(1+ev)}]/span/text()[2]' # JUROS
                    link_xpath = f'/html/body/main/div/div[3]/section/ol/li[{index}]/div/div/div[2]/h3/a'
                    preco_sem_desconto_xpath = f'/html/body/main/div/div[3]/section/ol/li[{index}]/div/div/div[2]/div[{str(1+ev)}]/s/span[2]' #/text()'
                    percentual_desconto_xpath = f'/html/body/main/div/div[3]/section/ol/li[{index}]/div/div/div[2]/div[{str(1+ev)}]/div/span[2]'
                    # tipo_entrega_xpath = f'/html/body/main/div/div[3]/section/ol/li[{index}]/div/div/div[2]/span/svg'
                    tipo_entrega_xpath = f'/html/body/main/div/div[3]/section/ol/li[{index}]/div/div/div[2]/span'
                    frete_gratis_xpath = f'/html/body/main/div/div[3]/section/ol/li[{index}]/div/div/div[2]/div[{str(2+ev)}]'
                    frete_gratis_opt_xpath = f'/html/body/main/div/div[3]/section/ol/li[{index}]/div/div/div[2]/div[{str(2+ev)}]/span[1]'

                    try:
                        image_element = driver.find_element(By.XPATH, image_xpath)
                        # image_element_opt = driver.find_element(By.XPATH, image_opt_xpath)
                        imagem1 = image_element.get_attribute('src')
                        # imagem2 = image_element_opt.get_attribute('src')
                        if imagem1.startswith('http'):
                            imagem = imagem1
                        # elif imagem2.startswith('http'):
                        #     imagem = imagem2
                        else:
                            imagem = None

                        if index == 10:
                            print(imagem.__len__())
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f'Error extracting image for product {index}: {str(e)}'))
                        imagem = None

                    try:
                        nome_element = driver.find_element(By.XPATH, nome_xpath)
                        nome = str(nome_element.text)
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f'Error extracting name for product {index}: {str(e)}'))
                        nome = None

                    try:
                        preco_element = driver.find_element(By.XPATH, preco_xpath)
                        preco = float(preco_element.text.replace('.', '').replace(',', '.'))
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f'Error extracting price for product {index}: {str(e)}'))
                        preco = None

                    try:
                        parcelas_element = driver.find_element(By.XPATH, parcelas_xpath)
                        # juros_element = driver.find_element(By.XPATH, juros_xpath)
                        # parcelamento = str(parcelas_element.text) + str(juros_element.text)
                        parcelamento = parcelas_element.text
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f'Error extracting installment or interest for product {index}: {str(e)}'))
                        parcelamento = None

                    try:
                        link_element = driver.find_element(By.XPATH, link_xpath)
                        link = link_element.get_attribute('href')
                        if index == 10:
                            print(link.__len__())
                            print(link)
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f'Error extracting link for product {index}: {str(e)}'))
                        link = None

                    try:
                        preco_sem_desconto_element = driver.find_element(By.XPATH, preco_sem_desconto_xpath)
                        preco_sem_desconto = float(preco_sem_desconto_element.text.replace('.', '').replace(',', '.'))
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f'Error extracting price without discount for product {index}: {str(e)}'))
                        preco_sem_desconto = None

                    try:
                        percentual_desconto_element = driver.find_element(By.XPATH, percentual_desconto_xpath)
                        percentual_desconto = float(percentual_desconto_element.text.split('%')[0])
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f'Error extracting discount for product {index}: {str(e)}'))
                        percentual_desconto = 0

                    try:
                        tipo_entrega_element = driver.find_element(By.XPATH, tipo_entrega_xpath)
                        tipo_entrega = tipo_entrega_element.text
                        if (tipo_entrega.startswith('Enviado pelo')):
                            tipo_entrega = 'Full'
                        else:
                            tipo_entrega = 'Normal'
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f'Error extracting delivering type for product {index}: {str(e)}'))
                        tipo_entrega = 'Normal'

                    try:
                        frete_gratis_element = driver.find_element(By.XPATH, frete_gratis_xpath)
                        frete_gratis = frete_gratis_element.text
                        if frete_gratis.startswith('Frete grátis'):
                            frete_gratis = True
                        else:
                            frete_gratis = False
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f'Error extracting freight for product {index}: {str(e)}'))
                        frete_gratis = False

                    try:
                        frete_gratis_element_opt = driver.find_element(By.XPATH, frete_gratis_opt_xpath)
                        frete_gratis_opt = frete_gratis_element_opt.text
                        if frete_gratis_opt.startswith('Chegará grátis'):
                            frete_gratis = True
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f'Error extracting opt freight for product {index}: {str(e)}'))

                    # Save the product to the database
                    Product.objects.create(
                        imagem=imagem,
                        nome=nome,
                        preco=preco,
                        parcelamento=parcelamento,  # Now stored as a string
                        link=link,
                        preco_sem_desconto=preco_sem_desconto,
                        percentual_desconto=percentual_desconto,
                        tipo_entrega=tipo_entrega,
                        frete_gratis=frete_gratis,
                    )

                self.stdout.write(self.style.SUCCESS('Successfully scraped and saved products for page' + str(page)))
                page_xpath = f'/html/body/main/div/div[3]/section/nav/ul/li[{str(page+1)}]/a'
                try:
                    page_element = driver.find_element(By.XPATH, page_xpath)
                    page_element.click()
                    time.sleep(5)
                    page+=1
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Page {page} not found!: {str(e)}'))
                    page = -1

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error during scraping: {str(e)}'))

        finally:
            # Close the browser
            driver.quit()