#!/usr/bin/env python
# coding: utf-8

# In[4]:


class MuseumSystem:
    def __init__(self):
        # Initialize attributes
        self.artworks = []
        self.exhibitions = []
        self.visitorManager = None

    # lets create Method to add artwork
    def addArtwork(self, artwork):
        # Add the new artwork to the list of artworks
        self.artworks.append(artwork)
        print("Artwork added successfully.")

    #  # lets create Method to remove artwork
    def removeArtwork(self, artwork):
        if artwork in self.artworks:
            self.artworks.remove(artwork)
            print("Artwork removed successfully.")
        else:
            print("Artwork not found.")

    #  # lets create Method to view artwork
    def viewArtwork(self, artwork):
        print("Viewing artwork details:")
        if artwork in self.artworks:
            print("Artwork Title:", artwork.title)
            print("Artist:", artwork.artist)
            print("Date of Creation:", artwork.date_of_creation)
            print("Location:", artwork.exhibition_location)
            # Add more details as needed
        else:
            print("Artwork not found.")

    #  # lets create Method to add exhibition
    def addExhibition(self, exhibition):
        self.exhibitions.append(exhibition)
        print("Exhibition added successfully.")

    #  # lets create Method to remove exhibition
    def removeExhibition(self, exhibition):
        if exhibition in self.exhibitions:
            self.exhibitions.remove(exhibition)
            print("Exhibition removed successfully.")
        else:
            print("Exhibition not found.")

    # # lets create Method to view exhibition
    def viewExhibition(self, exhibition):
        print("Viewing exhibition details:")
        if exhibition in self.exhibitions:
            print("Exhibition Title:", exhibition.title)
            print("Start Date:", exhibition.start_date)
            print("End Date:", exhibition.end_date)
            print("Location:", exhibition.location)
            # Add more details as needed
        else:
            print("Exhibition not found.")

    # # lets create Method to register visit to a tour
    def registerVisitTour(self):
        print("Visit to tour registered.")


# In[ ]:




