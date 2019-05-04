
def sortlist(lista):
    n=len(lista)
    for i in range(n):
        for j in range(1,n-i):
            if lista[j-1]>lista[j]:
                (lista[j-1],lista[j])=(lista[j],lista[j-1])
    return lista
'''
if __name__=='__main__':
    mylist=[64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]
    print("Before Sorting: ")
    print(mylist)
    sort_mylist=sortlist(mylist)
    print("After Sorting: ")
    print(sort_mylist)
'''
