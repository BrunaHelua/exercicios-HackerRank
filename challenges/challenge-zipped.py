# https://www.hackerrank.com/challenges/zipped/problem

a = input().strip().split(" ")
n = int(a[0])
x = int(a[1])

kk = []
for i in range(0, x):
    ll = input().strip().split(" ")
    kk.append(ll)
    #print(kk[i])

hello = zip(*kk)

soma = 0
for obj in hello:
    for y in obj:
    # print(f'aluno {x} com as notas {y}')
        soma = soma + float(y)
    print(soma/x)
    soma = 0
