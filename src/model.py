from sklearn.linear_model import LinearRegression, LogisticRegression

class Model():
    def __init__(self, learning_rate= 0.1, regularization= 1, num_hidden_layer= 0, model_type='LogisticRegression'):
        self.learning_rate      = learning_rate;
        self.regulization       = regularization;
        self.num_hidden_layers  = num_hidden_layer;

        if model_type == 'LogisticRegression':
            self.model = LogisticRegression();
        elif model_type == 'LinearRegression()':
            self.model = LinearRegression();
        else:
            print("Unknown model Passed");
        return

    def trainModel(self, features = None, labels = None):
        self.model.fit(X=features, y=labels);
        print("Model Training Completed");
        return

    def calculateTrainingAccuracy(self, features= None, labels= None):
        training_accuracy = self.model.score(X=features, y=labels);
        print("Training acuracy is %i", training_accuracy);
        return training_accuracy

    def calculateTestAccuracy(self, features= None, labels = None):
        self.model(features= features, labels=labels);
        return

    def testTheModel(self, features = None, labels = None):
        test_accuracy = self.model.score(X=features, y=labels);
        print('The testing is done and the test score is %i', test_accuracy);
        return test_accuracy

    def predictTheModel(self, features = None):
        predicted_labels = self.model.predict(X= features);
        print('Prediction is complete, Sourcing out the preicted labels...');
        return predicted_labels




