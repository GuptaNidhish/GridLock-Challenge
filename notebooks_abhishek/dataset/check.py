import pandas as pd

train = pd.read_csv("dataset/train.csv")
test = pd.read_csv("dataset/test.csv")

print("Train missing:")
print(train.isnull().sum())
print("\nTest missing:")
print(test.isnull().sum())

print("\nTrain shapes:")
print(train.shape, test.shape)
