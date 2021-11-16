import math

array = [ 1, 10, 3, 11, 6, 15 ]
n = len( array )
sum_array = []
min_sum = math.inf

for index in range ( 0, len(array) ) :
    key = array [ index ]
    if key not in sum_array : sum_array . append ( key )
    for i in range ( index + 1 , len(array) ) :
        temp = key + array [ i ]
        if temp not in sum_array : sum_array . append ( temp )

# merge sort due to lower time complexity
# this is because the resultant sum_array is too long
def re_arrange ( array1, array2 ) :
    ans = []
    index1 = 0
    index2 = 0
    while ( index1 < len( array1 ) and index2 < len( array2 ) ) :
        if array1 [ index1 ] > array2 [ index2 ] :
            ans.append ( array2 [ index2 ] )
            index2 += 1
        elif array1 [ index1 ] < array2 [ index2 ] :
            ans.append ( array1 [ index1 ] )
            index1 += 1
        else:   # array1 [ index1 ] == array2 [ index2 ] :
            ans.append ( array1 [ index1 ] )
            ans.append ( array2 [ index2 ] )
            index1 += 1
            index2 += 1
            
        if index1 == len( array1 ) :
            while index2 != len ( array2 ) : 
                ans.append ( array2 [ index2 ] )
                index2 += 1
        elif index2 == len ( array2 ) : 
            while index1 != len ( array1 ) : 
                ans.append ( array1 [ index1 ] )
                index1 += 1
                
        if len( ans ) == len ( array1 ) + len ( array2 ) : break
    return ( ans )
    
def separate ( array ) :
    if ( len(array) > 1 ) : 
        middle_index = int( 1 + ( len(array)-1) /2 )
        ans1 = separate ( array [ : middle_index ] )
        ans2 = separate ( array [ middle_index : ] )
        ans = re_arrange ( ans1 , ans2 )
        return ( ans )
    return ( array )
    
sum_array = separate ( sum_array )

for index in range ( 0 , n-1 ) :
    if sum_array[index] != index+1 : 
        min_sum = index+1
        print ( min_sum )
        break