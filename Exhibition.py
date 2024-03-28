#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Exhibition:
    def __init__(self):
        # Attributes
        self.artworks = []  #list to store python file
        self.exhibition_schedule = ""  

    # Method for scheduling the exhibition
    def schedule_exhibition(self):
        # Implementation for scheduling the exhibition
        pass

    # Method for setting artworks
    def set_artworks(self, artworks):
        self.artworks = artworks

    # Method for getting artworks
    def get_artworks(self):
        return self.artworks

    # Method for setting the exhibition schedule
    def set_exhibition_schedule(self, exhibition_schedule):
        self.exhibition_schedule = exhibition_schedule

    # Method for getting the exhibition schedule
    def get_exhibition_schedule(self):
        return self.exhibition_schedule

