from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet

class IndexViewTestCase(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()

    def test_index_view_retorna_caracteristicas_do_animal(self):
        """Teste que verifica se a index retorna as características do animal pesquisado."""
        response = self.client.get('/', 
            {
                'caracteristicas' : 'resultado'
            }
        )
        self.assertIs(type(response.context['caracteristicas']), QuerySet)