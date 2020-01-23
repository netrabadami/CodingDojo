class Store:
	def __init__(self,name,products = []):
		self.name = name
		self.products = products
		self.Product = Product(name="",price=10,category="")


	def add_product(self,new_product):
		self.products.append(new_product)
		print("new_product", self.products)
		return self.products

	def sell_product(self, id):
		del self.products[id]
		return self.products

	def inflation(self, percent_increase,is_increased):
		price_update = self.Product.update_price(percent_increase,is_increased)
		return price_update


class Product:
	"""docstring for Product"""
	def __init__(self, name, price, category):
		self.name = name
		self.price = price
		self.category = category

	def update_price(self, percent_change, is_increased):
		if(is_increased):
			self.price += self.price * percent_change/100
		else:
			self.price -= self.price * percent_change/100		

		return self.price	

	def print_info(self):
		print("Name: ",self.name, "Price: ",self.price," category: ",category)


p1 = Product("tacos", 100,"food")
p2 = Product("chips",5,"food")
s1 = Store("san Jose",["milk"])

print(p1.update_price(1,True))
print(p1.update_price(1,False))
print(s1.add_product("coco"))
print(s1.add_product("candy"))
print(s1.add_product("biscuits"))
print(s1.sell_product(-1))
print(s1.inflation(1,True))



		