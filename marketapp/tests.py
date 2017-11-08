import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Owner
from authapp.models import CustomUser
from django.contrib.auth import authenticate, login, logout


def create_owner(name, surname):
    """
    Creation of Owner model instance.
    """
    return Owner.objects.create(name=name, surname=surname)

def create_user(username, password):
    """
    Creation of CustomUser model instance.
    """
    user = CustomUser(username=username)
    user.set_password(password)
    user.save()
    return user

class OwnerListViewTests(TestCase):
    def test_login_requirement(self):
        """
        Tests login requirement.
        """
        response = self.client.get(reverse('owners'))
        self.assertEqual(response.status_code, 302)


    def test_login_redirect(self):
        """
        Tests redirection not logged users to login page.
        """
        response = self.client.get(reverse('owners'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/signin/?next=/owners/')


    def test_context_queryset_empty(self):
        """
        Tests empty queryset
        """
        create_user("username", "Ppassword12")
        self.client.login(username='username', password='Ppassword12')
        response = self.client.get(reverse('owners'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['owners'], Owner.objects.all())

    def test_context_queryset_notempty(self):
        """
        Tests not empty queryset
        """
        create_owner("name1", "surname1")
        create_user("username", "Ppassword12")
        self.client.login(username='username', password='Ppassword12')
        response = self.client.get(reverse('owners'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['owners'], ['<Owner: name1 surname1>'])


