import seaborn as sns;
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;
df=pd.read_csv('911.csv');

#Analysing the data types of attributes
print(df.info());
print(df.head());
print(df.columns());
print(df['twp'].value_counts().head());
print(df['title'].nunique());



#Splitting the title string to form a new attribut reason which is required
df['reason']=df['title'].apply(lambda title : title.split(':')[0]);
print(df['reason'].value_counts().head(1));
sns.countplot(x='reason',data=df);
plt.show();

#creating hour,month and dayofweek columns to get a clear visualisation of the data
df['timeStamp']=pd.to_datetime(df['timeStamp']);
df['hour']=df['timeStamp'].apply(lambda  x: x.hour);
df['month']=df['timeStamp'].apply(lambda  x: x.month);
df['dayofweek']=df['timeStamp'].apply(lambda  x: x.dayofweek);
dmap={0:'sunday',1:'monday',2:'tuesday',3:'wednesday',4:'thursday',5:'friday',6:'saturday'};
df['dayofweek']=df['dayofweek'].map(dmap);


#data visualisations to analyse the data and get a conclusion
sns.countplot(x='dayofweek',data=df,hue='reason');
plt.show();
sns.countplot(x='month',data=df,hue='reason');
plt.show();
bymonth=df.groupby('month').count();
sns.lmplot(x='month',y='twp',data=bymonth.reset_index());
plt.show();
df['date']=df['timeStamp'].apply(lambda x: x.date());
df.groupby('date').count()['lat'].plot();
plt.show();
df1=df.groupby(by=['dayofweek','hour']).count()['reason'].unstack();
sns.heatmap(df1);
plt.show();
