#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime

class Ticket:
    def __init__(self, ticket_type, price, purchase_date):
        # Attributes
        self.ticket_type = ticket_type
        self.price = price
        self.purchase_date = purchase_date

    # Getter and setter methods for ticketType
    def set_ticket_type(self, ticket_type):
        self.ticket_type = ticket_type

    def get_ticket_type(self):
        return self.ticket_type

    # Getter and setter methods for price
    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    # Method for calculating ticket price based on visitor's age
    def calculate_ticket_price(self, visitor):
        # Implementation for calculating ticket price based on visitor's age
        # For simplicity, returning a fixed price of 50 for now
        return 50.0

    # Method for applying VAT (Value Added Tax)
    def apply_vat(self):
        # Implementation for applying VAT to the ticket price
        self.price *= 1.05  # Assuming a 5% VAT rate

    # Getter and setter methods for purchaseDate
    def set_purchase_date(self, purchase_date):
        self.purchase_date = purchase_date

    def get_purchase_date(self):
        return self.purchase_date


# In[ ]:




