from sklearn import tree

#Decision Tree

#[height, weight, shoe size]

X= [[180,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,48],[190,90,47],
   [175,65,39],[177,70,40],[159,59,37],[171,75,42],[181,83,43]]
Y= ['m','f','f','f','m','m','m','f','m','f','m']
# Variable to Store our Classifier
clf=tree.DecisionTreeClassifier()
clf=clf.fit(X,Y)
prediction=clf.predict([180,70,43])
print prediction