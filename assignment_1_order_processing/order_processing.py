class Order():
    def __init__(self, order_id, type_of_order, properties_dict):
        self.order_id = order_id
        self.type = type_of_order
        self.properties_dict = properties_dict

    def edit(self, type_of_order, properties_dict):
        self.type = type_of_order
        self.properties_dict = properties_dict

class OrderProcessor():
    def __init__(self, orders_to_be_processed):
        self.orders_to_be_processed = orders_to_be_processed

    def add_order_to_be_processed(self, order):
        self.orders_to_be_processed.append(order)

    
