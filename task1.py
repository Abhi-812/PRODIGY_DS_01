import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data={
    'Age':[23, 45, 12, 33, 45, 56, 23, 44, 34, 27, 44, 55, 40, 30, 25],
    'Gender':['Male','Female','Female','Male','Female','Male','Female','Male','Female','Male','other','Male','Female','Male','other']
    }

df=pd.DataFrame(data)

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
sns.histplot(df['Age'], bins=10, kde=True)
plt.title('Age distribution:')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.subplot(1,2,2)
sns.histplot(x='Gender',data= df)
plt.title('Gender distribution:')
plt.xlabel('Gender')
plt.ylabel('Count')

plt.tight_layout()
plt.show()