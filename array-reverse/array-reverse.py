test =  [1,2,3,4,5,6]

def reverse_arr(list):
    rev_list=[]
    for i in range(len(list)-1,-1,-1):
        rev_list.append(list[i])
    print(rev_list)
reverse_arr(test)