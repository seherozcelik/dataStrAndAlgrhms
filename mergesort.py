def mergesort(l):
    if len(l)<=1:
        return l
    mid = len(l) // 2
    left = l[:mid]
    right = l[mid:]
    
    sortedleft = mergesort(left)
    sortedright = mergesort(right)

    return merge(sortedleft,sortedright)
    
def merge(left,right):    
    merged = []
    for i in range(max(len(left),len(right))):
        if left[i]<right[i]:
            merged.append(left[i])
            merged.append(right[i])
        else:
            merged.append(right[i])
            merged.append(left[i])
    print(merged)        
    return merged        

#mergesort(list)
