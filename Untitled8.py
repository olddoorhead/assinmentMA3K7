#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[24]:


n = np.arange(0,100)
a_n = np.zeros_like(n, dtype = int)
a_n[0] = 1
a_n[1] = 5

for N in np.arange(2,100):
    an2= np.mod(a_n[N-2] + a_n[N-1], 10)
    a_n[N] = an2
    if a_n[N] == 5:
        if a_n[N-1] ==1:
            print(N-1)
print(a_n)


all_possible_pairs = set((i, j) for i in range(9) for j in range(9))
occurred_pairs = set((a_n[N], a_n[N-1]) for N in range(1, 60))

unseen_pairs = all_possible_pairs - occurred_pairs

print("Unseen Pairs:")
for i, j in sorted(unseen_pairs):
    print(i, j)


# In[23]:


n = np.arange(0,100)
a_n = np.zeros_like(n, dtype = int)
a_n[0] = 1
a_n[1] = 7

for N in np.arange(2,100):
    an2= np.mod(a_n[N-2] + a_n[N-1], 10)
    a_n[N] = an2
    if a_n[N] == 7:
        if a_n[N-1] ==1:
            print(N-1)
print(a_n)


# In[ ]:




