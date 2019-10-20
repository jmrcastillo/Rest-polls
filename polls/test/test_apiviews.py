

from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
# autho rest
from rest_framework.authtoken.models import Token
# auth django
from django.contrib.auth import get_user_model


from polls.apiviews import PollViewSet


class TestPoll(APITestCase):

    def setUp(self):
        # apiclient
        self.client = APIClient()
        # API Request
        self.factory = APIRequestFactory()
        self.view = PollViewSet.as_view({'get': 'list'})
        self.uri = '/polls/'
        # user
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        """Create sample user to authenticate"""
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='testUser@test.com',
            password='test'
        )

    def test_list(self):
        request = self.factory.get(self.uri,
                                   HTTP_AUTHORIZATION=f'Token {self.token.key}')
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, recieved {response.status_code}')

    def test_list2(self):
        # Login
        self.client.login(username="test", password="test")
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, recieved {response.status_code}')

    def test_create(self):
        self.client.login(username="test", password="test")
        params = {
            "question": "How are you",
            "created_by": 1
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 201,
                         f'Expected Response Code 201, recieved {response.status_code}')
