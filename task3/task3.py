def mean_stdev(dataset, axis=0):
    """Computes mean and standard deviation of a numpy dataset

    This function computes the mean and the standard deviation of
    a dataset along the specified axis.

    Parameters
    ----------
    dataset : Numpy Array
        Dataset Presented as a numpy array.
    axis : int
        It takes 0,1 or None, where default is 0 and
        None means computing the mean of all the entries.

    Returns
    -------
    mean: float
        Mean along the specified axis
    standard_deviation: float
        Standard Deviation along the specified axis
    """

    return np.mean(dataset, axis=axis), numpy.std(dataset, axis=axis)
