#!/usr/bin/env python
# coding: utf-8

# In[2]:


# lets import datetime to handle date
from datetime import datetime

class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance, exhibition_location):
        # Initialize attributes
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.exhibition_location = exhibition_location

      # lets create Method to title of the artwork
    def getTitle(self):
        # Return the title of the artwork
        return self.title

 # lets create Method to get the artist of the artwork
    def getArtist(self):
        # Return the artist of the artwork
        return self.artist

# lets create Method to get the date of creation of the artwork
    def getDateOfCreation(self):
        # Return the date of creation of the artwork
        return self.date_of_creation

# lets create Method to get the historical significance of the artwork
    def getHistoricalSignificance(self):
        # Return the historical significance of the artwork
        return self.historical_significance

# lets create Method to get the exhibition location of the artwork
    def getExhibitionLocation(self):
        # Return the exhibition location of the artwork
        return self.exhibition_location

# lets create Method to set the title of the artwork
    def setTitle(self, title):
        # Set the title of the artwork
        self.title = title

 # lets create Method to set the artist of the artwork
    def setArtist(self, artist):
        # Set the artist of the artwork
        self.artist = artist

# lets create Method to set the date of creation of the artwork
    def setDateOfCreation(self, date_of_creation):
        # Set the date of creation of the artwork
        self.date_of_creation = date_of_creation

# lets create Method to set the historical significance of the artwork
    def setHistoricalSignificance(self, historical_significance):
        # Set the historical significance of the artwork
        self.historical_significance = historical_significance

# lets create Method to set the exhibition location of the artwork
    def setExhibitionLocation(self, exhibition_location):
        # Set the exhibition location of the artwork
        self.exhibition_location = exhibition_location



# In[ ]:




