#!/usr/bin/env python
# coding: utf-8

# In[5]:


from Ticket import Ticket
from Visitor import Visitor
from Event import Event

# Create a visitor using visitor class constructor instance
visitor1 = Visitor("Mariam", 20, "123456789", "Adult")

# Create an instance of the Exhibition class
event1= Event("MASQUERAVE", 1, 33, "Louvre Museum")
event2= Event("Film Screening: The Jungle Book", 1, 18, "Louvre Museum")

# Create tickets and associate them with the exhibition
ticket1 = Ticket("Adult", 63, "2024-03-28")
ticket2 = Ticket("Child", 0, "2024-03-28")

# Calculate total price including VAT
total_price_with_vat = ticket1.calculateTicketPrice(visitor) + ticket2.calculateTicketPrice(visitor)

# Display payment receipt
print("Payment Receipt:")
print("Visitor:", visitor.getName())
print("National ID:", visitor.getNationalId())
print("Visitor Category:", visitor.getVisitorCatagory())
print("Tickets Purchased:")
print("- Ticket Type:", ticket1.getTicketType(), "| Price (Including VAT):", ticket1.calculateTicketPrice(visitor))
print("  Event:", event1.getEventTitle(), "| Time:", event1.getDuration(), "| Location:", event1.getLocation())
print("- Ticket Type:", ticket2.getTicketType(), "| Price (Including VAT):", ticket2.calculateTicketPrice(visitor))
print("  Event:", event2.getEventTitle(), "| Time:", event2.getDuration(), "| Location:", event2.getLocation())
print("Total Price (Including VAT):", total_price_with_vat)
print("Purchase Date:", ticket1.getPurchaseDate())


# In[ ]:




