#!/usr/bin/env python
# coding: utf-8

# In[1]:


class MuseumSystem:
    #constructor to intialize values
    def __init__(self, artwork_catalog):
        # Attributes
        self.artwork_catalog = artwork_catalog
        self.visitor_manager = VisitorManager()  # Initialize with a new VisitorManager instance

    # Getter and setter methods for artworkCatalog
    def get_artwork_catalog(self):
        return self.artwork_catalog

    def set_artwork_catalog(self, artwork_catalog):
        self.artwork_catalog = artwork_catalog

    # Getter and setter methods for visitorManager
    def get_visitor_manager(self):
        return self.visitor_manager

    def set_visitor_manager(self, visitor_manager):
        self.visitor_manager = visitor_manager

    # Methods
    def set_exhibition_schedule(self):
        # Implementation for setting exhibition schedule
        return "Exhibition schedule set successfully."

    def view_exhibition_schedule(self):
        # Implementation for viewing exhibition schedule
        return "Exhibition schedule viewed successfully."


class VisitorManager:
    def __init__(self):
        # Initialization of visitor manager
        pass


# In[ ]:





# In[ ]:




