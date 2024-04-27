# quotes/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Quote, Author

class QuoteAPITestCase(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name='John Doe', date_of_birth='1990-01-01')
        self.quote = Quote.objects.create(text='Test Quote', author=self.author)

    def test_quote_list(self):
        url = reverse('quote-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_quote(self):
        url = reverse('quote-list-create')
        data = {'text': 'New Quote', 'author': self.author.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Quote.objects.count(), 2)

    def test_retrieve_quote(self):
        url = reverse('quote-detail', kwargs={'pk': self.quote.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_quote(self):
        url = reverse('quote-detail', kwargs={'pk': self.quote.id})
        data = {'text': 'Updated Quote', 'author': self.author.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Quote.objects.get(id=self.quote.id).text, 'Updated Quote')

    def test_delete_quote(self):
        url = reverse('quote-detail', kwargs={'pk': self.quote.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Quote.objects.count(), 0)
