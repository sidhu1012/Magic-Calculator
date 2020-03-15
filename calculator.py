#!/usr/bin/env python
# coding: utf-8

# In[7]:


import re
print('calculator')
print("quit to exit")
previous=0
run=True


# In[12]:


def performMath():
    global run
    global previous
    eqn=''
    if previous==0:
        eqn=input('Equation:')
    else:
        eqn=input(str(previous))
    if eqn=='quit':
        run=False
    elif eqn=='clear':
        previous=0
    else:
        eqn=re.sub('[a-zA-Z,:;." "]','',eqn)
        if previous==0:
            previous=eval(eqn)
        else:
            previou=eval(str(previous)+eqn)
        
        print('you typed:',previous)
        
while run:
    performMath()


# In[ ]:




