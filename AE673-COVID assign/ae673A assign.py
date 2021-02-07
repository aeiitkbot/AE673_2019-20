import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Taking input
df=pd.read_csv('coviddata.csv')
df.drop(['country_code','continent','source','population','rate_14_day'],axis=1,inplace=True)

# ### France
t1=df['country']=='France'; t2=df['indicator']=='confirmed cases'
df1=df[np.logical_and(t1,t2)]
cc=df1['daily_count']; x=df1['date']
cc=np.cumsum(cc)

t1=df['country']=='Afghanistan'; t2=df['indicator']=='deaths'
df1=df[np.logical_and(t1,t2)]
ds=df1['daily_count']; x=df1['date']
ds=np.cumsum(ds)

fig= plt.figure(figsize=(15,6))
axes= fig.add_axes()
plt.plot(range(len(cc)),np.log(cc+1))
plt.plot(range(len(ds)),np.log(ds+1))
plt.title('FRANCE')
plt.ylabel('Number of People')
plt.xlabel('Number of days starting from 2nd Jan\'20')
plt.legend(['Confirmed Cases','Deaths'])
plt.show()

print("Observation:")
print("As we can see from the graph of France, number of total cases increased and is almost constant at the end, therefore no second wave is observed.")

# ### Brazil
t1=df['country']=='Brazil'; t2=df['indicator']=='confirmed cases'
df1=df[np.logical_and(t1,t2)]
cc=df1['daily_count']; x=df1['date']
cc=np.cumsum(cc)

t1=df['country']=='Afghanistan'; t2=df['indicator']=='deaths'
df1=df[np.logical_and(t1,t2)]
ds=df1['daily_count']; x=df1['date']
ds=np.cumsum(ds)

fig= plt.figure(figsize=(15,6))
axes= fig.add_axes()
plt.plot(range(len(cc)),np.log(cc+1))
plt.plot(range(len(ds)),np.log(ds+1))
plt.title('BRAZIL')
plt.ylabel('Number of People')
plt.xlabel('Number of days starting from 2nd Jan\'20')
plt.legend(['Confirmed Cases','Deaths'])
plt.show()


# ### Iran
t1=df['country']=='Iran'; t2=df['indicator']=='confirmed cases'
df1=df[np.logical_and(t1,t2)]
cc=df1['daily_count']; x=df1['date']
ds=np.cumsum(ds)

t1=df['country']=='Afghanistan'; t2=df['indicator']=='deaths'
df1=df[np.logical_and(t1,t2)]
ds=df1['daily_count']; x=df1['date']
cc=np.cumsum(cc)

fig= plt.figure(figsize=(15,6))
axes= fig.add_axes()
plt.plot(range(len(cc)),np.log(cc+1))
plt.plot(range(len(ds)),np.log(ds+1))
plt.title('IRAN')
plt.ylabel('Number of People')
plt.xlabel('Number of days starting from 2nd Jan\'20')
plt.legend(['Confirmed Cases','Deaths'])
plt.show()


# ### Itlay
t1=df['country']=='Italy'; t2=df['indicator']=='confirmed cases'
df1=df[np.logical_and(t1,t2)]
cc=df1['daily_count']; x=df1['date']
cc=np.cumsum(cc)

t1=df['country']=='Afghanistan'; t2=df['indicator']=='deaths'
df1=df[np.logical_and(t1,t2)]
ds=df1['daily_count']; x=df1['date']
ds=np.cumsum(ds)

fig= plt.figure(figsize=(15,6))
axes= fig.add_axes()
plt.plot(range(len(cc)),np.log(cc+1))
plt.plot(range(len(ds)),np.log(ds+1))
plt.title('ITALY')
plt.ylabel('Number of People')
plt.xlabel('Number of days starting from 2nd Jan\'20')
plt.legend(['Confirmed Cases','Deaths'])
plt.show()


# ### China
t1=df['country']=='China'; t2=df['indicator']=='confirmed cases'
df1=df[np.logical_and(t1,t2)]
cc=df1['daily_count']; x=df1['date']
cc=np.cumsum(cc)

t1=df['country']=='Afghanistan'; t2=df['indicator']=='deaths'
df1=df[np.logical_and(t1,t2)]
ds=df1['daily_count']; x=df1['date']
ds=np.cumsum(ds)

fig= plt.figure(figsize=(15,6))
axes= fig.add_axes()
plt.plot(range(len(cc)),np.log(cc+1))
plt.plot(range(len(ds)),np.log(ds+1))
plt.title('CHINA')
plt.ylabel('Number of People')
plt.xlabel('Number of days starting from 2nd Jan\'20')
plt.legend(['Confirmed Cases','Deaths'])
plt.show()


# ### India
t1=df['country']=='India'; t2=df['indicator']=='confirmed cases'
df1=df[np.logical_and(t1,t2)]
cc=df1['daily_count']; x=df1['date']
cc=np.cumsum(cc)

t1=df['country']=='Afghanistan'; t2=df['indicator']=='deaths'
df1=df[np.logical_and(t1,t2)]
ds=df1['daily_count']; x=df1['date']
ds=np.cumsum(ds)

fig= plt.figure(figsize=(15,6))
axes= fig.add_axes()
plt.plot(range(len(cc)),np.log(cc+1))
plt.plot(range(len(ds)),np.log(ds+1))
plt.title('INDIA')
plt.ylabel('Number of People')
plt.xlabel('Number of days starting from 2nd Jan\'20')
plt.show()


# ### UK
t1=df['country']=='United Kingdom'; t2=df['indicator']=='confirmed cases'
df1=df[np.logical_and(t1,t2)]
cc=df1['daily_count']; x=df1['date']
cc=np.cumsum(cc)

t1=df['country']=='Afghanistan'; t2=df['indicator']=='deaths'
df1=df[np.logical_and(t1,t2)]
ds=df1['daily_count']; x=df1['date']
ds=np.cumsum(ds)

fig= plt.figure(figsize=(15,6))
axes= fig.add_axes()
plt.plot(range(len(cc)),np.log(cc+1))
plt.plot(range(len(ds)),np.log(ds+1))
plt.title('UK')
plt.ylabel('Number of People')
plt.xlabel('Number of days starting from 2nd Jan\'20')
plt.show()