#!/usr/bin/env python
# coding: utf-8

# ## Notebookforin
# 
# null

# In[1]:


import requests
import pandas as pd
from io import StringIO

url = "https://raw.githubusercontent.com/harshavenkatasai/Amazon-Sales-2025/refs/heads/main/amazon_sales_data%202025.csv"
response = requests.get(url)


# In[2]:


df = pd.read_csv(StringIO(response.text))
display(df)


# In[3]:


dfcopy=df.copy()


# In[4]:


display(dfcopy)
dfcopy=spark.createDataFrame(dfcopy)


# In[5]:


dfcopy.describe()


# In[6]:


type(dfcopy)


# In[9]:


dfcopy.toPandas().to_csv("Files/Amazonfiles", index=False)

print("Saved successfully!")


# In[11]:


dfcopy.write.mode("overwrite").format("parquet").save(
    "abfss://d5d0881b-c9b1-4da9-96df-3c27af8b9a02@onelake.dfs.fabric.microsoft.com/acf1c72a-22d0-4fe0-82ae-265f45be6ee0/Files/Amazonfiles"
)
#dont use


# In[12]:


dfcopy.coalesce(1).write.mode("overwrite").format("parquet").save(
    "abfss://d5d0881b-c9b1-4da9-96df-3c27af8b9a02@onelake.dfs.fabric.microsoft.com/acf1c72a-22d0-4fe0-82ae-265f45be6ee0/Files/Amazonfiles"
)
print("Saved as single file!")

