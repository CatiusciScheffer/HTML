import pandas as pd;


qte = int(input())

for i in range(qte):
    A = list(input().split())
    B = list(input().split())
    
    if A[-len(B):] == B[-3:]:
        print("encaixa")
    else:
        print("nao encaixa")