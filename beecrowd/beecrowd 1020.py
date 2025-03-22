#%%
n = int(input())

ano = 0
mes = 0
dia = 0

# ano = 365
# mes = 30
if n % 365 != 0:
    ano = n//365
    dif = ano*365
    n-=dif
    if n % 30 != 0:
        mes = n//30
        dif = mes*30
        n-=dif
        dia = n
    else:
        mes = n
else:
    ano = n


print(ano, "ano(s)")
print(mes, "mes(s)")
print(dia, "dia(s)")
# %%
