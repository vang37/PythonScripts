def max_subarray(row):
    largest_ending_here = 0
    best_start = this_start = end = best_so_far = 0
    for i, x in enumerate(row):
# i is the counter, x is row element
# if array = [4,5,6] enumerate(array) returns (i = 0,x = 4),(i=1,x=5),(i=2,x=6)
#
#
        largest_ending_here += x
# i = 0, x =4, largest_ending_here = 4
# i = 1, x =5, largest_ending_here = 9
# i = 2, x =6, largest_ending_here = 15

        best_so_far = max(best_so_far, largest_ending_here)
# step 0; best_so_far = max(0, 4) = 4
# step 1; best_so_far = 4, max(4, 9) = 9
# step 2; best_so_far = 9, max(9, 15) = 15
        if largest_ending_here <= 0:
            this_start = i + 1
            largest_ending_here = 0

# step 0; Is largest_ending_here == best_so_far? (t)
# step 1; Is largest_ending_here == best_so_far? (t)
# step 2; Is largest_ending_here == best_so_far? (t)
        elif largest_ending_here == best_so_far:
# step 0; best_start = this_start = 0, 0 = 0
# step 1; best_start = this_start = 0, 
# step 2; best_start = this_start = 0

            best_start = this_start
# end = 1
            end = i + 1 # the +1 is to have 'end' be exclusive
    
    return best_so_far, best_start, end

string = [5, -9, 8, 7, -6]
result = max_subarray(string)
print(result)