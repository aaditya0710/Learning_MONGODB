#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymongo


# In[2]:


client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')


# In[3]:


mydb = client['Employee']


# In[4]:


information = mydb.employeeinformation


# In[5]:


record = {'firstname':"aaditya","lastname":"singh","department":"analytics"}


# In[6]:


information.insert_one(record)


# In[9]:


record = [{'firstname':"naman","lastname":"agarwal","department":"web dev"},{'firstname':"jatin","lastname":"puri","department":"UI&UX"}]


# In[10]:


information.insert_many(record)


# In[11]:


information.find_one()


# In[13]:


for record in information.find():
    print(record)


# In[16]:


for record in information.find({"department":"analytics"}):
    print(record)


# In[17]:


for record in information.find({'department':{'$in':['analytics','web dev']}}):
    print(record)


# In[20]:


for record in information.find({'$or':[{'firstname':'aaditya'},{'department':'web dev'}]}):
    print(record)


# In[21]:


#UPDATION OF PYTHON JSON DOCUMENTS


# In[23]:


import pymongo
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb = client['workers']
inventory = mydb.inventory


# In[24]:


inventory.insert_many([
    {"item": "canvas",
     "qty": 100,
     "size": {"h": 28, "w": 35.5, "uom": "cm"},
     "status": "A"},
    {"item": "journal",
     "qty": 25,
     "size": {"h": 14, "w": 21, "uom": "cm"},
     "status": "A"},
    {"item": "mat",
     "qty": 85,
     "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
     "status": "A"},
    {"item": "mousepad",
     "qty": 25,
     "size": {"h": 19, "w": 22.85, "uom": "cm"},
     "status": "P"},
    {"item": "notebook",
     "qty": 50,
     "size": {"h": 8.5, "w": 11, "uom": "in"},
     "status": "P"},
    {"item": "paper",
     "qty": 100,
     "size": {"h": 8.5, "w": 11, "uom": "in"},
     "status": "D"},
    {"item": "planner",
     "qty": 75,
     "size": {"h": 22.85, "w": 30, "uom": "cm"},
     "status": "D"},
    {"item": "postcard",
     "qty": 45,
     "size": {"h": 10, "w": 15.25, "uom": "cm"},
     "status": "A"},
    {"item": "sketchbook",
     "qty": 80,
     "size": {"h": 14, "w": 21, "uom": "cm"},
     "status": "A"},
    {"item": "sketch pad",
     "qty": 95,
     "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
     "status": "A"}])


# In[25]:


inventory.update_one({"item":"sketch pad"},{"$set":{"size.uom":"m","status":"P"},
"$currentDate":{"lastModified":True} })


# In[26]:


inventory.update_many(
    {"qty": {"$lt": 50}},
    {"$set": {"size.uom": "in", "status": "P"},
     "$currentDate": {"lastModified": True}})


# In[27]:


inventory.replace_one(
    {"item": "paper"},
    {"item": "paper",
     "instock": [
         {"warehouse": "A", "qty": 60},
         {"warehouse": "B", "qty": 40}]})


# In[ ]:




