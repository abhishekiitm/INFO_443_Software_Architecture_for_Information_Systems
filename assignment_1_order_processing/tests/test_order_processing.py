import pytest
from ..order_processing import OrderType, Order, OrderProcessor
from collections import deque


def test_init_Order():
    # Arrange
    order_id = 1
    order_type = OrderType.BOOK
    properties_dict = {
        "title": "Snow Crash",
        "author": "Neal Stephenson",
        "price": 14.99,
        "no_items": 1
    }

    # Act
    order = Order(order_id, order_type, properties_dict)

    # Assert
    assert order.order_type == order_type


def test_init_OrderProcessing_deque():
    # Arrange
    order_id = 1
    order_type = OrderType.BOOK
    properties_dict = {
        "title": "Snow Crash",
        "author": "Neal Stephenson",
        "price": 14.99,
        "no_items": 1
    }
    order = Order(order_id, order_type, properties_dict)

    orders_to_be_processed = [order]

    # Act
    order_processor = OrderProcessor(orders_to_be_processed)

    # Assert
    assert order_processor.to_be_processed_deque == deque([1])


def test_init_OrderProcessing_dict():
    # Arrange
    order_id = 1
    order_type = OrderType.BOOK
    properties_dict = {
        "title": "Snow Crash",
        "author": "Neal Stephenson",
        "price": 14.99,
        "no_items": 1
    }
    order = Order(order_id, order_type, properties_dict)

    orders_to_be_processed = [order]

    # Act
    order_processor = OrderProcessor(orders_to_be_processed)

    # Assert
    assert order_processor.to_be_processed_dict[1].properties_dict \
        == properties_dict


def test_OrderProcessing_report_status():
    # Arrange
    order_id = 1
    order_type = OrderType.BOOK
    properties_dict = {
        "title": "Snow Crash",
        "author": "Neal Stephenson",
        "price": 14.99,
        "no_items": 1
    }
    order = Order(order_id, order_type, properties_dict)
    orders_to_be_processed = [order]
    order_processor = OrderProcessor(orders_to_be_processed)

    # Act
    result1 = order_processor.report_status(1)
    result0 = order_processor.report_status(0)

    # Assert
    assert result1 is True
    assert result0 is False


def test_OrderProcessing_add_order_to_be_processed():
    # Arrange
    order_id_1 = 1
    order_type_1 = OrderType.BOOK
    properties_dict_1 = {
        "title": "Snow Crash",
        "author": "Neal Stephenson",
        "price": 14.99,
        "no_items": 1
    }
    order_1 = Order(order_id_1, order_type_1, properties_dict_1)

    order_id_2 = 2
    order_type_2 = OrderType.MATERIAL
    properties_dict_2 = {
        "description": "Sand",
        "quantity": 2,
        "price": 5,
        "base_quantity": 1,
        "unit of measurement": "lbs"
    }
    order_2 = Order(order_id_2, order_type_2, properties_dict_2)

    orders_to_be_processed = [order_1]
    order_processor = OrderProcessor(orders_to_be_processed)

    # Act
    order_processor.add_order_to_be_processed(order_2)

    # Assert
    assert order_processor.to_be_processed_deque == deque([1, 2])
