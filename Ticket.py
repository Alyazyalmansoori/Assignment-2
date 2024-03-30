#!/usr/bin/env python
# coding: utf-8

# In[1]:


#lets import datetime
from datetime import datetime

class Ticket:
    def __init__(self, ticket_type, price, purchase_date):
        # Initialize attributes
        self.ticket_type = ticket_type  # Type of ticket (e.g., General, VIP)
        self.price = price  # Price of the ticket
        self.purchase_date = purchase_date  # Date when the ticket was purchased

  #lets create method to get ticket type
    def getTicketType(self):
        # Return the type of ticket
        return self.ticket_type

  #lets create method to get the purchase date of the ticket
    def getPurchaseDate(self):
        # Return the purchase date of the ticket
        return self.purchase_date

  #lets create method to set ticket type
    def setTicketType(self, ticket_type):
        # Set the type of ticket
        self.ticket_type = ticket_type

 #lets create method to set the purchase date of the ticket
    def setPurchaseDate(self, purchase_date):
        # Set the purchase date of the ticket
        self.purchase_date = purchase_date

    # lets create Method to calculate the ticket price based on visitor information
    def calculateTicketPrice(self, visitor):
        ticket_price = float(self.price)  # Assuming the price is in float format
        
        # Apply VAT (Value Added Tax)
        vat_rate = 0.05  # 5% VAT rate
        ticket_price_with_vat = ticket_price * (1 + vat_rate)  # Add VAT to the ticket price
        
        return ticket_price_with_vat


# In[ ]:




