def common_elements(list1,list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result

        
        
        
        
print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
    
    

    
    
    
    