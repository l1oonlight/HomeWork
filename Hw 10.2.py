import pandas as pd
import numpy as np

v1 = pd.Series(np.arange(0, 8, 2))
v2 = pd.Series(np.arange(2, 10, 1))
print(v1, v2)
st = set.union(set(v1), set(v2))
result = pd.Series(list(st))
print(result)