#sets in pythons 

# set1 = {1,2,{3,4}}

# using frozenset to achieve nested sets 

# Creating a set with frozensets inside
nested_set = {frozenset({1, 2}), frozenset({3, 4})}
print(nested_set)
# Output: {frozenset({1, 2}), frozenset({3, 4})}

# nadding elements to a nested set 
nested_set.add(frozenset({5,6}))
print(nested_set)


#iterating through nested sets
for inner_set in nested_set:
    print(inner_set)
    for element in inner_set:
        print(element, end=' ')
    print()
    
    
#converting between nested lists and nested sets

nested_list = [[1,2],[3,4],[5,6]]
nested_set = {frozenset(inner_list) for inner_list in nested_list}
print(nested_list)


#use cases for nested sets
coordinates = {frozenset({0,0}), frozenset({1,2}), frozenset({3,4})}
print(coordinates)