from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from apps.bookmarker.models import Category


class TestBookmarkerModels(TestCase):
    def create_category(self, title="Funny Dogs", description="New content"):
        testuser = User.objects.create_user(username="testuser", password="12345")
        return Category.objects.create(
            title=title,
            description=description,
            created_at=timezone.now(),
            created_by=testuser,
        )

    def test_category_creation(self):
        c = self.create_category()
        self.assertTrue(isinstance(c, Category))
        self.assertEqual(c.__str__(), c.title)
