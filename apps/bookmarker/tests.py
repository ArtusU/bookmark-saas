from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from apps.bookmarker.models import Category


class TestBookmarkerModels(TestCase):
    def setUp(self):
        self.testuser = User.objects.create_user(username="testuser", password="12345")
        self.category = Category.objects.create(
            title="Funny Dogs",
            description="New content",
            created_at=timezone.now(),
            created_by=self.testuser,
        )

    def test_category_creation(self):
        c = self.category
        self.assertTrue(isinstance(c, Category))
        self.assertEqual(c.__str__(), "Funny Dogs")
