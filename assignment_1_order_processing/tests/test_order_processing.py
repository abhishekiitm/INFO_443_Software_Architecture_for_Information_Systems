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
    assert order_processor.to_be_processed_deque \
        == deque([1])


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

    # Act
    order_processor = OrderProcessor(orders_to_be_processed)

    # Assert
    assert order_processor.report_status(1) is True
    assert order_processor.report_status(0) is False
