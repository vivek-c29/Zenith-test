from order_system.application.services.checkout.processor import process_checkout

def test_process_checkout():
    items = [
        {"price": 100, "quantity": 2},
        {"price": 50, "quantity": 1},
    ]

    assert process_checkout(items) == "?250.00"
