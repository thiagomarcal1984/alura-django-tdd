from django.test import TestCase, RequestFactory
from animais.models import Animal

class AnimalModelTestCase(TestCase):
    def setUp(self) -> None:
        # O objeto que será criado abaixo não entrará para o DB de produção.
        self.animal = Animal.objects.create(
            nome_animal = 'Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não',
        ) 

    def test_animal_cadastrado_com_caracteristicas(self):
        """Teste que verifica se o animal está cadastrado com as suas respectivas características."""
        self.assertEqual(self.animal.nome_animal, 'Leão')
