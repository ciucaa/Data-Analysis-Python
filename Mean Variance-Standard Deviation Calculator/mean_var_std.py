import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    a=np.array(list).reshape((3, 3))
    b=np.chararray.flatten(a)
    #print(a)
    mean_list=[np.mean(a,0).tolist(), np.mean(a, 1).tolist(), np.mean(b)]
    var_list=[np.var(a,0).tolist(), np.var(a,1).tolist(), np.var(b)]
    stdev_list=[np.std(a,0).tolist(), np.std(a,1).tolist(), np.std(b)]
    max_list=[np.max(a,0).tolist(), np.max(a,1).tolist(), np.max(b)]
    min_list=[np.min(a,0).tolist(), np.min(a,1).tolist(), np.min(b)]
    sum_list=[np.sum(a,0).tolist(), np.sum(a,1).tolist(), np.sum(b)]

    calculations={
        'mean': mean_list,
        'variance': var_list,
        'standard deviation': stdev_list,
        'max': max_list,
        'min': min_list,
        'sum': sum_list
        }
    return calculations




