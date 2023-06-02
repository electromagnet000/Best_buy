import pytest
import products


def is_true():
    return True


def test_product_details():
    product1 = products.Product("Product A", 100, 100)
    assert product1.name == "Product A"
    assert product1.price == 100
    assert product1.quantity == 100


def test_valid_details():
    product1 = products.Product("Product A", 100, 100)
    assert product1.name != None
    assert product1.price > 0
    assert product1.quantity > 0

def test_acitve():

    product1 = products.Product("Product A", 100, 100)
    product1.get_quantity() == 100
    assert product1.is_active() == True

    product1.set_quantity(0)
    assert product1.is_active() == False

    product3 = products.Non_stocked_products("product3", 100)
    assert  product3.name == "product3"
    assert product3.price == 100
    assert  product3.active == True

def test_inacitve():
    product2 = products.Product("Product2", 100, 0)
    assert product2.get_quantity() == 0
    assert product2.is_active() == False

    product2.set_quantity(100)
    assert product2.is_active() == True

def test_purchase():

    product1 = products.Product("Product A", 1, 100)
    assert product1.buy(100) == 100
    product1.set_quantity(100)
    assert product1.buy(1) == 1
    assert product1.buy(0) == 0
    assert product1.buy(-1) == -1


