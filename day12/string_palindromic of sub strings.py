def string_palindromic(string):
    i,j,sub_list=0,1,[]
    while j<=len(string):
        sub_string=string[i:j]
        sub_string_rev=sub_string[::-1]
        if sub_string==sub_string_rev:
            sub_list.append(sub_string)
        if j==len(string):
            i+=1
            j=i+1
        else:
            j+=1
    print(sub_list)
    return len(max(sub_list,key=len)),len(sub_list)
string_input=input()
result=string_palindromic(string_input)
print("the maximum len of sub_string palindrome = ",result[0])
print("the total no.of sub_string palindrome = ",result[1])