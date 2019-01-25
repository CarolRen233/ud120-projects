#!/usr/bin/python
import math

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)."""

    cleaned_data=[]
    e=abs(predictions-net_worths)
    cleaned_data=zip(ages,net_worths,e)
    cleaned_data=sorted(cleaned_data,key=lambda clean:clean[2])
    clean_num=int(math.ceil(len(cleaned_data)*0.9))
    cleaned_data=cleaned_data[:clean_num]
    
    return cleaned_data

