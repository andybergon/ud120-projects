#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = map(lambda x: (x[1], x[2], x[0] - x[2]),
                       sorted(zip(predictions, ages, net_worths), key=lambda tup: tup[0] - tup[2], reverse=True)[
                       int(len(predictions) * 0.1):])

    return cleaned_data
