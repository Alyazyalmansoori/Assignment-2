#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime, timedelta

class Event:
    def __init__(self, event_title, hours, minutes, location):
        self.event_title = event_title
        self.duration = timedelta(hours=hours, minutes=minutes)
        self.location = location

#let's create method to get event title
    def getEventTitle(self):
        return self.event_title
    
    #let's create method to get event duration

    def getDuration(self):
        hours, minutes = divmod(self.duration.seconds // 60, 60)
        return f"{hours} h {minutes} min"

  #let's create method to get event location
    def getLocation(self):
        return self.location

    #let's create method to set event title
    def setEventTitle(self, event_title):
        self.event_title = event_title
 #let's create method to set event duration
    def setDuration(self, hours, minutes):
        self.duration = timedelta(hours=hours, minutes=minutes)
        self.end_date = self.start_date + self.duration

        #let's create method to set event location
    def setLocation(self, location):
        self.location = location


# In[ ]:




