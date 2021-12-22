#!/usr/bin/env python
# coding: utf-8

# (assignment04)=
# 
# # Assignment #4 (demo). Exploring OLS, Lasso and Random Forest in a regression task
# 
# <img src="https://habrastorage.org/webt/ia/m9/zk/iam9zkyzqebnf_okxipihkgjwnw.jpeg" />
# 
# Author: [Yury Kashnitsky](https://www.linkedin.com/in/festline/). All content is distributed under the [Creative Commons CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license.
# 
# **Same assignment as a [Kaggle Notebook](https://www.kaggle.com/kashnitsky/a6-demo-linear-models-and-rf-for-regression) + [solution](https://www.kaggle.com/kashnitsky/a6-demo-regression-solution).**  
# 
# ```{figure} /_static/img/wine_quality.jpg
# :width: 444px
# ```
# 
# **Fill in the missing code and choose answers in [this](https://docs.google.com/forms/d/1aHyK58W6oQmNaqEfvpLTpo6Cb0-ntnvJ18rZcvclkvw/edit) web form.**

# In[1]:


import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Lasso, LassoCV, LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import (GridSearchCV, cross_val_score,
                                     train_test_split)
from sklearn.preprocessing import StandardScaler


# **We are working with UCI Wine quality dataset (no need to download it – it's already there, in course repo and in Kaggle Dataset).**

# In[2]:


# for Jupyter-book, we copy data from GitHub, locally, to save Internet traffic,
# you can specify the data/ folder from the root of your cloned
# https://github.com/Yorko/mlcourse.ai repo, to save Internet traffic
DATA_PATH = "https://raw.githubusercontent.com/Yorko/mlcourse.ai/master/data/"


# In[3]:


data = pd.read_csv(DATA_PATH + "winequality-white.csv", sep=";")


# In[4]:


data.head()


# In[5]:


data.info()


# **Separate the target feature, split data in 7:3 proportion (30% form a holdout set, use random_state=17), and preprocess data with `StandardScaler`.**

# In[6]:


# y = None

# X_train, X_holdout, y_train, y_holdout = train_test_split
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform
# X_holdout_scaled = scaler.transform


# ## Linear regression
# 
# **Train a simple linear regression model (Ordinary Least Squares).**

# In[7]:


# (read-only in a JupyterBook, pls run jupyter-notebook to edit)
# linreg =
# linreg.fit


# **<font color='red'>Question 1:</font> What are mean squared errors of model predictions on train and holdout sets?**

# In[8]:


# (read-only in a JupyterBook, pls run jupyter-notebook to edit)
# print("Mean squared error (train): %.3f"
# print("Mean squared error (test): %.3f" %


# **Sort features by their influence on the target feature (wine quality). Beware that both large positive and large negative coefficients mean large influence on target. It's handy to use `pandas.DataFrame` here.**
# 
# **<font color='red'>Question 2:</font> Which feature this linear regression model treats as the most influential on wine quality?**

# In[9]:


# (read-only in a JupyterBook, pls run jupyter-notebook to edit)
# linreg_coef = pd.DataFrame
# linreg_coef.sort_values


# ## Lasso regression
# 
# **Train a LASSO model with $\alpha = 0.01$ (weak regularization) and scaled data. Again, set random_state=17.**

# In[10]:


# (read-only in a JupyterBook, pls run jupyter-notebook to edit)
# lasso1 = Lasso
# lasso1.fit


# **Which feature is the least informative in predicting wine quality, according to this LASSO model?**

# In[11]:


# (read-only in a JupyterBook, pls run jupyter-notebook to edit)
# lasso1_coef = pd.DataFrame
# lasso1_coef.sort_values


# **Train LassoCV with random_state=17 to choose the best value of $\alpha$ in 5-fold cross-validation.**

# In[12]:


# (read-only in a JupyterBook, pls run jupyter-notebook to edit)
# alphas = np.logspace(-6, 2, 200)
# lasso_cv = LassoCV
# lasso_cv.fit


# In[13]:


# lasso_cv.alpha_


# **<font color='red'>Question 3:</font> Which feature is the least informative in predicting wine quality, according to the tuned LASSO model?**

# In[14]:


# (read-only in a JupyterBook, pls run jupyter-notebook to edit)
# lasso_cv_coef = pd.DataFrame
# lasso_cv_coef.sort_values


# **<font color='red'>Question 4:</font> What are mean squared errors of tuned LASSO predictions on train and holdout sets?**

# In[15]:


# (read-only in a JupyterBook, pls run jupyter-notebook to edit)
# print("Mean squared error (train): %.3f"
# print("Mean squared error (test): %.3f" %


# ## Random Forest
# 
# **Train a Random Forest with out-of-the-box parameters, setting only random_state to be 17.**

# In[16]:


# (read-only in a JupyterBook, pls run jupyter-notebook to edit)
# forest = RandomForestRegressor
# forest.fit


# **<font color='red'>Question 5:</font> What are mean squared errors of RF model on the training set, in cross-validation (cross_val_score with scoring='neg_mean_squared_error' and other arguments left with default values) and on holdout set?**

# In[17]:


# (read-only in a JupyterBook, pls run jupyter-notebook to edit)
# print("Mean squared error (train): %.3f" %
# print("Mean squared error (cv): %.3f" %
# print("Mean squared error (test): %.3f" %


# **Tune the `max_features` and `max_depth` hyperparameters with GridSearchCV and again check mean cross-validation MSE and MSE on holdout set.**

# In[18]:


# (read-only in a JupyterBook, pls run jupyter-notebook to edit)
# forest_params = {'max_depth': list(range(10, 25)),
#                  'min_samples_leaf': list(range(1, 8)),
#                  'max_features': list(range(6,12))}

# locally_best_forest = GridSearchCV
# locally_best_forest.fit


# In[19]:


# locally_best_forest.best_params_, locally_best_forest.best_score_


# **<font color='red'>Question 6:</font> What are mean squared errors of tuned RF model in cross-validation (cross_val_score with scoring='neg_mean_squared_error' and other arguments left with default values) and on holdout set?**

# In[20]:


# (read-only in a JupyterBook, pls run jupyter-notebook to edit)
# print("Mean squared error (cv): %.3f" %
# print("Mean squared error (test): %.3f" %


# **Output RF's feature importance. Again, it's nice to present it as a DataFrame.**<br>
# **<font color='red'>Question 7:</font> What is the most important feature, according to the Random Forest model?**

# In[21]:


# (read-only in a JupyterBook, pls run jupyter-notebook to edit)
# rf_importance = pd.DataFrame  
# rf_importance.sort_values  


# **Make conclusions about the perdormance of the explored 3 models in this particular prediction task.**
