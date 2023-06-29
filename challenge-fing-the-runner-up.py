# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':

    n = int(input())
    arr = map(int, input().split(" "))
    lista_sorted = sorted(arr)

    # print(lista_sorted, type(lista_sorted))
    res = []
    [res.append(i) for i in lista_sorted if i not in res]
    # print(res)


    maximo = max(res)
    # print(maximo)
    index = res.index(maximo)

    res.pop(index)
    # print(res)
    print(res[-1])
    
