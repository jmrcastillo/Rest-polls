

from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
# autho rest
from rest_framework.authtoken.models import Token
# auth django
from django.contrib.auth import get_user_model


from polls.apiviews import PollViewSet


class TestPoll(APITestCase):

    def setUp(self):
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
