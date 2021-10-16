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

        # create empty deque and dictionary to store orders to be processed
        self.to_be_processed_deque = deque()
        self.to_be_processed_dict = {}

        # loop through orders, validate and add them to be processed
        for order in orders_to_be_processed:
            if not self._validate_items(order):
                continue
            self.add_order_to_be_processed(order)

    def report_status(self, order_id):
        """
        prints the order type and status of the order
        """
        if order_id not in self.to_be_processed_dict:
            print(f"Order id: {order_id} does not exist")
            return False
        order = self.to_be_processed_dict[order_id]
        order_status = "TO BE PROCESSED"
        print(f"Order Type for order id: {order_id} is '{order.order_type}'")
        print(f"Order status: {order_status}")
        return True

    def add_order_to_be_processed(self, order):
        """
        adds an order to the list of order to be processed
        """
        self.to_be_processed_deque.append(order.order_id)
        self.to_be_processed_dict[order.order_id] = copy.deepcopy(order)

    def edit_order(self, order):
        order_id = order.order_id
        if order_id not in self.to_be_processed_dict:
            print(f"Order id: {order_id} does not exist")
            return False
        # update order details
        self.to_be_processed_dict[order_id] = copy.deepcopy(order)

        # restart the to to be processed process
        self.to_be_processed_deque.remove(order_id)
        self.to_be_processed_deque.append(order_id)
        if not self._validate_items(order):
            self.to_be_processed_deque.pop()
            self.to_be_processed_dict.pop(order_id)

    def _validate_items(self, order):
        """
        checks if the no of items of an order are valid or not
        """
        if order.order_type == OrderType.BOOK:
            if order.properties_dict['no_items'] <= 0:
                return False
        if order.order_type == OrderType.MATERIAL:
            if order.properties_dict['quantity'] <= 0:
                return False
        if order.order_type == OrderType.FOOD:
            if order.properties_dict['quantity'] <= 0:
                return False
        return True

    def _calculate_cost(self, order):
        properties = order.properties_dict
        if order.order_type == OrderType.BOOK:
            return properties['no_items'] * properties['price']
        if order.order_type == OrderType.MATERIAL:
            return properties['quantity'] * properties['price'] / \
                properties['base_quantity']
        if order.order_type == OrderType.FOOD:
            return properties['quantity'] * properties['price'] / \
                properties['base_quantity']
        return 0

    def process_order(self):
        """
        processes the first order in the queue waiting to be processed
        """
        if len(self.to_be_processed_deque) == 0:
            return
        order_id = self.to_be_processed_deque.popleft()
        order = self.to_be_processed_dict.pop(order_id)
        cost = self._calculate_cost(order)
        print(f"Processed order id: {order_id}, cost = {cost}")
