import numpy as np
td = {'Sunny': 0.8, 'Rainy': 0.19,
                             'Snowy': 0.01}


print(list(td.values()))
print(list(td.keys()))

print(np.random.choice(list(td.keys()), p=list(td.values()) ))


