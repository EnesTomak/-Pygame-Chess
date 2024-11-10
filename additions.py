import numpy as np
from functools import reduce

num_list= np.arange(10)
filter_list = list(filter(lambda x:x %3 ==0 , num_list))

final_list = reduce(lambda x ,y: x*y,filter_list )

print(final_list)