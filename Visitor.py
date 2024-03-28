#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Visitor:
    def __init__(self, name, age, national_id):
        # Attributes
        self.name = name
        self.age = age
        self.national_id = national_id

    # Getter and setter methods for name
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    # Getter and setter methods for age
    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    # Getter and setter methods for nationalId
    def set_national_id(self, national_id):
        self.national_id = national_id

    def get_national_id(self):
        return self.national_id

    # Method for purchasing a ticket
    def purchase_ticket(self):
        # Implementation for purchasing a ticket
        pass


# In[ ]:




