from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory
from .models import Custom_user
from .views import Custom_userViewSet,FriendshipViewSet
import json

class CustomUserTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user_viewset = Custom_userViewSet
        self.friendships_viewset = FriendshipViewSet
        user1 = Custom_user.objects.create(username="Mark", password="12345")
        user2 = Custom_user.objects.create(username="Jody", password="12345")
        user3 = Custom_user.objects.create(username="Rachel", password="12345")
        user4 = Custom_user.objects.create(username="Joe", password="12345")
        user4.friends.add(user1)

    def test_get_all_users(self):
        request = self.factory.get('/users/')

        response = self.user_viewset.as_view({'get': 'list'})(request)
        response.render()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)), 4)

    def test_get_add_friend(self):
        request = self.factory.get('/friendships/')
        response = self.friendships_viewset.as_view({'get': 'list'})(request)
        response.render()
        self.assertEqual(len(json.loads(response.content)), 1)

        request = self.factory.post('/users/4/add_friend/', {'id': 3}, format='json')
        response = self.user_viewset.as_view({'post': 'add_friend'})(request, pk=4)
        response.render()
        self.assertEqual(response.status_code, 200)

        request = self.factory.post('/users/4/add_friend/', {'id': 1}, format='json')
        response = self.user_viewset.as_view({'post': 'add_friend'})(request, pk=4)
        response.render()
        self.assertEqual(response.status_code, 400)

        request = self.factory.get('/friendships/')
        response = self.friendships_viewset.as_view({'get': 'list'})(request)
        response.render()
        self.assertEqual(len(json.loads(response.content)), 2)
    
    def test_get_user_friends(self):
        request = self.factory.get('/users/1/friends/')
        response = self.user_viewset.as_view({'get': 'friends'})(request, pk=1)
        response.render()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)), 1)
    

class FriendshipsTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user_viewset = Custom_userViewSet
        self.friendships_viewset = FriendshipViewSet
        user1 = Custom_user.objects.create(username="Mark", password="12345")
        user2 = Custom_user.objects.create(username="Jody", password="12345")
        user3 = Custom_user.objects.create(username="Rachel", password="12345")
        user4 = Custom_user.objects.create(username="Joe", password="12345")
        user4.friends.add(user1)
        user4.friends.add(user2)
        user4.friends.add(user3)

    def test_friendships(self):
        request = self.factory.get('/friendships/')
        response = self.friendships_viewset.as_view({'get': 'list'})(request)
        response.render()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)), 3)
