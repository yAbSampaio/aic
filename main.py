#coding= utf -8
from process import*
from cell import*
from memory import*
import time
#------------------------VarGlobais------------------------------------#
atual_clock = 0
t_apply = 0
t_wait = 0
t_fail = 0
t_medio = 0

#------------------------inicialização---------------------------------#

proce = open("process.txt","r")
List = []
list_proc = []
Memo = mem_virtual()
choice = 0
for i in proce : #padronização do arquivo
    line=i.split("\n")[0]
    cell = line.split(" ")
    List.append(cell)
    
for i in List: #cria lista de classe processo
    Var = process(int(i[0]),int(i[1]),int(i[2]),int(i[3]))
    list_proc.append(Var)
list_proc = sorted(list_proc, key = process.get_arr)
choice = int(input("Digite\n1 - First Fit\n2 - Best Fit\n3 - Worst Fit\n"))

#---------------------------------------------------------------#
n_wait = 0
while (Memo.get_len() != 1 or n_wait < len(list_proc)):#Enquato haver processo na lista 
    if(n_wait < len(list_proc)):
        para = n_wait
        while ((n_wait < len(list_proc)) and (list_proc[para].get_arr() <= atual_clock)):#Fazer lista de espera
            #Chamada da função first, best worst
            if(choice == 1):
                if (Memo.FirstFit(list_proc[n_wait],atual_clock)):
                    n_wait += 1#Espera
                else:
                    t_fail += 1
                para += 1
            elif(choice == 2):
                if(Memo.BestFit(list_proc[n_wait],atual_clock)):
                    n_wait += 1#Logica de t wait
                else:
                    t_fail += 1
                para += 1
            else:
                #Memo.WorstFit(list_proc[n_wait],atual_clock)
                n_wait += 1
                
    for i in range(len(list_proc)):
        if atual_clock == list_proc[i].get_end():
            Memo.out_proce(list_proc[i])
            #list_proc[i].pop()
    print("-------------")
    print("clock: "+str(atual_clock))
    Memo.printf()
    print("------")
    print("\n")
    atual_clock += 1
print("Numero de falhas "+ str(t_fail))