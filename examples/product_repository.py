from common.product_repository import ProductRepository

product_repository = ProductRepository()

product_repository.add_product("Product 1")
product_repository.add_product("Product 2")

print(product_repository.get_products())
