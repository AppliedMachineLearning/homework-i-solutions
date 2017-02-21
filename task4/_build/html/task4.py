
# coding: utf-8

# 4.1 Create a pair-plot of the iris dataset similar to Figure 1-3 in IMLP using only numpy and matplotlib. Ensure all axes are labeled. The diagonals need to contain histograms, the different species need to be distinguished by color or glyph,
# and there needs to be a legend for the species.

# In[1]:

from sklearn.datasets import load_iris
iris_dataset = load_iris()


# In[4]:

import numpy as np
from matplotlib import pyplot as pl
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec


X, Y, features, target_names = iris_dataset['data'], iris_dataset['target'], iris_dataset['feature_names'],iris_dataset['target_names']

def make_plot(data, labels, features):

    no = len(data[0])
    fig = pl.figure()
    recs=[]
    classes = ['setosa' ,'versicolor', 'virginica']
    class_colours = np.array(['r','g','b'])
    
    fig.set_figheight(15)
    fig.set_figwidth(15)

    recs = []
    for i in range(0,len(class_colours)):
        recs.append(mpatches.Rectangle((0,0),1,1,fc=class_colours[i]))
    fig.legend(recs,classes)    
    

    for i in range(no):
        for j in range(no):
            nSub = i * no + j + 1
            ax = fig.add_subplot(no, no, nSub)
            
            if(j==0):
                ax.set_ylabel(features[i])
            if(i==no-1):
                ax.set_xlabel(features[j])
            if i == j:
                ax.hist(data[:,i])
            else:              
                ax.scatter(data[:,i], data[:,j], c=class_colours[labels])

    fig.suptitle("Pair plot of the Iris dataset, colored by class label")
    return fig

fig=make_plot(X,Y,features)
fig.show()
fig.savefig("plot.png")

