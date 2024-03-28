#!/usr/bin/env python
# coding: utf-8

# In[45]:


from datetime import datetime
from Artwork import Artwork
from Exhibition import Exhibition
from Visitor import Visitor
from Ticket import Ticket
from Tour import Tour
from museumsystem import MuseumSystem
# Test case 3.2 implementation
ticket1 = Ticket("Regular", 50, datetime.now())
ticket2 = Ticket("VIP", 100, datetime.now())

# Create instances of Artwork
artwork1 = Artwork("Lion", "Abdullah", datetime(1503, 1, 1), "Iconic portrait", "Gallery 1")
artwork2 = Artwork("Fox", "Maryam", datetime(1889, 1, 1), "Symbolic landscape", "Gallery 2")

# Displaying payment receipt with artwork details
payment_receipt = f"Payment Receipt:\nTicket 1:  {ticket1.get_price()} - {artwork1.get_title()}, {artwork1.get_artist()}, {artwork1.get_date_of_creation()}, {artwork1.get_historical_significance()}, {artwork1.get_exhibition_location()}\nTicket 2: {ticket2.get_price()} - {artwork2.get_title()}, {artwork2.get_artist()}, {artwork2.get_date_of_creation()}, {artwork2.get_historical_significance()}, {artwork2.get_exhibition_location()}\nTotal Price: {ticket1.get_price() + ticket2.get_price()}"

print(payment_receipt)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




