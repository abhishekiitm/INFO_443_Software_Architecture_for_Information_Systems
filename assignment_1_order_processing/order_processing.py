from collections import deque
import copy


class OrderType(object):
    BOOK = 'Book'
    MATERIAL = 'Material'
    FOOD = 'Food'


class Order(object):
    def __init__(self, order_id, order_type, properties_dict):
        self.order_id = order_id
        self.order_type = order_type
        self.properties_dict = properties_dict


class OrderProcessor(object):
    def __init__(self, orders_to_be_processed):
        """
        creates an OrderProcessor class from a list of order objects
        """
        self.to_be_processed_deque = self._convert_orders_to_deque(
            orders_to_be_processed)
        self.to_be_processed_dict = self._convert_orders_to_dict(
            orders_to_be_processed)

    def _convert_orders_to_deque(self, orders):
        """
        this method creates a deque from the order ids
        this deque of order ids will be used to maintain FIFO
        processing of the orders
        """
        order_id_deque = deque()
        for order in orders:
            order_id_deque.append(order.order_id)
        return order_id_deque

    def _convert_orders_to_dict(self, orders):
        """
        this method creates a dictionary from the orders
        this dictionary is used for O(1) access for reporting
        """
        order_id_dict = {}
        for order in orders:
            order_id_dict[order.order_id] = copy.deepcopy(order)
        return order_id_dict

    def report_status(self, order_id):
        if order_id not in self.to_be_processed_dict:
            print("This order does not exist.")
            return False
        order = self.to_be_processed_dict[order_id]
        order_status = "TO BE PROCESSED"
        print(f"Order Type for order id: {order_id} is '{order.order_type}'")
        print(f"Order status: {order_status}")
        return True

    def add_order_to_be_processed(self, order):
        self.to_be_processed_deque.append(order.order_id)
        self.to_be_processed_dict[order.order_id] = copy.deepcopy(order)
