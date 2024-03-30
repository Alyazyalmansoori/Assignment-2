#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Import the Visitor class
from Visitor import Visitor

# Create a visitor instance
visitor1 = Visitor("Mariam", 30, "123456789", "Adult")

# Test the getter methods
print("Visitor's Name:", visitor1.getName())  # Output should be "John Doe"
print("Visitor's Age:", visitor1.getAge())    # Output should be 30
print("Visitor's National ID:", visitor1.getNationalId())  # Output should be "123456789"
print("Visitor's Category:", visitor1.getVisitorCatagory())  # Output should be "Adult"

# Modify visitor information using setter methods
visitor1.setName("Mariam")
visitor1.setAge(75)
visitor1.setNationalId("987654321")
visitor1.setVisitorCatagory("Senior")

# Test the getter methods again to verify modifications
print("\nAfter modification:")
print("Visitor's Name:", visitor1.getName())  # Output should be "Jane Doe"
print("Visitor's Age:", visitor1.getAge())    # Output should be 35
print("Visitor's National ID:", visitor1.getNationalId())  # Output should be "987654321"
print("Visitor's Category:", visitor1.getVisitorCatagory())  # Output should be "Senior"


# In[ ]:




