class Model: 
	def __init__(self, name, model):
		self.model = model
		self.name = name
	
	 def fit(self, X_train, y_treain):
                self.fit(X_train, y_train)

        def predict(self, X_test):
                self.predict = self.model.predict(X_test)
                return self.pred
	def cross_val_split(self, X, y):
                pass




