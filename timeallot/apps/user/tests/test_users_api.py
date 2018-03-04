from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from timeallot.apps.user.models import TimerUser


class GeneralUserAPITest(APITestCase):
    fixtures = ['test_users']

    def setUp(self):
        self.client = APIClient()
        self.authenticated_user = TimerUser.objects.get(email='admin@admin.com')
        self.all_users = TimerUser.objects.all()

    def test_view_users_list_if_authenticated(self):
        """
        Ensure you can see the users list if authenticated.
        """
        self.client.force_authenticate(user=self.authenticated_user)
        response = self.client.get('/users/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), len(self.all_users))

    def test_cannot_view_users_list_if_not_authenticated(self):
        """
        Ensure unauthenticated users cannot see the users list.
        """
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cannot_view_users_list_if_not_permission(self):
        """
       Ensure you can see the users list if you have correct permissions.
       Normal users should not be able to see it.
       """
        self.fail("Finish the test!")

    def test_can_edit_user(self):
        """
        Ensure superusers can edit any user, and normal users can edit their own.
        """
        self.fail("Finish the test!")

    def test_can_delete_user(self):
        """
        Ensure superusers can delete any user, and normal users can delete their own.
        """
        self.fail("Finish the test!")

    def test_normal_user_can_see_own_detail_view(self):
        """
        Ensure normal users have permission to see their own user info.
        """
        self.fail("Finish the test!")

    def test_normal_user_cannot_see_others_detail_view(self):
        """
        Ensure normal users do not have permission to see other peoples user info.
        """
        self.fail("Finish the test!")


class CreateUsersAPITest(APITestCase):
    fixtures = ['test_users']

    def setUp(self):
        self.client = APIClient()
        self.authenticated_user = TimerUser.objects.get(email='admin@admin.com')
        self.all_users = TimerUser.objects.all()

    def test_can_create_user(self):
        """
        Ensure we can create a new user object with email and password
        """
        self.client.force_authenticate(user=self.authenticated_user)
        response = self.client.post('/users/', {'email': 'testcreate@test.com', 'password': 'testpassword'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TimerUser.objects.count(), 2)

        new_user = TimerUser.objects.get(email='testcreate@test.com')
        print(new_user.password)

        # Test user data
        self.assertEqual(new_user.email, 'testcreate@test.com')
        self.assertIsNone(new_user.display_name)
        self.assertEqual(new_user.get_full_name(), 'testcreate')
        self.assertEqual(new_user.get_short_name(), 'testcreate')
        self.assertEqual(new_user.is_active, True)
        self.assertEqual(new_user.is_admin, False)
        self.assertEqual(new_user.is_staff, False)

        # Try to login with the user.
        self.assertTrue(authenticate(email='testcreate@test.com', password='testpassword'))

    def test_with_only_email(self):
        """
        Ensure we can create a new user object with only email.
        """
        self.client.force_authenticate(user=self.authenticated_user)
        response = self.client.post('/users/', {'email': 'testcreate@test.com'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TimerUser.objects.count(), 2)
        self.assertEqual(TimerUser.objects.get(email='testcreate@test.com').email, 'testcreate@test.com')

    def test_with_password_and_display_name(self):
        """
        Ensure we can create a new user object with both email and display name.
        """
        self.client.force_authenticate(user=self.authenticated_user)
        data = {'email': 'testcreate@test.com', 'display_name': 'The Ultimate Tester'}
        response = self.client.post('/users/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        new_user = TimerUser.objects.get(email='testcreate@test.com')

        self.assertEqual(TimerUser.objects.count(), 2)
        self.assertEqual(new_user.display_name, 'The Ultimate Tester')

    def test_with_invalid_password(self):
        """
        Ensure we cannot create a user with invalid password.
        """
        self.client.force_authenticate(user=self.authenticated_user)

        # Too short
        response = self.client.post('/users/', {'email': 'testcreate@test.com', 'password': 'abc'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Empty
        response = self.client.post('/users/', {'email': 'testcreate@test.com', 'password': ''}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Special invalid characters
        response = self.client.post('/users/', {'email': 'testcreate@test.com', 'password': 'ab1a£sdka15¥&s*-__'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Final confirmation that user was not made
        self.assertEqual(TimerUser.objects.count(), 1)
        self.assertIsNone(TimerUser.objects.get(email='testcreate@test.com'))

    def test_with_no_data(self):
        self.client.force_authenticate(user=self.authenticated_user)
        response = self.client.post('/users/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_with_existing_email(self):
        self.client.force_authenticate(user=self.authenticated_user)
        response = self.client.post('/users/', {'email': 'admin@admin.com'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_with_invalid_email(self):
        self.client.force_authenticate(user=self.authenticated_user)
        response = self.client.post('/users/', {'email': 'invalidemail.com@'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
