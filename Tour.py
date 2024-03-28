#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Tour:
    def __init__(self):
        # Attributes
        self.guide = ""
        self.route = ""
        self.number_of_visitors = 3  # Initialize with the value 3

    # Getter and setter methods for guide
    def set_guide(self, guide):
        self.guide = guide

    def get_guide(self):
        return self.guide

    # Getter and setter methods for route
    def set_route(self, route):
        self.route = route

    def get_route(self):
        return self.route

    # Getter and setter methods for number_of_visitors
    def set_number_of_visitors(self, number_of_visitors):
        self.number_of_visitors = number_of_visitors

    def get_number_of_visitors(self):
        return self.number_of_visitors


# In[ ]:




