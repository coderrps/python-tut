# x =lambda a : a + 10
# a  = 8
# print(x(a))

# x = lambda a, b : a * b
# a = 10
# b = 20
# print(x(a, b))

# x = lambda a, b, c : a*b*c
# print(x(2, 2, 2))

# def myfunc(n):
#     return lambda a: a* n 
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
# print(mytripler(11))
# print(mydoubler(11))


# cars = ['Toyota', 'Mercedes', 'Volvo', 'BMW', 'Safari']
# print(cars[1])
# print(len(cars))

# for x in cars:
#     print(x)

# cars.append('Honda')
# cars.pop(1)
# cars.remove('Volvo')

# print("\nNew List-")
# for x in cars:
#     print(x)

# class MyClass:
#     x = 5
#     y = 10

# p1 = MyClass()
# print(p1.x * p1.y)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}, {self.age}"
    
#     def myFunc(self):
#         print("Hello my name is", self.name, "and my age is", self.age)

# p1 = Person('John', 23)
# p2 = Person('Ritu', 22)
# p3 = Person('Helly', 25)
# p4 = Person('Priya', 30)
# print(p2.name, p2.age)
# print(p1.name, p1.age)
# print(p3)
# p4.myFunc()


# class Person:
#     def __init__(myobj, name, age):
#         myobj.name = name
#         myobj.age = age

#     def myfunc(abc):
#         print("hello my name is", abc.name)
#         print("My age is", abc.age)

# p1 = Person('John', 32)
# p1.myfunc()
# p1.age = 40 
# del p1.age
# del p1





# Parent Class
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname 

#     def printname(self):
#         print(self.firstname, self.lastname)

# x = Person('John', 'Doe')
# x.printname()

# child Class
# class Student(Person):
#     pass

# class Student2(Person):
#     def __init__(self, fname, lname, year):
#         super()__init__(fname, lname)
#         self.gradYear = year 

#     def __str__(self):
#         return f"{self.firstname} {self.lastname} {self.gradYear}"
    
#     def welcome(self):
#         print(self.firstname, self.lastname, self.gradYear)

# y = Student('Mike', 'Olsen')
# y.printname()
# z = Student2('Danny', "Mark", 2021)
# z.welcome()
# print(z)


# mytuple = ('apple', 'banana', 'cherry')
# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# mystr = "banana"
# myit2 = iter(mystr)
# print(next(myit2))
# print(next(myit2))
# print(next(myit2))
# print(next(myit2))
# print(next(myit2))
# print(next(myit2))
# print(next(myit2))

# for x in mytuple:
#     print(x)

# for i in mystr:
#     print(i)


# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self  
    
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1 
#             return x 
#         else:
#             raise StopIteration
    
# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# for i in myiter:
#     print(i)


# Polymorphism --> multiple classes with the same method name
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model 

#     def move(self):
#         print("Drive!")

# class Boat:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Sail!")

# class Plane:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Fly!")

# car1 = Car("Ford", "Mustang")
# boat1 = Boat("Mount", "Cruise 69")
# plane1 = Plane("Boeing", "777")

# for x in (car1, boat1, plane1):
#     x.move()



# Inheritance Class Polymorphism
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Move!")

# class Car(Vehicle):
#     pass

# class Boat(Vehicle):
#     def move(self):
#         print("Sail!")

# class Plane(Vehicle):
#     def move(self):
#         print("Fly!")

# car1 = Car("Ford", "Mustang") 
# boat1 = Boat("Ibiza", "Touring 20") 
# plane1 = Plane("Boeing", "747") 

# for x in (car1, boat1, plane1):
#     print(x.brand)
#     print(x.model)
#     x.move()


# def myfunc():
#     x = 300
#     def myinnerfunc():
#         print(x) 
#     myinnerfunc()
# myfunc()


# x = 400
# def myfunc():
#     print(x)
# myfunc()

# import datetime
# x = datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.strftime("%A"))

# x = min(23, 45, 21)
# y = max(23, 45, 21)
# print(x)
# print(y)

# x = abs(-5.39)
# print(x)

# x = pow(4, 2)
# print(x)

# import math 
# x = math.sqrt(64)
# print(x)
# y = math.pi
# print(y)

# import re
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)

# try:
#     print(x)
# except NameError:
#     print("Variable X is not defined")
# except:
#     print("An Error Occured")


# import matplotlib.pyplot as plt
# import numpy as np
# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(xpoints, ypoints)
# plt.show()

# import numpy as np
# from scipy import stats
# import matplotlib.pyplot as plt
# from sklearn.metrics import r2_score
# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# print("Mean Value: ", np.mean(speed))
# print("Median Value: ", np.median(speed))
# print("Mode Value: ", stats.mode(speed))
# print("Standard Deviation: ", np.std(speed))
# print("Variance: ", np.var(speed))
# ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
# print("Percentile:", np.percentile(ages, 90))
# print("Random Array: ", np.random.uniform(0, 500, 250))
# x = np.random.uniform(0.0, 500, 100000)
# plt.hist(x, 100)
# plt.show()
# x = np.random.normal(5, 1, 100000)
# plt.hist(x, 100)
# plt.show()

# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# x = np.random.normal(5, 1, 1000)
# y = np.random.normal(10, 2, 1000)

# slope, intercept, r, p, std_err = stats.linregress(x, y)
# def myfunc(x):
#     return slope * x + intercept
# mymodel = list(map(myfunc, x))
# plt.scatter(x, y)
# plt.plot(x, mymodel)
# plt.show()
# print(r)
# speed = myfunc(10)
# print(speed)


# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
# mymodel = np.poly1d(np.polyfit(x, y, 3))
# myline = np.linspace(1, 25, 100)
# plt.scatter(x, y)
# plt.plot(myline, mymodel(myline))
# plt.show()
# print(r2_score(y, mymodel(x)))
# speed = mymodel(17)
# print(speed)

# import pandas as pd
# df = pd.read_csv("data.csv")
# X = df[['Weight', 'Volume']]
# y = df[['CO2']]
# from sklearn import linear_model
# from sklearn.preprocessing import StandardScaler

# model = linear_model.LinearRegression()
# model.fit(X, y)
# predictedCO2 = model.predict([[3300, 1300]])
# print(predictedCO2)
# print(model.coef_)

# scale = StandardScaler()
# scaledX = scale.fit_transform(X)
# print(scaledX)

# regr = linear_model.LinearRegression()
# regr.fit(scaledX, y)
# scaled = scale.transform([[2300, 1.3]])
# predictedCO2 = regr.predict([scaled[0]])
# print(predictedCO2)



# import pandas as pd
# from sklearn import tree
# from sklearn.tree import DecisionTreeClassifier
# import matplotlib.pyplot as plt
# df = pd.read_csv('dt_data.csv')
# d = {'UK':0, 'USA':1, 'N':2}
# df['Nationality'] = df['Nationality'].map(d)
# d = {'YES':1, 'NO': 0}
# df['Go'] = df['Go'].map(d)
# features = ['Age', 'Experience', 'Rank', 'Nationality']
# X = df[features]
# y = df['Go']
# dtree = DecisionTreeClassifier()
# dtree = dtree.fit(X, y)
# tree.plot_tree(dtree, feature_names=features)



# import matplotlib.pyplot as plt
# import numpy
# from sklearn import metrics
# actual = numpy.random.binomial(1,.9,size = 1000)
# predicted = numpy.random.binomial(1,.9,size = 1000)
# confusion_matrix = metrics.confusion_matrix(actual, predicted)
# cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [0, 1])
# cm_display.plot()
# plt.show()
# Accuracy = metrics.accuracy_score(actual, predicted)
# Precision = metrics.precision_score(actual, predicted)
# Sensitivity_recall = metrics.recall_score(actual, predicted)
# Specificity = metrics.recall_score(actual, predicted, pos_label=0)
# F1_score = metrics.f1_score(actual, predicted)
# print({"Accuracy":Accuracy,"Precision":Precision,"Sensitivity_recall":Sensitivity_recall,"Specificity":Specificity,"F1_score":F1_score})



# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.cluster.hierarchy import dendrogram, linkage
# x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
# y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
# data = list(zip(x, y))
# linkage_data = linkage(data, method='ward', metric='euclidean')
# dendrogram(linkage_data)
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.cluster import AgglomerativeClustering
# x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
# y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
# data = list(zip(x, y))
# hierarchical_cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
# labels = hierarchical_cluster.fit_predict(data)
# plt.scatter(x, y, c=labels)
# plt.show()



# import numpy
# from sklearn import linear_model
# X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
# y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
# logr = linear_model.LogisticRegression()
# logr.fit(X,y)
# predicted = logr.predict(numpy.array([3.46]).reshape(-1,1))
# print(predicted)



# import numpy
# from sklearn import linear_model
# X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
# y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
# logr = linear_model.LogisticRegression()
# logr.fit(X,y)
# log_odds = logr.coef_
# odds = numpy.exp(log_odds)
# print(odds)



# import numpy
# from sklearn import linear_model
# X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
# y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
# logr = linear_model.LogisticRegression()
# logr.fit(X,y)
# def logit2prob(logr, X):
#   log_odds = logr.coef_ * X + logr.intercept_
#   odds = numpy.exp(log_odds)
#   probability = odds / (1 + odds)
#   return(probability)
# print(logit2prob(logr, X))



# import pandas as pd
# from sklearn import linear_model
# cars = pd.read_csv('data.csv')
# ohe_cars = pd.get_dummies(cars[['Car']])
# X = pd.concat([cars[['Volume', 'Weight']], ohe_cars], axis=1)
# y = cars['CO2']
# regr = linear_model.LinearRegression()
# regr.fit(X, y)
# predictedCO2 = regr.predict([[2300, 1300,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])
# print(predictedCO2)


# import matplotlib.pyplot as plt
# x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
# y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
# from sklearn.cluster import KMeans
# data = list(zip(x, y))
# inertias = []
# for i in range(1, 11):
#     kmeans = KMeans(n_clusters=i)
#     kmeans.fit(data)
#     inertias.append(kmeans.inertia_)
# plt.plot(range(1,11), inertias, marker='o')
# plt.title('Elbow method')
# plt.xlabel('Number of clusters')
# plt.ylabel('Inertia')
# plt.show()



# n = 1234
# print(str(n)[::-1])

# def palindrome(x):
#     if str(x) == str(x)[::-1]:
#         return True
#     else:
#         return False
# print(palindrome(1213))
    

# def gcd_lcm(A, B):
#     def gcd(a,b):
#         while b:
#             a, b = b, a%b
#         return a
#     gcd_val = gcd(A, B)
#     lcm_val = (A*B) // gcd_val
#     return [lcm_val,gcd_val]
# print(gcd_lcm(42, 24))




# def armstrong(x):
#     num_str = str(x)
#     n = len(num_str)
#     sum = 0
#     for i in num_str:
#         sum += int(i) ** n
#     if sum == x:
#         return True
#     else: 
#         return False
# print(armstrong(123))


# def sum_divisor(x):
#     sum = 0
#     for i in range(1, x+1):
#         sum += (i * (x // i))
#     return sum

# print(sum_divisor(4))