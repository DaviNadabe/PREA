import seaborn as sns

iris = sns.load_dataset('iris')
iris.head()
print (iris.max())
print(iris.min())

print(iris.mean(numeric_only=True ))
print(iris.median(numeric_only=True ))


print(iris.quantile(0.25, numeric_only=True))
print(iris.quantile(0.5, numeric_only=True))
print(iris.quantile(0.75, numeric_only=True))


print(iris.describe().loc["mean", "petal_length"])