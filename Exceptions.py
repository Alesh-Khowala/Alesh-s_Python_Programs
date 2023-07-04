# a = ["A", "E", "G"]  
# try:  

#  for i in range( 4 ):  
#         print( "The index and element from the array is", i, a[i] )  
     
#  except:  
#       print ("Index out of range")

num = [3, 4, 5, 7]  
if len(num) > 3:  
    raise Exception( f"Length of the given list must be less than or equal to 3 but is {len(num)}" )