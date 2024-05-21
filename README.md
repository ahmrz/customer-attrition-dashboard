# An Interactive Dashboard for Predicting Bank Customer Attrition

This dash application allows you to predict  customer churn using machine learning algorithms (Random Forest and SVM). Developed with Python using scikit-learn, dash and plotly libraries. You can:
- Predict customer churn
- Review data analysis

## Abstract

Customer attrition rate is a significant concern for commercial banks. In this era of increased competition, banks have to compete fiercely to retain existing customers, particularly high-grade customers. Commercial banks have a clear motivation to predict customer attrition and by taking appropriate actions beforehand, they can not only significantly increase profits, but also, enhance their core competitiveness. This paper presents six machine learning algorithms, Logistic Regression, Support Vector Machine, Decision Tree, Random Forest, Gradient Boosting Classifier and K-Nearest Neighbor, which are trained using two different publicly available datasets to predict bank customer attrition rates. The results of the algorithms are measured using four metrics: Accuracy, Precision, Recall, and F-Measure. In addition, a dashboard is designed that can provide exploratory analysis of current customers and also provides their loyalty status prediction using the mentioned machine learning algorithms. Results show that Gradient Boosting Classifier and Random Forest algorithms performed the best, reaching an average accuracy of about 87% and 97%, respectively for both datasets.

The complete paper can be viewed at [https://doi.org/10.1109/ETCEA57049.2022.10009818](https://doi.org/10.1109/ETCEA57049.2022.10009818).


## Dataset:
- Dataset 1 (ChurnModeling):
https://www.kaggle.com/adammaus/predicting-churn-for-bank-customers

## Installation and Usage:
1. Install all dependencies listed in requirements.txt - all packages are pip-installable.
2. Run app.py to launch a local Dash server to host the Dash app. A link will appear in your console; click this to use the Dash app.
