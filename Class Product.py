class Product:
  def __init__(self, name, price, description, evaluation):
    self.name = name
    self.price = price
    self.description = description
    self.evaluation = evaluation

product_1 = Product("sports shoes","$96", "white color, size 34-43", "5-stars")
product_2 = Product("lipstick", "$10", "red color, smell flowers", "4-stars")
product_3 = Product("necklace", "$1000", "pure gold", "5-stars")
product_4 = Product("shirt", "$100", "black shirt , %100 cotton", "4-stars")

print(f"The first product name is {product_1.name}")
print(f"The second product evaluation is {product_2. evaluation}")
print(f"The third product price is {product_3.price}")
print(f"The fourth product description is {product_4.description}")