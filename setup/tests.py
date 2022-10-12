from os import curdir, path, sep
from django.test import LiveServerTestCase
from selenium import webdriver

class AnimaisTestCase(LiveServerTestCase):
    def setUp(self) -> None:
        driver = "chromedriver.exe"
        self.browser = webdriver.Chrome(f"{path.abspath(curdir)}{sep}{driver}")

    def tearDown(self) -> None:
        self.browser.quit()

    # def test_para_verificar_se_a_janela_ok(self):
    #     self.browser.get("http://www.google.com.br") # Busca URL externa.

    def test_abre_janela_do_chrome(self):
        self.browser.get(self.live_server_url) # Retorna URL do Django Server.

    def test_deu_ruim(self):
        """Teste de exemplo de erro."""
        self.fail("Teste falhou.")
