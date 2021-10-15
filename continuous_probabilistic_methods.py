#Continuous Probabilistic Methods: Exercises
#-------------------------------------------

#1. Define a function named get_lower_and_upper_bounds that has two arguments. 
# The first argument is a pandas Series. 
# The second argument is the multiplier, which should have a default argument of 1.5

def get_lower_and_upper_bounds(s, multiplier=1.5):

    # Defining IQR/Tukey method: get the Q1 and Q3 values

    # start with an inner fence calculation

    # calculate our q1 and q3
    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)

    iqr = q3 - q1

    lower_fence = q1 - (multiplier * iqr)
    upper_fence = q3 + (multiplier * iqr)

    return multiplier, lower_fence, upper_fence