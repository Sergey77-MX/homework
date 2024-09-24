def filter_by_currency(transactions, code = "USD"):
    if len(transactions) > 0:
        for transaction in transactions:
            if transaction["operationAmount"]["currency"]["code"] == code:
                yield transaction
    elif len(transactions) < 0:
        raise StopIteration("Ввели пустой список")