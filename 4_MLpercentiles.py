# what are Percentiles? : 
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

# the numpy module has a method for finding the specified percentile:
import numpy as np
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
sharad = np.percentile(ages, 75)
print(sharad)

# what is the age of 90% people younger than?
import numpy as np
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
sharad = np.percentile(ages, 90)
print(sharad)