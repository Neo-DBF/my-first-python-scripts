from unittest.util import sorted_list_difference


def add(a, b):
    return a % b

# Вызов функции и вывод результата в консоль
result = add(93, 5)
#доработаем код никиты
L=bin(result)[2:]
if L.count("1")%2==1:
    L=L+L.replace("1","0")
if L.count("0")%2==0:
    L=L+bin(L.count("0"))[2:]
    Q=int(L, 2)
    if Q>5:
        print(Q,"%", "мой вклад в этот код")
        print("94%", "твой вклад в этот код")
        print(L, "Твой примерный айкью")

print("никита пошел нафиг"  * 100)
#тут кончается тот код что мы писали с тобой и начинается то что хочу сказать тебе я
for N in range(1, 100):
    s=bin(N)[2:]
    if N%2==0:
        sm=sum(int(c) for c in s)
        s=s.replace("0","1")
        s="100"+s[2:]+ bin(s.count('1'))[2:]+bin(sm)[2:]+"10101011"
    R=int(s , 2)
    if R>0:
        print(N*100,"%", "то на сколько ты умница")
        print(R*100, "%", "то насколько ты совершенен")
        print(int(s*8, 2) , "%" , "то на сколько я в тебя верю")
        break
