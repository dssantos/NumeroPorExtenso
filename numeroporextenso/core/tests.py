from django.test import TestCase

from .forms import ConverterForm
from .views import converter


class HomeTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """GET must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """"Must use template index.html"""
        self.assertTemplateUsed(self.response, 'index.html')


class ConvertFormTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_html(self):
        """Html must contain some tags"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input')
        self.assertContains(self.response, 'type="number"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have converter form"""
        form = self.response.context['form']
        self.assertIsInstance(form, ConverterForm)

    def test_form_has_number_field(self):
        """Form must have a number field"""
        form = self.response.context['form']
        self.assertSequenceEqual(['number'], list(form.fields))


class ConvertInvalidValueTest(TestCase):

    def test_value_over_quintillion(self):
        """Should show error if the value is greater than or equal to one quintillion"""
        data = dict(number=10**18,)
        self.response = self.client.post('/', data)
        form = self.response.context['form']
        self.assertTrue(form.errors)

    def test_blank_value(self):
        """Should show error if the value is blank"""
        self.response = self.client.post('/', {})
        form = self.response.context['form']
        self.assertTrue(form.errors)


class ConvertSucessTest(TestCase):

    def test_convert_integrer(self):
        """Must show converted integrer on html page"""
        data = dict(number=1234,)
        self.response = self.client.post('/', data)
        self.assertContains(self.response, 'Mil, duzentos e trinta e quatro')

    def test_convert_decimal(self):
        """Must show converted decimal on html page"""
        data = dict(number=1234.56,)
        self.response = self.client.post('/', data)
        self.assertContains(self.response, 'Mil, duzentos e trinta e quatro vírgula cinco seis')


class ConverterTest(TestCase):

    def test_converter(self):
        """Must return expected converted value"""
        self.assertEqual(converter(1234), 'mil, duzentos e trinta e quatro')
        self.assertEqual(converter(1234.56), 'mil, duzentos e trinta e quatro vírgula cinco seis')
        self.assertEqual(converter(1234567890), 'um bilhão, duzentos e trinta e quatro milhões, quinhentos e sessenta e sete mil, oitocentos e noventa')
        self.assertEqual(converter(999999999999999999), '''novecentos e noventa e nove quatrilhões, novecentos e noventa e nove trilhões e novecentos e noventa e nove bilhões, novecentos e noventa e nove milhões, novecentos e noventa e nove mil, novecentos e noventa e nove''')
