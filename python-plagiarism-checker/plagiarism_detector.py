from tkinter import*
from winsound import *

import tkinter.messagebox
import re
from datetime import datetime
import time


database=""
search=""
answer="Result here"
calculation=0
color=""
answer=""
need=0
play_it=False






#====================================================================================================================================================

def get_database():
    

    database1=""
    database1file=open("database.txt","r")
    database1_list=database1file.readlines()
    
    for lines in database1_list:
        for words in lines:
            if words=="\n":
                word=" "           
            database1=database1+words
    window.txtReciept.insert("1.0",database1)
    database1file.close()

def get_search():
    search1=""
    search1file=open("search.txt","r")
    search1_list=search1file.readlines()
    
    for lines in search1_list:
        for words in lines:
            if words=="\n":
                word=" "           
            search1=search1+words
    window.txtReciept1.insert("1.0",search1)
    search1file.close()
    
    
    
        



def put_database():
    database2=window.txtReciept.get("1.0","end-1c")
    if len(database2)>0:
        asking=tkinter.messagebox.askyesno("Relative Plagiarism Detector","Are you sure you want add this to database")
        if asking>0:
            database_put=open("database.txt","w")
            database_put.write(database2)
            database_put.close()
            
    else:
        show=tkinter.messagebox.showinfo("Relative Plagiarism Detector","There is nothing in the database box")

    
    



def put_search():
    search2=window.txtReciept1.get("1.0","end-1c")
    if len(search2)>0:
        asking=tkinter.messagebox.askyesno("Relative Plagiarism Detector","Are you sure you want add this to search")
        if asking>0:
            search_put=open("search.txt","w")
            search_put.write(search2)
            search_put.close()
    else:
        show=tkinter.messagebox.showinfo("Relative Plagiarism Detector","There is nothing in the search box")
    
    
    

def append_database():
    database2=window.txtReciept.get("1.0","end-1c")
    if len(database2)>0:
        asking=tkinter.messagebox.askyesno("Relative Plagiarism Detector","Are you sure you want add this to database")
        if asking>0:
            database_put=open("database.txt","a")
            database_put.write(database2)
            database_put.close()
    else:
        show=tkinter.messagebox.showinfo("Relative Plagiarism Detector","There is nothing in the search box")


def append_search():
    search2=window.txtReciept1.get("1.0","end-1c")
    if len(search2)>0:
        asking=tkinter.messagebox.askyesno("Relative Plagiarism Detector","Are you sure you want to add this to search")
        if asking>0:
            search_put=open("search.txt","a")
            search_put.write(search2)
            search_put.close()
    else:
        show=tkinter.messagebox.showinfo("Relative Plagiarism Detector","There is nothing in the search box")
    
    
    


    
    
    

def reset():
    
    asking=tkinter.messagebox.askyesno("Relative Plagiarism Detector","Are you sure you want to reset the boxes")
    if asking>0:
        window.txtReciept.delete("1.0",END)
        window.txtReciept1.delete("1.0",END)

def check_for_update():
    tkinter.messagebox.showinfo("Relative Plagiarism Detector","No updates available\nThis is the final version")

    
    

def exit_it():
    asking=tkinter.messagebox.askyesno("Relative Plagiarism Detector","Are you sure you want to exit it")
    if asking>0:
        exit()




def about():
    import tkinter.messagebox
    tkinter.messagebox.showinfo("Relative Plagiarism Detector","This is a program made by Jalees Mukarramm, Hassaan Ali and Mamnoon Hussnain used to detect relative plagiarism between two text")


def playsound1():
    PlaySound('safe level.wav', SND_FILENAME)

def playsound2():
    PlaySound('risky level.wav', SND_FILENAME)

def playsound3():
    PlaySound('hard level', SND_FILENAME)

def playsound4():
    PlaySound('full level.wav', SND_FILENAME)



#======================================================================================================================================


    

def database():
    global database
    global search
    global answer
    global calculation
    global color
    global counter
    global need
    global play_it
    answer="" 
    
    



    database=window.txtReciept.get("1.0","end-1c")
    search=window.txtReciept1.get("1.0","end-1c")

    database=database.lower()


    variable=""
    for every in database:
        if every==" ":
            continue
        else:
            variable=variable+every

    print("\n"*2)
    list_1=[]
    list_2=[]
    list_3=[]
    list_4=[]
    list_5=[]
    list_6=[]
    list_7=[]

    final_list=[]

    string=""


    search=search.lower()
    checker=""
    for every in search:
        if every==" ":
            continue
        else:
            checker=checker+every
    
    
    if len(checker)==0:
        answer=("Nothing to compare for Plagiarism")
        print("Nothing to compare")






    elif checker==variable and len(checker)>0:
        answer="Total plagiarism is 100%"
        color="Red"
        calculation=100
        print("lenghth of checker is: ",len(checker))
        print("Got result at the earliest")
        play_it=True



    elif re.search(checker,variable) and len(checker)>0:
        answer="Total plagiarism is 100%"
        color="Red"
        print("Got result from partial")
        calculation=100
        play_it=True
        


    else:
        for every in search:
            if every==" " and string!="" and len(string)>0:
                list_1.append(string)
                string=""
            elif string.isspace():
                string=""

            else:
                string=string+every
        list_1.append(string)
        need=1
        

        print("below is list 1")
        print(list_1)
       
           

        

#========================================================================================================================================


    def domore():
        global answer
        global need
        global calculation
        global play_it



        string=""

        print("\n"*2)


        time_runner2=0
                

        for entry in list_1:
            string=string+entry
            list_2.append(string)

        print("below is list 2")
        print(list_2)
        print("\n"*2)


        string=""
        counter1=0

        for every in list_1:
            string=string+every
            counter1+=1
            if counter1%2==0:
                list_3.append(string)
                string=""
        list_3.append(string)

        print("below is list 3")
        print(list_3)
        print("\n"*2)



        string=""
        counter2=0
        for every in list_3:
            string=string+every
            counter2+=1
            if counter2%2==0:
                list_4.append(string)
                string=""
        list_4.append(string)


        print("here is list 4")
        print(list_4)
        print("\n"*2)



        string=""
        counter5=len(list_1)-1
        for every in list_1:
            list_5.append(list_1[counter5:len(list_1)])
            counter5-=1


        print(list_5)
        print("\n"*2)



        string=""
        for every in list_5:
            for entries in every:
                string=string+entries
            list_6.append(string)
            string=""

        print("list 6 here......")
        print(list_6)


        print("\n"*2)




        final_list=list_1+list_2+list_3+list_4+list_6

        final_list=list(set(final_list))
        print("here is final list")
        print(final_list)
        print("\n"*5)




        found=0
        for every in final_list:
            if len(every)>1:
                if re.search(every,variable):
                    print("This is found: ",every)
                    print("\n")
                    found+=1

        print("Calculating Result")
        if len(list_1)>0:
            plagiarism=round(found/len(final_list)*100,2)
            answer=("Total plagiarism is "+str(plagiarism)+"%")
            calculation=found/len(final_list)*100
        else:
            print("Length of final list: ",len(final_list))


        print("words found: ",found)
        print("Got result after long calculation steps")
        print("total percentage: ",found/len(final_list)*100)
        print("Length of final list: ",len(final_list))
        print("now calculation is: ",found/len(final_list)*100)
        need=0
        play_it=True
        print("here is checker: ",checker)
        







        

        


    
#gere
    if need>0:
        if 0<=len(list_1)<300:
            domore()
               
        if 300<=len(list_1)<1000:
            continue_it=tkinter.messagebox.askyesno("Relative Plagiarism Detector","The search text shows that it will take upto 2 minutes {}. Do you want to continue?".format(len(list_1)))
            if continue_it>0:
                domore()
        
        elif len(list_1)>=1000:
            continue_it=tkinter.messagebox.askyesno("Relative Plagiarism Detector","The search text shows that it will take upto 5 minutes {}. Do you want to continue?".format(len(list_1)))
            if continue_it>0:
                domore()
                
        
            



    
    result_box=Label(abc6,text=answer,bg="orangered",fg="Yellow",font="none 16 bold")
    result_box.grid(row=0,column=0)


    if play_it==True:
        if 0<=calculation<30:
            playsound1()
            


        if 30<=calculation<50:
            playsound2()
            

        if 50<=calculation<80:
            playsound3()
            

        if 80<=calculation<=100:
            playsound4()
            



    calculation=0
    play_it=False
    print("reseted",play_it)
    print(len(list_1))
        
        
        
    




#==================================================================================================================================================
window=Tk()
window.title("Relative Plagiarism Detector")
window.geometry("1040x690+120+0")
window.configure(background="navy")
window.iconbitmap("title.ico")

abc=Frame(window,bg="olivedrab1",bd=10,relief=RAISED,width=400)
abc.grid(row=0)
abc1=Frame(abc,bd=12,width=600,height=50,padx=3,pady=4,relief=RAISED,bg="orangered")
abc1.grid(row=0,column=0,columnspan=3,sticky=N)

abc2=Frame(abc,bd=15,width=600,height=10,padx=1,bg="olivedrab1")
abc2.grid(row=1,column=0,sticky=N)

abc3=Frame(abc,bd=10,width=600,height=30,padx=3,relief=RIDGE,bg="olivedrab1")
abc3.grid(row=2,column=0,sticky=N)


abc4=Frame(abc,bd=10,width=600,height=10,padx=1,bg="olivedrab1")
abc4.grid(row=3,column=0,sticky=N)

abc5=Frame(abc,bd=10,width=600,height=50,padx=3,relief=RIDGE,bg="olivedrab1")
abc5.grid(row=4,column=0,sticky=N)

abc6=Frame(abc,bd=10,width=600,height=50,padx=3,bg="olivedrab1")
abc6.grid(row=5,column=0,sticky=N)

abc7=Frame(abc,width=600,height=50,bg="olivedrab1")
abc7.grid(row=6,column=0,sticky=N)








#==========================================================================================================================================================================

Date1=StringVar()
Time1=StringVar()
Date1.set(time.strftime("%d/%m/%y"))
Time1.set(time.strftime("%H:%M:%y"))

#===========================================================================================================================================================


window.lbltitle=Label(abc1,text="                     Relative Plagiarism detector                      ",
                      font=("Georgia",22,"bold"),fg="sienna1",bg="ivory2",pady=9,bd=6).grid(row=0,column=1)

window.lbltitle=Label(abc1,textvariable=Date1,font=("algerian", 22,"bold"),fg="blue2",bg="ivory2",pady=9,bd=6).grid(row=0,column=0)

window.lbltitle=Label(abc1,textvariable=Time1,font=("algerian",22,"bold"),fg="blue2",bg="ivory2",pady=9,bd=6).grid(row=0,column=5)

window.lbltitle=Label(abc2,text="Enter Database here",font=("Georgia",17,"bold"),fg="red2",bg="olivedrab1").grid(row=1,column=0)

window.txtReciept=Text(abc3,bd=10,width=70,height=4,font=("Georgia",14,"bold"),fg="red",bg="lightblue1")
window.txtReciept.grid(row=0,column=0)


window.lbltitle=Label(abc4,text="Enter Search text here",font=("Georgia",17,"bold"),fg="red2",bg="olivedrab1").grid(row=1,column=0)

window.txtReciept1=Text(abc5,bd=14,width=70,height=4,font=("Georgia",14,"bold"),fg="red",bg="lightblue1")
window.txtReciept1.grid(row=0,column=0)












#==========================================================================================================================================================


button_for_start=Button(abc7,font=("Algerian 16 bold"),text="Check Plagiarism",bg="cyan",height=2,width=20,command=database)
button_for_start.grid(row=0,column=2)


button_for_reset=Button(abc7,text="Reset",command=reset,bg="goldenrod1",height=1,width=15)
button_for_reset.grid(row=1,column=0)

button_for_exit=Button(abc7,text="Exit",command=exit_it,bg="goldenrod1",height=1,width=15)
button_for_exit.grid(row=1,column=4)









#command=lambda:[database(),playsound()]
#===========================================================================================================================================================

Main_Menu=Menu(window)
window.config(menu=Main_Menu)

first_Sub_Menu=Menu(Main_Menu)

Main_Menu.add_cascade(label="Options",menu=first_Sub_Menu)

first_Sub_Menu.add_separator()
first_Sub_Menu.add_command(label="Import Database",command=get_database)
first_Sub_Menu.add_command(label="Import Search",command=get_search)
first_Sub_Menu.add_command(label="Import Both",command=lambda:[get_database(),get_search()])

first_Sub_Menu.add_separator()
first_Sub_Menu.add_command(label="Export Database",command=put_database)
first_Sub_Menu.add_command(label="Expoer Search",command=put_search)
first_Sub_Menu.add_command(label="Export Both",command=lambda:[put_database(),put_search()])

first_Sub_Menu.add_separator()
first_Sub_Menu.add_command(label="Append Database",command=append_database)
first_Sub_Menu.add_command(label="Append Search",command=append_search)
first_Sub_Menu.add_command(label="Append Both",command=lambda:[append_database(),append_search()])

first_Sub_Menu.add_separator()



first_Sub_Menu.add_command(label="Exit",command=exit_it)



second_Sub_Menu=Menu(Main_Menu)
Main_Menu.add_cascade(label="Help",menu=second_Sub_Menu)

second_Sub_Menu.add_command(label="About",command=about)
second_Sub_Menu.add_command(label="Check for Update",command=check_for_update)






Status_Bar=Label(abc,text="Relative Plagiarism Detector \t\t\t\t\t\t\t  © All rights reserved \t\t\t Jalees Mukarram |||  Hassaan Ali ||| Mamnoon Hussnain",bd=1,bg="floralwhite",relief=SUNKEN,anchor=W)
Status_Bar.grid(row=10)
#================================================================================================================================================================

#
result_box=Label(abc6,text="RESULT",bd=5,bg="orangered",fg="Yellow",font="none 16 bold",width=30)
result_box.grid(row=0,column=0)




window.mainloop()



