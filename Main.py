#!/usr/bin/env python
# coding: utf-8

# In[30]:


from datetime import datetime
from Artwork import Artwork
from Exhibition import Exhibition
from Visitor import Visitor
from Ticket import Ticket
from Tour import Tour
from museumsystem import MuseumSystem


# In[31]:


# Create instances of Artwork
artwork1 = Artwork("Lion", "Abdullah", datetime(1503, 1, 1), "Iconic portrait", "Gallery 1")
artwork2 = Artwork("Fox", "Maryam", datetime(1889, 1, 1), "Symbolic landscape", "Gallery 2")

# Create an instance of Exhibition
exhibition = Exhibition()
exhibition.set_exhibition_schedule("January 2024 - March 2024")

# Create an instance of Visitor
visitor = Visitor("Alyazy", 20, "123456789")

# Create an instance of Ticket
ticket = Ticket("Regular", 50, datetime.now())

# Create an instance of Tour
tour = Tour()
tour.set_guide("Tour Guide")
tour.set_route("Main Gallery")
tour.set_number_of_visitors(10)

# Create an instance of MuseumSystem
museum_system = MuseumSystem("Main Catalog")
museum_system.exhibition = exhibition

# Print information of all instances
print("Artwork 1 Information:")
print("Title:", artwork1.title)
print("Artist:", artwork1.artist)
print("Date of Creation:", artwork1.date_of_creation)
print("Historical Significance:", artwork1.historical_significance)
print("Exhibition Location:", artwork1.exhibition_location)
print()

print("Artwork 2 Information:")
print("Title:", artwork2.title)
print("Artist:", artwork2.artist)
print("Date of Creation:", artwork2.date_of_creation)
print("Historical Significance:", artwork2.historical_significance)
print("Exhibition Location:", artwork2.exhibition_location)
print()

print("Exhibition Information:")
print("Exhibition Schedule:", exhibition.exhibition_schedule)
print("Artworks in Exhibition:")
for artwork in exhibition.artworks:
    print("Title:", artwork.title)
    print("Artist:", artwork.artist)
    print("Date of Creation:", artwork.date_of_creation)
    print("Historical Significance:", artwork.historical_significance)
    print("Exhibition Location:", artwork.exhibition_location)
    print()

print("Visitor Information:")
print("Name:", visitor.name)
print("Age:", visitor.age)
print("National ID:", visitor.national_id)
print()

print("Ticket Information:")
print("Ticket Type:", ticket.ticket_type)
print("Price:", ticket.price)
print("Purchase Date:", ticket.purchase_date)
print()

print("Tour Information:")
print("Guide:", tour.guide)
print("Route:", tour.route)
print("Number of Visitors:", tour.number_of_visitors)
print()

print("Museum System Information:")
print("Artwork Catalog:", museum_system.artwork_catalog)
print("Exhibition Schedule:", museum_system.exhibition.exhibition_schedule)
print("Artworks in Exhibition:")
for artwork in museum_system.exhibition.artworks:
    print("Title:", artwork.title)
    print("Artist:", artwork.artist)
    print("Date of Creation:", artwork.date_of_creation)
    print("Historical Significance:", artwork.historical_significance)
    print("Exhibition Location:", artwork.exhibition_location)
    print()


# In[ ]:




