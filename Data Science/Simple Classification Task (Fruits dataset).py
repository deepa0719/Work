#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

fruits = pd.read_table('fruit_data_with_colors.txt')


# In[2]:


fruits.head()


# In[3]:


lookup_fruit_name = dict(zip(fruits.fruit_label.unique(), fruits.fruit_name.unique()))
lookup_fruit_name


# ### Create Train-test split
# #### Basically for X given we will identify Y

# In[4]:


X = fruits[['mass','width','height', 'color_score']]
y = fruits['fruit_label']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
#random_state parameter provides a seed value to the function's internal random number generator.
#If we choose different values for that seed value, that will result in different randomized splits for training and testing data.


# ### Feature-Pair Plot for examining the data

# In[5]:


from matplotlib import cm

cmap = cm.get_cmap('gnuplot')
scatter = pd.plotting.scatter_matrix(X_train, c= y_train, marker = 'o', s=40, hist_kwds={'bins':15}, figsize=(6,6), cmap=cmap)


# ### 3D feature scatterplot

# In[6]:


# plotting a 3D scatter plot
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(X_train['width'], X_train['height'], X_train['color_score'], c= y_train, marker = 'o', s=100)
ax.set_xlabel('width')
ax.set_ylabel('height')
ax.set_zlabel('color_score')
plt.show()


# ### Create a Classifier Object

# In[7]:


from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors = 5)


# ### Train the Classifier using the training data

# In[8]:


knn.fit(X_train, y_train)


# ### Estimate the accuracy of the classifier on future data, using test data sets

# In[9]:


knn.score(X_test,y_test)


# ### Use the k-NN classifier model to classify previously unseen fruits

# In[10]:


fruit_prediction = knn.predict([[150,1.2,0.5,1]])
lookup_fruit_name[fruit_prediction[0]]


# In[11]:


fruit_prediction = knn.predict([[100,1.2,0.5,1]])
lookup_fruit_name[fruit_prediction[0]]


# In[12]:


fruit_prediction = knn.predict([[50,4.3,0.5,1]])
lookup_fruit_name[fruit_prediction[0]]


# ### Plot the decision boundary of the k-NN Classifier

# In[14]:


from adspy_shared_utilities import plot_fruit_knn
plot_fruit_knn(X_train, y_train, 5, 'uniform')


# In[ ]:




