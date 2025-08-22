#store temperatures of 7 days for 3 cities, then analyze using indexing, slicing, data types, and copy vs view.
import numpy as np
#create array (7 days * 3 ,cities :Kurunagala, Mathara ,Colombo)
temp= np.array([
    [30,32,28,31,29,33,34], #Kurunagala
    [25,27,26,28,29,30,31], #Mathara
    [35,36,34,33,37,38,36], #Colombo
])

print("Temperatures(Rows = Cities, Columns = Days):\n",temp)
#indexing -Temp of  Kurunagala on day 3
print("\n Kurunagala ,day 3 Temperature : ",temp[0,2])

#clicing - all temperatures of Mathara

print("\n All temps of  Mathara",temp[1,:])

"""
output:

Temperatures(Rows = Cities, Columns = Days):
 [[30 32 28 31 29 33 34]
 [25 27 26 28 29 30 31]
 [35 36 34 33 37 38 36]]

 Kurunagala ,day 3 Temperature :  28

 All temps of  Mathara [25 27 26 28 29 30 31]


"""