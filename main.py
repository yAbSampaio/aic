#coding= utf-8
#from graphic import*
from process import*
from memory import*
import time
#------------------------VarGlobais------------------------------------#
atual_clock = 0
t_apply = 0
t_wait = 0 #t_inicio_clock - t_chegada
t_fail = 0 #tentativas falhas
t_medio = 0 
n_wait = 0

#------------------------inicialização---------------------------------#

proce = open("process.txt","r")
List = []
list_proc = []
Memo = mem_virtual()
choice = 0
choice = int(input("Digite\n1 - First Fit\n2 - Best Fit\n3 - Worst Fit\n"))
t_medio = time.time()
for i in proce : #padronização do arquivo
    line=i.split("\n")[0]
    cell = line.split(" ")
    List.append(cell)
    
for i in List: #cria lista de classe processo
    Var = process(int(i[0]),int(i[1]),int(i[2]),int(i[3]))
    list_proc.append(Var)
list_proc = sorted(list_proc, key = process.get_arr)

#---------------------------------------------------------------#

#Arruma logica de parada
while (Memo.get_len() != 1 or n_wait < len(list_proc)):#Enquato haver processo na lista 
    #if(n_wait < len(list_proc)):
    par = True
    while (n_wait < len(list_proc) and (list_proc[n_wait].get_arr() <= atual_clock) and par):#Fazer lista de espera
        #Chamada da função first, best worst
        if(choice == 1):

            if(Memo.FirstFit(list_proc[n_wait],atual_clock)):
                t_wait += atual_clock-list_proc[n_wait].get_arr()
                n_wait += 1
            else:
                control = False

        elif(choice == 2):

            if(Memo.BestFit(list_proc[n_wait],atual_clock)):
                t_wait += atual_clock-list_proc[n_wait].get_arr()
                n_wait += 1#Logica de t wait
            else:
                control = False
        
        elif(choice == 3):

            if(Memo.WorstFit(list_proc[n_wait],atual_clock)):
                t_wait += atual_clock-list_proc[n_wait].get_arr()
                n_wait += 1#Logica de t wait
            else:
                control = False
                
    for i in range(len(list_proc)):
        if atual_clock == list_proc[i].get_end():
            Memo.out_proce(list_proc[i])
    
    print("-------------")
    print("clock: "+str(atual_clock))
    Memo.printf()
    #l=input("Test")
    print("-------------")
    print("\n")
    atual_clock += 1
    #Memo.graph(atual_clock)
print("Numero de falhas "+ str(t_wait))
a = t_wait/n_wait
t_medio = time.time()-t_medio
print("Numero medio de espera "+str(a))
print("tempo de execução "+str(t_medio))
