def quick_sort(lst):
    if len(lst)<1:
        return lst
    else:
        pv=lst[0]
        left_lst=[i for i in lst if i<pv]
        right_lst=[i for i in lst if i>pv]
        return quick_sort(left_lst)+[pv]+quick_sort(right_lst)
lst=list(map(int,input().split(" ")))
print(quick_sort(lst))