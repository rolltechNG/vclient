"""
Helper function to process paystack transactions
Gotten from https://github.com/Chibuzor-IN/python-paystack
"""
from frontend.models import Price
from python_paystack.objects.transactions import Transaction
from python_paystack.managers import Transaction

NIN_PRICE = Price.nin_price
PHONE_PRICE = Price.phone_price
DEMO_PRICE = Price.demo_price


# PHONE_PRICE =
# DEMO_PRICE =
# EMAIL = {user's email}

def process_transaction():
    transaction = Transaction(NIN_PRICE, '{EMAIL}')
    # transaction = transaction_manager.initialize_transaction('STANDARD', transaction)
    pass
