from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from .models import Category


class CategoryListCreateApiTests(APITestCase):
    def test_get_lists_categories(self):
        category = Category.objects.create(name='Birthday cake')

        response = self.client.get('/categories/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [{'id': category.id, 'name': category.name}])

    def test_post_creates_category_for_staff_user(self):
        staff_user = get_user_model().objects.create_user(
            username='category-admin',
            password='test-password',
            is_staff=True,
        )
        self.client.force_authenticate(user=staff_user)

        response = self.client.post('/categories/', {'name': 'Wedding cake'})

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Category.objects.filter(name='Wedding cake').exists())
