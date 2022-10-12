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

    def test_buscando_um_novo_animal(self):
        """
        Teste se um usuário encontra um animal pesquisando.
        """
        # Vini deseja encontrar um novo animal para adotar.

        # Ele encontra o Busca Animal e decide usar o site, 
        # porque ele vê no menu do site escrito Busca Animal.

        # Ele vê um campo para pesquisar animais pelo nome.

        # Ele pesquisa por Leão e clica no botão Pesquisar.

        # O site exibe 4 características do animal pesquisado.

        # Ele desiste de adotar um leão.
