#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import csv


# In[3]:


data=[]


# In[4]:


with open(r"C:\Users\dell\Downloads\mysheet_numpy.csv",'r')as csvfile:
    file_reader=csv.reader(csvfile,delimiter=',')
    for row in file_reader:
        data.append(row)


# In[5]:


data=np.array(data)


# In[6]:


data


# In[7]:


data=np.delete(data,0,axis=0)


# In[8]:


data=np.delete(data,0,axis=0)


# In[9]:


data[0:3]


# In[10]:


d1=data[2:,:]
d1


# In[11]:


#cond for blank space in colmn 1
c=d1[:,0]==''
c


# In[12]:


#filling of the colmn1 with month name
d1[1:4,0:1]='November'
d1[5:8,0:1]='December'
d1[9:12,0:1]='January'
d1[13:16,0:1]='February'


# In[13]:


d1


# In[14]:


#vertical stacking to add title
d2=np.vstack((data[0:2,:],d1))
d2


# In[15]:


#cond for blank space in row 1
c2=data[0:1,:]==''
c2


# In[16]:


#filling of row 1 with day name
data[0:1,3:4]='Monday'
data[0:1,5:6]='Tuesday'
data[0:1,7:8]='Wednesday'
data[0:1,9:10]='Thursday'
data[0:1,11:12]='Friday'
data[0:1,13:14]='Saturday'
data[0:1,15:16]='Sunday'
data


# In[17]:


#Write the dimensions and shape of the NumPy array that you have created


# In[18]:


data.ndim


# In[19]:


data.shape


# In[20]:


#Print the daily temperatures for the first week of each month


# In[21]:


data[0:3]


# In[22]:


#cond for week1
cond_week1= data[0:,1]=='week 1'
cond_week1


# In[23]:


data_1=data[cond_week1]
data_1


# In[24]:


#vertical stacking
week1_temp=np.vstack((data[0:2,:],data_1))
week1_temp


# In[25]:


#Print the temperatures for Tuesday of each month.


# In[26]:


tuesday_temp=data[:,4:6]
tuesday_temp


# In[27]:


np.hstack((data[:,0:2],tuesday_temp))


# In[28]:


#Print only the maximum temperature for all the weekdays of Dec and Feb.


# In[29]:


data[1:2]


# In[30]:


max_temp=np.hstack((data[:,0:2],data[:,3::2]))
max_temp


# In[31]:


#cond for december temp
cond_dec=max_temp[:,0]=='December'
dec_temp=max_temp[cond_dec]


# In[32]:


#cond for February temp
cond_feb=max_temp[0:,0]=='February'
feb_temp=max_temp[cond_feb]


# In[33]:


#vertical stacking for title,december and February
np.vstack(((max_temp[0:2,:],dec_temp,feb_temp)))


# In[34]:


#Print all the days along with the week number in November when the minimum temperature was less than 8 degrees


# In[35]:


#create an array for min temp
min_temp=np.hstack((data[:,0:2],data[:,2::2]))
min_temp


# In[36]:


#mask for nov
cond_nov=min_temp[:,0]=='November'
cond_nov


# In[37]:


#min_temp for nov
min_temp_nov=min_temp[cond_nov]
min_temp_nov


# In[38]:


#data type change into int
t=min_temp_nov[:,2:].astype(int)
t


# In[39]:


#week 1 data in 1D array
week_1=t[0:1,:].reshape(7,)
week_2=t[1:2,:].reshape(7,)
week_3=t[2:3,:].reshape(7,)
week_4=t[3:4,:].reshape(7,)


# In[40]:


#cond for check where temp<8 for week1,week2,week3,week4
w1=[]
for n in week_1:
    if n<8:
        w1.append(n)
    else:
        w1.append('')
print(w1)
w2=[]
for n in week_2:
    if n<8:
        w2.append(n)
    else:
        w2.append('')
print(w2)
w2=[]
for n in week_2:
    if n<8:
        w2.append(n)
    else:
        w2.append('')
print(w2)
w3=[]
for n in week_3:
    if n<8:
        w3.append(n)
    else:
        w3.append('')
print(w3)
w4=[]
for n in week_4:
    if n<8:
        w4.append(n)
    else:
        w4.append('')
print(w4)


# In[41]:


#1d to 2d conversion
w1=np.array(w1).reshape(1,7)
w2=np.array(w2).reshape(1,7)
w3=np.array(w3).reshape(1,7)
w4=np.array(w4).reshape(1,7)


# In[42]:


#vertical stacking of week1,week2,week3 and week 4
Nov_temp=np.vstack((((w1,w2,w3,w4))))
Nov_temp


# In[43]:


#Horizentel stacking
temp_lesser_8=np.hstack((min_temp_nov[:,0:2],Nov_temp))
temp_lesser_8


# In[44]:


## Print all the weeks in Dec and Jan where the maximum temperature has crossed a threshold of 20 degrees.


# In[45]:


max_temp


# In[46]:


cond_dec=max_temp[:,0]=='December'


# In[47]:


cond_jan=max_temp[:,0]=='January'


# In[48]:


dec_jan=np.vstack((max_temp[cond_dec],max_temp[cond_jan]))
dec_jan


# In[49]:


dec_w1=dec_jan[0:1,2:].reshape(7,).astype(int)
dec_w2=dec_jan[1:2,2:].reshape(7,).astype(int)
dec_w3=dec_jan[2:3,2:].reshape(7,).astype(int)
dec_w4=dec_jan[3:4,2:].reshape(7,).astype(int)


# In[50]:


jan_w1=dec_jan[4:5,2:].reshape(7,).astype(int)
jan_w2=dec_jan[5:6,2:].reshape(7,).astype(int)
jan_w3=dec_jan[6:7,2:].reshape(7,).astype(int)
jan_w4=dec_jan[7:8,2:].reshape(7,).astype(int)


# In[51]:


d_w1=[]
for i in dec_w1:
    if i>20:
        d_w1.append(i)
    else:
        d_w1.append('')
print(d_w1)
d_w2=[]
for i in dec_w2:
    if i>20:
        d_w2.append(i)
    else:
        d_w2.append('')
print(d_w2)
d_w3=[]
for i in dec_w3:
    if i>20:
        d_w3.append(i)
    else:
        d_w3.append('')
print(d_w3)
d_w4=[]
for i in dec_w4:
    if i>20:
        d_w4.append(i)
    else:
        d_w4.append('')
print(d_w4)


# In[52]:


j_w1=[]
for i in jan_w1:
    if i>20:
        j_w1.append(i)
    else:
        j_w1.append('')
print(j_w1)
j_w2=[]
for i in jan_w2:
    if i>20:
        j_w2.append(i)
    else:
        j_w2.append('')
print(j_w2)
j_w3=[]
for i in jan_w3:
    if i>20:
        j_w3.append(i)
    else:
        j_w3.append('')
print(j_w3)
j_w4=[]
for i in jan_w4:
    if i>20:
        j_w4.append(i)
    else:
        j_w4.append('')
print(j_w4)


# In[53]:


d_w1=np.array(d_w1).reshape(1,7)
d_w2=np.array(d_w2).reshape(1,7)
d_w3=np.array(d_w3).reshape(1,7)
d_w4=np.array(d_w4).reshape(1,7)


# In[54]:


j_w1=np.array(j_w1).reshape(1,7)
j_w2=np.array(j_w2).reshape(1,7)
j_w3=np.array(j_w3).reshape(1,7)
j_w4=np.array(j_w4).reshape(1,7)


# In[55]:


temp=np.vstack((((((((d_w1,d_w2,d_w3,d_w4,j_w1,j_w2,j_w3,j_w4,))))))))
temp


# In[56]:


temp_greater_20=np.hstack((dec_jan[:,0:2],temp))
temp_greater_20


# In[57]:


#Check if there are any absurd values present in the dataset(like some temp which should not be present in the data)


# In[58]:


data[0:3]


# In[59]:


d1=data[2:,2:]
d1


# In[60]:


#Find and print the indexes of all the outlier(unusual) values present in the above dataset.


# In[61]:


data


# In[62]:


temp_1=data[2:,2:].astype(int)


# In[63]:


temp_1.shape


# In[64]:


temp_1=temp_1.reshape(16*14,)


# In[65]:


temp_1


# In[66]:


sort_temp_1=np.sort(temp_1)
sort_temp_1


# In[67]:


sort_temp_1.shape


# In[68]:


mean=round(np.mean(temp_1),3)
mean


# In[69]:


std=np.std(temp_1)
std


# In[70]:


q1=np.median(sort_temp_1[0:112])
q3=np.median(sort_temp_1[112:])
print(q1,q3)


# In[71]:


iqr=q3-q1
iqr


# In[72]:


b=[]
for i in temp_1:
    if i>q1-1.5*iqr and i<q3+1.5*iqr:
        b.append(i)
    else:
        b.append('outlier')
        print(b)


# In[73]:


temp_outliers=np.array(b).reshape(16,14)
temp_outliers


# In[74]:


#Replace the outliers with an appropriate value.


# In[75]:


k=[]
for i in b:
    if i !='outliers':
        k.append(i)
    else:
        k.append(mean)
print(k)


# In[76]:


out_re_array=np.array(k).reshape(16,14)
out_re_array


# In[77]:


#Find the average max temperature for the winter months in Jaipur.


# In[78]:


max_temp


# In[79]:


temp=max_temp[2:,2:].astype(int)
temp


# In[80]:


np.max(temp)


# In[81]:


np.mean(temp)


# In[82]:


np.median(temp)


# In[83]:


#Find the weekly min avg temp for the month of Dec in Jaipur


# In[84]:


min_temp


# In[85]:


dec_min_w1=min_temp[6:7,2:].astype(int)
dec_min_w2=min_temp[7:8,2:].astype(int)
dec_min_w3=min_temp[8:9,2:].astype(int)
dec_min_w4=min_temp[9:10,2:].astype(int)


# In[86]:


print('minimum average temperature week 1:',np.mean(dec_min_w1))
print('minimum average temperature week 2:',np.mean(dec_min_w2))
print('minimum average temperature week 3:',np.mean(dec_min_w3))
print('minimum average temperature week 4:',np.mean(dec_min_w4))


# In[87]:


#Find the overall avg temp for the months Dec and Jan


# In[88]:


data[0:3]


# In[89]:


cond_dec=data[0:,0]=='December'
dec_temp=data[cond_dec]
dec_temp=dec_temp[:,2:].astype(int)
dec_temp


# In[90]:


cond_jan=data[0:,0]=='January'
jan_temp=data[cond_jan]
jan_temp=jan_temp[:,2:].astype(int)
jan_temp


# In[91]:


np.mean(dec_temp)


# In[92]:


np.mean(jan_temp)


# In[93]:


#average temp of dec and jan
np.mean(np.vstack((dec_temp,jan_temp)))


# In[94]:


#Find the least temp experienced by the city in the month of Dec and Jan. Also print the exact date( Day/Week/Month) for the same.


# In[95]:


dec_jan_temp=np.vstack((dec_temp,jan_temp))
dec_jan_temp


# In[96]:


cond_least_temp=np.min(dec_jan_temp)
cond_least_temp


# In[97]:


d_j=np.hstack((data[6:14,0:2],dec_jan_temp[:,:]))


# In[98]:


d_j=np.vstack((data[0:2,:],d_j))


# In[99]:


d_j


# In[100]:


cond=d_j[:,2]=='2'
cond


# In[101]:


cond=d_j[:,3]=='2'
cond


# In[102]:


cond=d_j[:,4]=='2'
cond


# In[103]:


cond=d_j[:,5]=='2'
cond


# In[104]:


cond=d_j[:,6]=='2'
cond


# In[105]:


cond=d_j[:,7]=='2'
cond


# In[106]:


cond=d_j[:,8]=='2'
cond


# In[107]:


cond=d_j[:,9]=='2'
cond


# In[108]:


cond=d_j[:,10]=='2'
cond


# In[109]:


cond=d_j[:,11]=='2'
cond


# In[110]:


cond=d_j[:,12]=='2'
cond


# In[111]:


cond=d_j[:,13]=='2'
cond


# In[112]:


cond=d_j[:,14]=='2'
cond


# In[113]:


cond=d_j[:,15]=='2'
cond


# In[114]:


#Find the max temp in the month of Feb and return its date(Day/Week/Month)


# In[115]:


data[1:2]


# In[116]:


max_temp=np.hstack((data[:,0:2],data[:,3::2]))
max_temp


# In[117]:


#cond for max_February temp
cond_feb=max_temp[0:,0]=='February'
feb_temp=max_temp[cond_feb]


# In[118]:


feb_temp


# In[ ]:




