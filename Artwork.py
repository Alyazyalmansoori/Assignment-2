#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance, exhibition_location):
        # Attributes
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.exhibition_location = exhibition_location

    # Getter and setter methods for title
    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    # Getter and setter methods for artist
    def set_artist(self, artist):
        self.artist = artist

    def get_artist(self):
        return self.artist

    # Getter and setter methods for dateOfCreation
    def set_date_of_creation(self, date_of_creation):
        self.date_of_creation = date_of_creation

    def get_date_of_creation(self):
        return self.date_of_creation

    # Getter and setter methods for historicalSignificance
    def set_historical_significance(self, historical_significance):
        self.historical_significance = historical_significance

    def get_historical_significance(self):
        return self.historical_significance

    # Getter and setter methods for exhibitionLocation
    def set_exhibition_location(self, exhibition_location):
        self.exhibition_location = exhibition_location

    def get_exhibition_location(self):
        return self.exhibition_location


# In[ ]:




