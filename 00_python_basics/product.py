class Product:
    def __init__(self, produce_name, product_price, product_desc):
        self.produce_name = produce_name
        self.product_price = product_price
        self.product_desc = product_desc
        
        def get_name(self):
            return self.produce_name

        def set_name(self, name):
            self.produce_name = name
            
            p1 = Product("Tablet", 963258, "qwerty")
            print(p1.get_name())
            
            