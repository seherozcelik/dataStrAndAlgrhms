def quicksort(l,low,high):
    if high<=low:
        print(l)
        return
    pivot = l[high]
    j = low
    for i in range(low,high):
        if l[i] < pivot:
            l[i],l[j] = l[j],l[i]
            j += 1              
    l[high],l[j] = l[j],l[high]
    quicksort(l,low,j-1)
    quicksort(l,j+1,high)
  
#quicksort(list,0,len(list)-1)
