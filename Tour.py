#!/usr/bin/env python
# coding: utf-8

# In[2]:


#lets import event class
from Event import Event

# Tour is child class of event
class Tour(Event):
    def __init__(self, guide_name, purpose, num_of_visitors, date):
        # Call the constructor of the parent class (Event)
        super().__init__("Tour", 0, 0, "")  # Not using parent attributes, passing dummy values
        # Attributes specific to Tour
        self.guideName = guide_name
        self.purpose = purpose
        self.numberOfVisitors = num_of_visitors

   #lets create a method to get guide name
    def getGuideName(self):
        return self.guideName

  #lets create a method to set guide name
    def setGuideName(self, guide_name):
        self.guideName = guide_name

 #lets create a method to get purpose for tour
    def getPurpose(self):
        return self.purpose

#lets create a method to set purpose for tour
    def setPurpose(self, purpose):
        self.purpose = purpose

  #lets create a method to get the number of visitors
    def getNumberOfVisitors(self):
        return self.numberOfVisitors

     #lets create a method to set the number of visitors
    def setNumberOfVisitors(self, num_of_visitors):
        self.numberOfVisitors = num_of_visitors

  #lets create a method to get date
    def getDate(self):
        return self.date

  #lets create a method to set date
    def setDate(self, date):
        self.date = date


# In[ ]:




