#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df=pd.read_csv("E:\Data Analysis Resourses\dataset-3.csv",header=0)


# In[3]:


pip install geopy


# In[11]:


#question:1


# In[50]:


import pandas as pd

def calculate_distance_matrix(df):
    unique_ids = pd.concat([df['id_start'], df['id_end']]).unique()
    distance_matrix = pd.DataFrame(index=unique_ids, columns=unique_ids, dtype=float)
    distance_matrix.values[[range(len(unique_ids))]*2] = 0
    for index, row in df.iterrows():
        id_start, id_end, distance = row['id_start'], row['id_end'], row['distance']

        distance_matrix.at[id_start, id_end] += distance
        distance_matrix.at[id_end, id_start] += distance

    return distance_matrix


result_distance_matrix = calculate_distance_matrix(df)

print(result_distance_matrix)


# In[13]:


#question:2


# In[54]:


import pandas as pd

def unroll_distance_matrix(distance_matrix):
    unrolled_data = []

    for i in range(len(distance_matrix.index)):
        for j in range(i + 1, len(distance_matrix.columns)):
            id_start = distance_matrix.index[i]
            id_end = distance_matrix.columns[j]
            distance = distance_matrix.at[id_start, id_end]

            unrolled_data.append({'id_start': id_start, 'id_end': id_end, 'distance': distance})

    unrolled_df = pd.DataFrame(unrolled_data)

    return unrolled_df

result_unrolled_df = unroll_distance_matrix(result_distance_matrix)

print(result_unrolled_df)


# In[20]:


#question3


# In[21]:


import pandas as pd

def find_ids_within_ten_percentage_threshold(df, reference_value):

    reference_data = df[df['id_start'] == reference_value]

    reference_average_distance = reference_data['distance'].mean()
    lower_threshold = reference_average_distance - 0.1 * reference_average_distance
    upper_threshold = reference_average_distance + 0.1 * reference_average_distance

    within_threshold_df = df[(df['distance'] >= lower_threshold) & (df['distance'] <= upper_threshold)]

    result_ids = within_threshold_df['id_start'].unique()
    result_ids.sort()

    return result_ids.tolist()

reference_value = 1001402

result_ids_within_threshold = find_ids_within_ten_percentage_threshold(unrolled_df, reference_value)

print(result_ids_within_threshold)


# In[22]:


#question 4


# In[55]:


import pandas as pd

def calculate_toll_rate(df):
    df_with_rates = df.copy()

    rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }

    for vehicle_type, rate_coefficient in rate_coefficients.items():
        column_name = vehicle_type + '_rate'
        df_with_rates[column_name] = df_with_rates['distance'] * rate_coefficient

    return df_with_rates

unrolled_df.reset_index(drop=True, inplace=True)

df_with_rates = calculate_toll_rate(unrolled_df)
print(df_with_rates)


# In[44]:


#question5
df=pd.read_csv("E:\Data Analysis Resourses\excel.csv",header=0)


# In[49]:


import pandas as pd
from datetime import datetime, timedelta, time
df=pd.read_csv("E:\Data Analysis Resourses\excel.csv",header=0)

df.head()


# In[ ]:




