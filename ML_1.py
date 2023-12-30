
###########################################################
def task1():
    import numpy as np
    s = np.double(input("Введите температуру: "))
    if(s > 28): print("ЖАРКО")
    elif(s < 15.5): print("ХОЛОДНО")
    else: print("НОРМАЛЬНО")
##############################################################
def task2():
    import numpy as np
    n=int(input("Число строк: "))
    str = [[]]*n
    word1 = "Кот"
    word2 = "кот"
    k = 0
    print(str)
    for i in range(n):
        str[i] = input()
        if(int(str[i].find(word1))  != -1 or int(str[i].find(word2) != -1)): k+=1


    if(k>0): print("\nМЯУ")
    else: print("\nНЕТ")

##############################################################
def task3():
    list = []
    while(1):
        s=input()
        if(s=="стоп"): break
        list.append(s)

    max_len=max(list, key=len)
    min_len=min(list, key=len)

    if(set(max_len)&set(min_len) == set(min_len)): print("\nДА")
    else: print("\nНЕТ")
##################################################
def task4():
    arr = []
    n=int(input("Число покупок: "))
    for i in range(n):
        arr.append((input()))
    
    print("\n".join(arr))
################################################
def task5():
    s = input()
    for i in s:
        print(2 * i, end='')
#############################################
def task6():
    def  greet():
        list=[]
        for i in range(2):
            list.append(input())
        print("Здравствуйте,", " ".join(list))

    greet()
########################################
class LittleBell:
    def sound(self):
        print("ding")

def task7():
    bell=LittleBell()
    bell.sound()

########################################

# task1()
# task2() 
# task3()
# task4()  
# task5()
# task6()   
# task7()