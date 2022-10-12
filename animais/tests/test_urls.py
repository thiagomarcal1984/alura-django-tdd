from django.test import TestCase, RequestFactory
from animais.views import index

class AnimaisURLSTestcase(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory() # Fábrica de requisições na aplicação.

    def test_rota_url_utiliza_view_index(self):
        """Teste se a home da aplicação utiliza a função index da view."""
        request = self.factory.get('/')
        response = index(request)
        self.assertEqual(response.status_code, 200)
