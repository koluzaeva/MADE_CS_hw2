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


	 def cross_val_train(self, X, y):
                self.acc = 0
                for X_train, X_test, y_train, y_test in cross_val(X, y):
                        self.fit(X_train, y_train)
                        self.pred = self.predict(X_test, y_test)
                        self.acc += self.accuracy(self.pred, y_test)
                return self.acc
	
	def test_model(self, X_test, y_test):
		pass 

