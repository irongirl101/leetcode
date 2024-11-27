#have 2 pointers, one in needle, one in haystack
#pointer stays at needle[0] until pointer at haystack sees needle[0]
#then, pointer moves through both haystack and needle. if needle reaches the end without it stopping, get the index when it first hits the haystack 
#else, it breaks, and the pointer at the needle restarts at needle[0], and process repeats again 

haystack='true'
needle='sadbuttrue'

j=0 #needle pointer
index=[]
if len(haystack)>len(needle):
    for i in range(len(haystack)):
        if j<len(needle) and i+1<len(haystack):
            if haystack[i]==needle[j] and haystack[i+1]!=needle[j]:
                index.append(i)
                j+=1
            elif haystack[i]==needle[j] and haystack[i+1]==needle[j]:
                i+=1

            else:
                j=0
                index=[]
    if index!=[]:
        print(index[0])
    else:
        print(-1)

else:
    print('Needle longer than haystack')




#in this code, it doesnt work if the letters all start with the beginning of the needle, works for other scenarios tho 