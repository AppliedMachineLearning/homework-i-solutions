# 4.1 Create a pair-plot of the iris dataset similar to Figure 1-3 in
# IMLP using only numpy and matplotlib. Ensure all axes are labeled.
# The diagonals need to contain histograms, the different species need
# to be distinguished by color or glyph.
# and there needs to be a legend for the species.

from sklearn.datasets import load_iris
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec

iris_dataset = load_iris()


X, y = iris_dataset['data'], iris_dataset['target']
features = iris_dataset['feature_names']
target_names = iris_dataset['target_names']

no = len(X[0])
recs = []
classes = ['setosa', 'versicolor', 'virginica']
class_colors = np.array(['r', 'g', 'b'])
figure, axes = plt.subplots(no, no, figsize=(15, 15))

# creating rectangles for colored patches
# alternatively you can use plot and loop to create the legend
recs = []
for color in class_colors:
    recs.append(mpatches.Rectangle((0, 0), 1, 1, fc=color))
for i in range(no):
    for j in range(no):
        if i == j:
            axes[i, j].hist(X[:, i], bins=25, edgecolor='black')
        else:
            axes[i, j].scatter(X[:, j], X[:, i], c=class_colors[y],
                               marker="o")
        axes[i, j].get_xaxis().set_visible(False)
        axes[i, j].get_yaxis().set_visible(False)
        if(j == 0):
            axes[i, j].get_yaxis().set_visible(True)
            axes[i, j].set_ylabel(features[i])
        if(i == no-1):
            axes[i, j].get_xaxis().set_visible(True)
            axes[i, j].set_xlabel(features[j])

# figure.subplots_adjust(wspace=0, hspace=0, top=0.90)
figure.legend(recs, classes)

figure.suptitle("Pair plot of the Iris dataset, colored by class label")
figure.show()
