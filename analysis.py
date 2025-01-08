import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
data = pd.read_csv("C:/Users/HP/Desktop/creditcard.csv")
data_df = pd.DataFrame(data)

# Number of rows and columns
# print(data_df.shape)

# Column DataTypes
# print(data_df.info())

# Number of Fraudulent/Legitimate Activities 
# print(data_df['Class'].value_counts())

# Pecentage of Fraudulent/Legitimate Activities 
# print(data_df['Class'].value_counts(normalize=True))

# Minimum, Maximum, Mean and Median Values in Amount Column
# print(data_df['Amount'].describe())

# Maximum transaction amount in the dataset, and is it fraudulent ?
# print(data_df['Amount'].max())
# print(data_df[data_df['Amount'] == data_df['Amount'].max()]['Class'])

# Barchart showing the count of fraudulent vs. legitimate transactions
# counts = data_df['Class'].value_counts()
# counts.index = ['Legitimate','Fraudulent']
# counts.plot(kind='bar')
# plt.ylabel("Total Counts")
# plt.xticks(rotation=0) 
# plt.show()

# Histogram of transaction amounts 
plt.hist(data_df['Amount'])
plt.xlabel('Transaction Amount')
plt.ylabel('Frequency')
plt.title('Histogram of Transaction Amounts') 
plt.show()

# Heatmap to visualize the correlation between numerical features

sns.heatmap(data_df.corr())
plt.show()