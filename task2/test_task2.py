from __future__ import division
import numpy as np
import os
from io import open
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score


def test_check_divide():
    assert 2/8 == 0.25


def test_check_divide_numpy():
    a = np.array([2])
    b = np.array([8])
    assert a/b == 0.25


def test_input_size():
    with open(os.path.dirname(__file__) + '/../input.txt',
              encoding='utf-8') as f:
        text = f.read().rstrip("\n")
    assert len(text) == 6


def test_KNN_CV():
    X, y = load_iris(return_X_y=True)
    knn = KNeighborsClassifier()
    scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
    assert sum(scores)/len(scores) > 0.7
