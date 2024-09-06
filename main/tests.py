from django.test import TestCase, Client
from .models import Product
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Sample Product",
            price=1000,
            description="This is a sample product description."
        )

    def test_product_creation(self):
        product = Product.objects.get(name="Sample Product")
        self.assertEqual(product.name, "Sample Product")
        self.assertEqual(product.price, 1000)
        self.assertEqual(product.description, "This is a sample product description.")

    def test_price_should_be_integer(self):
        with self.assertRaises(IntegrityError):
            Product.objects.create(name="Invalid Product", price="not_an_integer", description="Invalid price")

    def test_price_cannot_be_negative(self):
        with self.assertRaises(ValidationError):
            product = Product(name="Negative Price Product", price=-100, description="Price should be positive")
            product.full_clean()  # This will trigger the validation

    def test_max_length_of_name(self):
        long_name = "a" * 256  # One character more than the max length
        with self.assertRaises(ValidationError):
            product = Product(name=long_name, price=500, description="Description")
            product.full_clean()  # This will trigger the validation


