#!/usr/bin/env python
# coding: utf-8

# In[3]:


from datetime import datetime
from Event import Event

# As exhibition is child class of Event
class Exhibition(Event):
    def __init__(self, exhibition_title, start_date, end_date, location):
        # Call the constructor of the parent class (Event)
        super().__init__(exhibition_title, start_date, end_date, location)
        
   # method to get the title of the exhibition
    def getExhibitionTitle(self):
        # Return the title of the exhibition
        return self.event_title

   # method to set the title of the exhibition
    def setExhibitionTitle(self, exhibition_title):
        # Set the title of the exhibition
        self.event_title = exhibition_title

   #method to get the start date
    def getStartDate(self):
        return self.startDate

  #method to set the start date
    def setStartDate(self, start_date):
        self.startDate = start_date

     #method to get the end date
    def getEndDate(self):
        return self.endDate

   #method to set the end date
    def setEndDate(self, end_date):
        self.endDate = end_date

     #method to get the location
    def getLocation(self):
        return self.location

    #method to set the location
    def setLocation(self, location):
        self.location = location


# In[ ]:




