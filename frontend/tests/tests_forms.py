# Run tests with python3 manage.py test frontend.test --verbosity 2
from django.test import TestCase

# Create your tests here.
from frontend.forms import NINPostForm


class APIFormTest(TestCase):
    """Test NIN form fields"""

    def test_nin_post_form(self):
        """Test that the field's label is correct"""
        form = NINPostForm()
        self.assertTrue(form.fields['nin'].label == None or form.fields['nin'].label == 'nin')
        print('\n=====================================================')

    # self.assertTrue(form.fields['renewal_date'].label == None or form.fields['renewal_date'].label == 'renewal date')

    def test_nin_post_form_help_text(self):
        """Test that the field's help_text is correct"""
        form = NINPostForm()
        self.assertEqual(form.fields['nin'].help_text, 'e.g. 123xxxxxxxx')
        print('\n=====================================================')

    def test_nin_post_form_correct_nin(self):
        """Test that the nin is valid"""
        nin = 12345678924
        form = NINPostForm(data={'nin': nin})
        self.assertTrue(form.is_valid())
        print('\n=====================================================')

    def test_nin_post_form_incorrect_nin(self):
        """Test that the form is invalid upon invalid nin"""
        nin = 'akdjkj8888'
        form = NINPostForm(data={'nin': nin})
        self.assertFalse(form.is_valid())
        print('\n=====================================================')
