#!/usr/bin/env python
# coding: utf-8

# In[6]:


'''Defining a class called Queue'''

class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return not bool(self.items)
    def enque(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def qsize(self):
        return len(self.items)
    def disp(self):
        return self.items


# In[7]:


'''calling the class through object'''
q = Queue()


# In[24]:


'''checking if the queue is empty'''
q.is_empty()


# In[25]:


q.enque(4)


# In[26]:


q.disp()


# In[22]:


q.enque('kiran')


# In[21]:


q.dequeue()


# In[27]:


q.qsize()


# In[42]:


'''Hot potato encoding'''

def Hpotato(names, num):
    queue = []
    for name in names:
        queue.insert(0,name)


    while len(queue)>1:
        for i in range(num):
            queue.insert(0,queue.pop())
            print(queue)
        queue.pop()
    return queue.pop()
        

    
    
Hpotato(['surya','kiran','udaya','kumar','arya','rahul'],9)


# In[ ]:




