******
README
******

TASK 3
######

The meanStdev function computes the mean and the standard deviation of a dataset along the specified axis. It takes in the dataset (represented by a numpy array) and the desired axis (which could be among 0,1 or None). It returns the mean and the standard deviation calculated along the desired axis according to the following formula.

Formula for mean:

.. math::

   mean(\overline{A}) = \frac{ \sum_{i=1}^{N}A[i]}{\sum_{i=1}^{N}1}

where N is the number of elements

Formula for standard deviation:

.. math::

    s = \sqrt{\frac{1}{N} \sum_{i=1}^N (A[i] - \overline{A})^2}

`Link to Main page <index.html>`_
