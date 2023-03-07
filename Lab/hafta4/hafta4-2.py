import pandas as pd
from google.colab import files
file = files.upload()
data = pd.read_csv("breastCancer.csv", header = None)


data.info()
data.head(15)
df = pd.DataFrame(data)
df[6] = df[6].replace('?',0)
df[6] = df[6].astype(int)

mean = int(df[6].mean())
df[6] = df[6].replace(0,mean)
df.head()

df = pd.DataFrame(data)
df[6].value_counts()

df[10] = df[10].replace(2,0).replace(4,1)
df.head(10)



from sklearn.model_selection import train_test_split

X = df.iloc[:, 1:10]
Y = df.iloc[:, 10]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

classifier.add(Dense(units = 5, activation = 'relu', input_dim=9))
classifier.add(Dense(units = 3, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

classifier.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

classifier.fit(X_train, Y_train, batch_size = 10, epochs = 100)

Y_pred = classifier.predict(X_test)
Y_pred = [ 1 if y>=0.5 else 0 for y in Y_pred]
print(Y_pred)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)
print(cm)
