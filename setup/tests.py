from os import curdir, path, sep
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AnimaisTestCase(LiveServerTestCase):
    def setUp(self) -> None:
        driver = "chromedriver.exe"
        self.browser = webdriver.Chrome(f"{path.abspath(curdir)}{sep}{driver}")

    def tearDown(self) -> None:
        self.browser.quit()

    # def test_para_verificar_se_a_janela_ok(self):
    #     self.browser.get("http://www.google.com.br") # Busca URL externa.

    def test_buscando_um_novo_animal(self):
        """
        Teste se um usuário encontra um animal pesquisando.
        """
        # Vini deseja encontrar um novo animal para adotar.

        # Ele encontra o Busca Animal e decide usar o site,
        home_page = self.browser.get(self.live_server_url + '/') # A barra serve para dar semântica à URL.
        # porque ele vê no menu do site escrito Busca Animal.
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        # brand_element = self.browser.find_element_by_css_selector('.navbar') # Comando antigo do Selenium.
        self.assertEqual('Busca Animal', brand_element.text)

        # Ele vê um campo para pesquisar animais pelo nome.
        # buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        buscar_animal_input = self.browser.find_element(By.ID, 'buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão')

        # Ele pesquisa por Leão e clica no botão Pesquisar.
        buscar_animal_input.send_keys('leão') # Insere o valor "leão" no campo buscar_animal_input.
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()
        time.sleep(2)

        # O site exibe 4 características do animal pesquisado.

        # Ele desiste de adotar um leão.
