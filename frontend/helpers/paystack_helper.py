"""
Helper function to process paystack transactions
Gotten from https://github.com/Chibuzor-IN/python-paystack
"""
from frontend.models import Price
price = Price.objects.query
NIN_PRICE = Price.objects.get(id=1)


# PHONE_PRICE =
# DEMO_PRICE =
# EMAIL = {user's email}

def process_transaction():
    # transaction = Transaction(nin_price, '{EMAIL}')
    # transaction = transaction_manager.initialize_transaction('STANDARD', transaction)
    pass
