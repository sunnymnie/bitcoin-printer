# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import plot_roc_curve

def train_model(X, y, tts=False):
	"""
	Returns trained model given X and y. If tts is true, also return X_train, X_test, y_train, y_test. 
	"""
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
	np.random.seed(42)
	model = RandomForestClassifier()
	m = model.fit(X_train, y_train)
	return m if not tts else m, X_train, X_test, y_train, y_test


def plot_conf_matrix(X, y):
	"""
	Plots a confusion matrix with default paramaters
	"""
	model, X_train, X_test, y_train, y_test = train_model(X, y, tts=True)
	y_preds = model.predict(X_test)	

	sns.set(font_scale = 1.5)
	fig, ax = plt.subplots(figsize=(3, 3))
	ax = sns.heatmap(confusion_matrix(y_test, y_preds),
					 annot=True,
					 cbar=False)
	plt.xlabel("True label")
	plt.ylabel("Predicted label")

def feature_importance(X, y, plot=True):
	"""
	plots the feature importance. If plot is False, returns dictionary of feature importance
	"""
	model, X_train, X_test, y_train, y_test = train_model(X, y, tts=True)


	feature_dict = dict(zip(X_train.columns, list(model.feature_importances_)))
	feature_df = pd.DataFrame(feature_dict, index=[0])
	if not plot:
		return feature_df
	feature_df.T.plot.bar(title="Feature Importance", legend=False, figsize=(10, 6));

def cross_val_metrics(X, y, remind=False):
	"""
	Generates cross validated metrics with default RandomForestClassifier hyperparamaters. 
	If remind is true, gives definition of accuracy, precision, recall, f1. 

	X = df.drop(["target"], axis=1)
	y = df["target"]
	"""
	# model = train_model(X, y)
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
	np.random.seed(42)
	model = RandomForestClassifier()
	model.fit(X_train, y_train)

	def cross_validated_metric(model, metric:str)->float:
		"""
		returns the cross-validated metric
		"""
		cv_metric = cross_val_score(model, X, y, cv=5, scoring=metric)
		return np.mean(cv_metric)


	d = {}
	d["accuracy"] = cross_validated_metric(model, 'accuracy')
	d["precision"] = cross_validated_metric(model, 'precision')
	d["recall"] = cross_validated_metric(model, 'recall')
	d["f1"] = cross_validated_metric(model, 'f1')
	
	if remind:
		d["remind"] = {"Accuracy": "Ratio of number of correct predictions to all predictions",
						"Precision": "Portion of guessed positives that are actually correct",
						"Recall": "Portion of actual positives that are guessed correct",
						"F1": "Balance, use if uneven class distribution (ie large # actual negatives)"}
	return d
	
def generate_report(X, y, remind=False):
	"""
	renerates report with default RandomForestClassifier paramaters
	"""
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
	np.random.seed(42)
	model = RandomForestClassifier()
	model.fit(X_train, y_train)

	d = {}
	d["precision"] = np.mean(cross_val_score(model, X, y, cv=5, scoring='precision'))
	d["recall"] = np.mean(cross_val_score(model, X, y, cv=5, scoring='recall'))
	d["f1"] = np.mean(cross_val_score(model, X, y, cv=5, scoring='f1'))

	if remind:
		d["remind"] = {	"Precision": "Portion of guessed positives that are actually correct",
						"Recall": "Portion of actual positives that are guessed correct",
						"F1": "Balance, use if uneven class distribution (ie large # actual negatives)"}
	return d
	# print(f"accuracy: {cross_validated_metric(model, 'accuracy')}")
	# print(f"precision: {cross_validated_metric(model, 'precision')}")
	# print(f"recall: {cross_validated_metric(model, 'recall')}")
	# print(f"f1: {cross_validated_metric(model, 'f1')}")
	
def forward_test(X, y, close, rows=3000, mistakes=False):
	"""
	performs quick forward test with last 'rows' number of rows (Default 3000)
	close is closing price and is same length as X (and y)
	If mistakes, shows correct, wrong, and missed. 
	"""
	close = close[-rows:]
	X_train, X_test, y_train, y_test = train_test_split(X[:-rows], y[:-rows], test_size=0.2)
	model = RandomForestClassifier()
	model.fit(X_train, y_train)
	results = model.predict(X[-rows:])
	scatter_results = list(map(lambda x, c: c if x == 1 else None, results, close))

	s_correct = list(map(lambda x, t, c: c if x == 1 and t == 1 else None, results, y[-rows:], close))
	s_wrong = list(map(lambda x, t, c: c if x == 1 and t == 0 else None, results, y[-rows:], close))
	s_missed = list(map(lambda x, t, c: c if x == 0 and t == 1 else None, results, y[-rows:], close))

	fig,ax = plt.subplots(figsize=(20, 10))
	if not mistakes:
		ax.scatter(range(rows), 
					scatter_results,
					color="#43aa8b")
	else:

		ax.scatter(range(rows), 
					s_missed,
				color="#f9c74f")

		ax.scatter(range(rows), 
					s_correct,
		 		color="#43aa8b")

		ax.scatter(range(rows), 
					s_wrong,
				color="#f94144")

	ax.set_xlabel("time")
	ax.set_ylabel("close")
	ax.plot(range(rows),
			close,
			color="gray")

	ax.tick_params(labelbottom=False)
	ax.axes.xaxis.set_visible(False)

	# Scatter

