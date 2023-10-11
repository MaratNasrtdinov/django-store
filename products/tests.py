from django.test import TestCase
from django.urls import reverse
from django.conf import settings
settings.configure()


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'products/index.html')






