#!/usr/bin/env python
# coding: utf-8

# In[11]:


from Ticket import Ticket
from Visitor import Visitor
from Artwork import Artwork
from Tour import Tour

# let's Create a visitor using visitor class constructor instance
visitor1 = Visitor("Mariam", 20, "123456789", "Adult")

# let's Create an instance of the Tour class
tour = Tour("Hasan", "visit museum to attend artwork", 15, "2024-04-30")

# let's Create an instance of the Artwork class representing the main artwork in the tour
artwork = Artwork("Astrolabe", "Muhammad ibn Ahmad Al-Battuti", "1726", "Stories of Cultural Connections", "Permanent Galleries")

# let's Create a list to store discounted ticket prices
discounted_prices = []

# let's Create 15 tickets for the tour with a 50% discount and store the discounted prices
for i in range(15):
    ticket_price = 63  # Original ticket price
    discounted_price = ticket_price * 0.5  # Apply 50% discount
    discounted_prices.append(discounted_price)

# let's Calculate total price without VAT
total_price_without_vat = sum(discounted_prices)

# let's Calculate VAT (5% of the total price)
vat = total_price_without_vat * 0.05

# let's Calculate total price including VAT
total_price_with_vat = total_price_without_vat + vat

# Display payment receipt
print("Payment Receipt:")
print("Guide:", tour.getGuideName())
print("Number of visitors:", tour.getNumberOfVisitors())
print("Purpose:", tour.getPurpose())
print("Main Artwork in Tour:")
print("- Title:", artwork.getTitle())
print("- Artist:", artwork.getArtist())
print("- Location:", artwork.getExhibitionLocation())
print("Total Price after 50% discount (Excluding VAT) for 15 tickets:", total_price_without_vat)
print("VAT (5%):", vat)
print("Total Price (Including VAT) for 15 tickets:", total_price_with_vat)
print("Purchase Date:", "2024-03-28")  # Assuming all tickets are purchased at the same time


# In[ ]:




