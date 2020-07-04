import pandas as pd
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
from guietta import _,Gui,Quit


#df = pd.read_csv(r'C:\\Users\\Hi\\pycharm projects\\weather_prediction\\demo6.csv')
#X = df.drop(columns = ['pred'])
#y = df['pred']

#X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
#model = DecisionTreeClassifier()
#model.fit(X, y)
#pickle.dump(model, open('weather_predictor_model.pkl', 'wb'))
model = pickle.load(open('weather_predictor_model.pkl', 'rb'))

prediction = model.predict([[29.99,47,289,29]])
print(prediction)

