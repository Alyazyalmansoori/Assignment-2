#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime

class Event:
    def __init__(self, title, duration, location):
        # Attributes
        self.title = title
        self.duration = duration
        self.location = location

    # Getter and setter methods for title
    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    # Getter and setter methods for duration
    def set_duration(self, duration):
        self.duration = duration

    def get_duration(self):
        return self.duration

    # Getter and setter methods for location
    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location


# In[ ]:




