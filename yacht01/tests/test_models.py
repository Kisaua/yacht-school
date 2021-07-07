from django.test import TestCase

# #from phonebook.phonebook.pb.models  import Contact
from yacht01.models  import Contact
# # Create your tests here.
class ContactModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        Contact.objects.create(
            name = 'Serg',
            user_email ='test@test.com',
            subject = 'test subject',
            message = 'Some text',
            )

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)