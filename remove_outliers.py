"""returns pandas dataframe after removing outliers"""

def remove_outliers(data, column):
    import numpy
    removed-outliers = data[(data['column'] >= numpy.percentile(data['column'], 0.5)) & 
        (data['column'] <= np.percentile(data['column'], 99.5))]
    return removed-outliers

