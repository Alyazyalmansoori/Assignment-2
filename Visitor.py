#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Visitor:
    def __init__(self, name, age, national_id, visitor_category):
        # Initialize attributes
        self.name = name  # Visitor's name
        self.age = age  # Visitor's age
        self.national_id = national_id  # Visitor's national ID
        self.visitor_category = visitor_category  # Visitor's category (e.g., Adult, Child, Senior)

# lets create method to get the visitor's name
    def getName(self):
        # Return the visitor's name
        return self.name

# lets create method to get the the visitor's age
    def getAge(self):
        # Return the visitor's age
        return self.age

# lets create method to get the visitor's national ID
    def getNationalId(self):
        # Return the visitor's national ID
        return self.national_id

# lets create method to get the visitor's category
    def getVisitorCatagory(self):
        # Return the visitor's category
        return self.visitor_category

# lets create method to set the visitor's name
    def setName(self, name):
        # Set the visitor's name
        self.name = name

# lets create method to set the visitor's age
    def setAge(self, age):
        # Set the visitor's age
        self.age = age

# lets create method to set the visitor's national ID
    def setNationalId(self, national_id):
        # Set the visitor's national ID
        self.national_id = national_id

# lets create method to set the visitor's category
    def setVisitorCatagory(self, visitor_category):
        # Set the visitor's category
        self.visitor_category = visitor_category

# lets create method to purchase a ticket
    def PurchaseTicket(self):
        pass  # Placeholder for the actual implementation


# In[ ]:




