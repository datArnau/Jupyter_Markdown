#!/usr/bin/env python
# coding: utf-8

# # Exercicis en Python

# ### Exercici amb gestió de llistes

# In[8]:


nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)


# ### Exercici amb fucions que retornen valors

# In[9]:


def max(x,y):
    if x > y:
        return x
    else:
        return y

print(max(4,6))

z=max(10, 12)
print(z)


# ### Exercici amb herencies

# In[10]:


class A:
    def method(self):
        print("A method")
    
class B(A):
    def another_method(self):
        print("B method")
    
class C(B):
    def third_method(self):
        print("C method")
    
c = C()
c.method()
c.another_method()
c.third_method()


# ## Inserció d'una imatge:

# ![1_E1haIGB9K4K89PsFZgm-pw.jpeg](attachment:1_E1haIGB9K4K89PsFZgm-pw.jpeg)# 

# In[12]:


pip install jupyter_contrib_nbextensions


# In[ ]:




