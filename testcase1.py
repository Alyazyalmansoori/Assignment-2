#!/usr/bin/env python
# coding: utf-8

# In[3]:


from Artwork import Artwork

# Define a function to test the addition of new artwork to the museum
def test_add_artwork_to_museum():
    # Create an instance of the Artwork class
    artwork = Artwork("1890 painting of Cairo’s Al Azhar University", "Zahra Fatima", "1503-01-01", "Iconic portrait", "Gallery 1")

    # Add the artwork to the museum (In this case, let's assume the museum has an artwork catalog)
    museum_artwork_catalog = []
    museum_artwork_catalog.append(artwork)

    # Check if the artwork is successfully added to the museum
    assert artwork in museum_artwork_catalog
    print("Artwork successfully added to the museum.")
    
    # Print the information of the added artwork
    print("Artwork Information:")
    print("Title:", artwork.get_title())
    print("Artist:", artwork.get_artist())
    print("Date of Creation:", artwork.get_date_of_creation())
    print("Historical Significance:", artwork.get_historical_significance())
    print("Exhibition Location:", artwork.get_exhibition_location())

# Run the test case
test_add_artwork_to_museum()


# In[ ]:




