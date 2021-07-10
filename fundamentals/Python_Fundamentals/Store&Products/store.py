class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            priceP = self.price * percent_change
            return self.price + priceP
        else:
            if is_increased == False :
            priceP = self.price * percent_change
            return self.price - priceP
    def print_info(self):
        print(self.name, ' - ', self.category, ' - ', self.price)


class Store:
    def __init__(self, name, list = []):
        self.name = name
        self.list = list
        
    def add_product(self, new_product):
        list.append(new_product)
        return self
    def sell_product(self, id):
        for i in range(len(list)):
            if len[i] == id:
                list.remove(id)
        return self
    def inflation(self, percent_increase):
        if percent_increase > 0:
            return True
        else:
            return False
        
    def set_clearance(self, category, percent_discount):
        #if category == Product.category:
        #    for i in range(len(list)):
        #        list[i] = Product.update_price()
        return self
    
