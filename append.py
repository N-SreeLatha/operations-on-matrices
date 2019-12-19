#appending elements into an array
import numpy as np
a=np.array(input("enter the elements for the first array:"))
b=np.array(input("enter the elements for the second array:"))
print("the first array is:",a)
print ("the second array is:",b)
l=len(b)
for i in range(0,l):
	a=np.append(a,b[i])
print("the new array formed by appending the terms in array b into array a:",a)
