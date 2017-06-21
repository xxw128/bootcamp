def seq_concat(a, b, **kwargs):
    """concatenate sequences."""
    seq = a + b
    #print('test')
    for key in kwargs:
        seq += kwargs[key]
    return seq
