#!/usr/bin/env python
# coding: utf-8

# In[11]:


from Artwork import Artwork

# Create an instance of the Artwork class
artwork = Artwork("1890 painting of Cairo’s Al Azhar University", "Mariam", "2024-03-27", "Iconic portrait", "Permanent Galleries")

# Add the artwork to the museum (In this case, let's assume the museum has an artwork catalog)
museum_artwork_catalog = []
museum_artwork_catalog.append(artwork)

# Check if the artwork is successfully added to the museum
assert artwork in museum_artwork_catalog
print("Artwork successfully added to the museum.")

# Print the information of the added artwork
print("Artwork Information:")
print("Title:", artwork.getTitle())
print("Artist:", artwork.getArtist())
print("Date of Creation:", artwork.getDateOfCreation())
print("Historical Significance:", artwork.getHistoricalSignificance())
print("Exhibition Location:", artwork.getExhibitionLocation())


# In[ ]:




