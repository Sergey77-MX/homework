import pytest

from src.processing import filter_by_currency


def test_filter_by_currency(transaction_list, usd_transaction):
    """Функция тестирует выдачу списка операций"""
    try:
        assert filter_by_currency(transaction_list, "USD") == usd_transaction
    except AssertionError:
        print("Введены некорректные данные")
