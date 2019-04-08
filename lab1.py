
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if not int_list:    
        if int_list is None:
            raise ValueError('list is None')
        return None
    result = int_list[0]
    for element in int_list:
        if element > result:
            result = element
    return result
    

def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError("List is None")
    if len(int_list) <= 1:
        return int_list
    return [int_list[-1]] + reverse_rec(int_list[:-1])      
    

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   pass
