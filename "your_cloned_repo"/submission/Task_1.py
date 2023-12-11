#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
df=pd.read_csv("E:\Data Analysis Resourses\dataset-1.csv",header=0)


# In[24]:


#question1


# In[30]:


import pandas as pd

def generate_car_matrix(df):
    
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    
   
    for i in car_matrix.index:
        car_matrix.at[i, i] = 0
    
    return car_matrix


result_matrix = generate_car_matrix(df)


print(result_matrix)


# In[33]:


#question2


# In[34]:


import pandas as pd

def get_type_count(df):
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')], labels=['low', 'medium', 'high'], right=False)
    
   
    type_counts = df['car_type'].value_counts().to_dict()
    
   
    sorted_type_counts = dict(sorted(type_counts.items()))
    
    return sorted_type_counts


result_type_count = get_type_count(df)


print(result_type_count)


# In[ ]:


#question3


# In[35]:


import pandas as pd

def get_bus_indexes(df):
    bus_mean = df['bus'].mean()
    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()
    bus_indexes.sort()
    
    return bus_indexes
result_bus_indexes = get_bus_indexes(df)
print(result_bus_indexes)


# In[ ]:


#question4


# In[36]:


import pandas as pd

def filter_routes(df):
    route_avg_truck = df.groupby('route')['truck'].mean()
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()
    selected_routes.sort()
    
    return selected_routes
result_filtered_routes = filter_routes(df)
print(result_filtered_routes)


# In[37]:


#question5


# In[38]:


def multiply_matrix(result_matrix):
    modified_matrix = result_matrix.copy()
    modified_matrix = modified_matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    modified_matrix = modified_matrix.round(1)

    return modified_matrix

modified_result_matrix = multiply_matrix(result_matrix)

print(modified_result_matrix)


# In[39]:


#question6


# In[11]:


import pandas as pd
df=pd.read_csv("E:\Data Analysis Resourses\dataset-2.csv",header=0)


# In[23]:


import pandas as pd

def verify_timestamps(df):
    try:
        df['start_timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
        df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])
        df['day_of_week'] = df['start_timestamp'].dt.dayofweek

        result_series = df.groupby(['id', 'id_2']).apply(lambda group: (
            (group['start_timestamp'].min().time() == pd.Timestamp('00:00:00').time()) and
            (group['end_timestamp'].max().time() == pd.Timestamp('23:59:59').time()) and
            (group['day_of_week'].nunique() == 7)
        )).all(level=['id', 'id_2'])

        return result_series

    except pd.errors.OutOfBoundsDatetime as e:
        print(f"Error: {e}")
        problematic_rows = df[df.isna().any(axis=1)]
        print("Problematic rows:")
        print(problematic_rows)
        return pd.Series(dtype=bool) 

result_series = verify_timestamps(df)

print(result_series)


# In[ ]:




