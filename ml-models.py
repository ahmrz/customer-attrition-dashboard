# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from colorama import Fore, Back, Style


# Discover Data

# Read CSV data
data = pd.read_csv("data/Data1_Churn_Modelling.csv")

# Print the first 5 lines of the dataset
# data.head()

# Convert all columns heading in lowercase
clean_column_name = []
columns = data.columns
for i in range(len(columns)):
    clean_column_name.append(columns[i].lower())
data.columns = clean_column_name

# Drop the irrelevant columns  as shown above
data = data.drop(["rownumber", "customerid", "surname"], axis=1)

# data.head()
# data['exited'].unique()
# {column: list(data[column].unique()) for column in data.select_dtypes('object').columns}

gender = {"Female": 0, "Male": 1}
city = {"France": 0, "Spain": 1, "Germany": 2}

data["gender"] = data["gender"].replace(gender)
data["geography"] = data["geography"].replace(city)

# data.head()

# Split df into X and y
y = data["exited"].copy()
X = data.drop("exited", axis=1).copy()

# Scale X with a standard scaler
# scaler = StandardScaler()
# X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

# Checking for unique value in the data attributes
# data.nunique()

# Separate dataset into train and test
# from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# X_train.shape, X_test.shape

LR = LogisticRegression()
svc = SVC()
DTC = DecisionTreeClassifier()
RFC = RandomForestClassifier()
GBC = GradientBoostingClassifier()
KNN = KNeighborsClassifier()

models = [LR, svc, DTC, RFC, GBC, KNN]

for model in models:
    model.fit(X_train, y_train)

# For exporting model files
import pickle

model_names = [
    "Logistic_Regression",
    "Support_Vector_Machine",
    "Decision_Tree",
    "Random_Forest",
    "Gradient_Boosting_Classifier",
    "KNN",
]

for model, name in zip(models, model_names):

    # Save the model files
    filename = "data/" + name + "_Model.sav"
    pickle.dump(model, open(filename, "wb"))

    # Print the output on the screen
    print(
        Fore.RED
        + name
        + " Accuracy : {:.4f}%".format(model.score(X_test, y_test) * 100)
        + Fore.RESET
    )

    pred = model.predict(X_test)
    print(model.predict(X_test.iloc[0:10]))
    print(Fore.RED + "confusion_matrix :" + Fore.RESET)
    print(confusion_matrix(y_test, pred))

    print(Fore.RED + "classification_report :" + Fore.RESET)
    print(classification_report(y_test, pred))
    print("------------------------------------------------------------")

# For importing model files
import joblib

# Model Read
svm_path = "data/Support_Vector_Machine_Model.sav"
svm_model = joblib.load(svm_path)

rf_path = "data/Random_Forest_Model.sav"
rf_model = joblib.load(rf_path)

print(rf_model.predict(X_test.iloc[0:10]), svm_model.predict(X_test.iloc[0:10]))
# RFC.score(X_test, y_test) * 100
