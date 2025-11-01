from tkinter import*

root = Tk()

#creating function / logic
def Details():

        Name = str(S_N.get()) 
    
        rSn.set(Name)

        rollnum = int(Roll_num.get())
        
        rRn.set(rollnum)
       
        SPN = int(ph_num.get()) 
        
        rPn.set(SPN)
        
        SEI = str(E_I.get())
        
        rEI.set(SEI)
        
        SB = str(S_B.get())
        
        rSb.set(SB)
        
        SS = str(S_S.get())
        
        rSs.set(SS)
        
        
        SA = str(S_A.get())
        
        rSa.set(SA)
        
        SJM = int(S_JM.get())
        
        rJM.set(SJM)
#grade for Java marks
        if SJM >= 90:
        
            grd="A"
            rGJ.set(grd)
        
        elif SJM >= 80 :
        
            grd="B"
            rGJ.set(grd)
        elif SJM >=70 :
        
            grd="C"
            rGJ.set(grd)
        elif SJM >=60:
        
            grd="D"
            rGJ.set(grd)
        elif SJM >=35:
            grd="E"
            rGJ.set(grd)
        elif SJM <35:
            grd="F"
            rGJ.set(grd)
        
#grade for dotnet marks        
        SDNM = int(S_DNM.get())
        
        rDM.set(SDNM)
        
        if SDNM >= 90:
        
            grd="A"
            rDJ.set(grd)
        
        elif SDNM >= 80 :
        
            grd="B"
            rDJ.set(grd)
        elif SDNM >=70 :
        
            grd="C"
            rDJ.set(grd)
        elif SDNM >=60:
        
            grd="D"
            rDJ.set(grd)
        elif SDNM >=35:
            grd="E"
            rDJ.set(grd)
        elif SDNM <35:
            grd="F"
            rDJ.set(grd)
#grade for Web development marks            
        SWBM = int(S_WBM.get())
        
        rWM.set(SWBM)
        
        if SWBM >= 90:
        
            grd="A"
            rWD.set(grd)
        
        elif SWBM >= 80 :
        
            grd="B"
            rWD.set(grd)
        elif SWBM >=70 :
        
            grd="C"
            rWD.set(grd)
        elif SWBM >=60:
        
            grd="D"
            rWD.set(grd)
        elif SWBM >=35:
            grd="E"
            rWD.set(grd)
        elif SWBM <35:
            grd="F"
            rWD.set(grd)
            
        SDBM = int(S_DBM.get())
        
        rDBM.set(SDBM)
#grade for DBMS marks

        if SDBM >= 90:
        
            grd="A"
            rDG.set(grd)
        
        elif SDBM >= 80 :
        
            grd="B"
            rDG.set(grd)
        elif SDBM >=70 :
        
            grd="C"
            rDG.set(grd)
        elif SDBM >=60:
        
            grd="D"
            rDG.set(grd)
        elif SDBM >=35:
            grd="E"
            rDG.set(grd)
        elif SDBM <35:
            grd="F"
            rDG.set(grd)
                  
        SPM =int(S_PM.get())
        
        rPM.set(SPM)
#grade for Python marks
        if SPM >= 90:
        
            grd="A"
            rPG.set(grd)
        
        elif SPM >= 80 :
        
            grd="B"
            rPG.set(grd)
        elif SPM >=70 :
        
            grd="C"
            rPG.set(grd)
        elif SPM >=60:
        
            grd="D"
            rPG.set(grd)
        elif SPM >=35:
            grd="E"
            rPG.set(grd)
        elif SPM <35:
            grd="F"
            rPG.set(grd)
#end of marks and grade section  
    
        Total_Marks = (SJM+SDNM+SWBM+SDBM+SPM) 
        rTM.set(Total_Marks)
        if SJM >=35 and SDNM>=35 and SWBM>=35 and SDBM>=35 and SPM>=35:
            if 450<=Total_Marks<=500:
                grd="A"
                resofG.set(grd)
        
            elif 400<=Total_Marks<=450:
                grd="B"
                resofG.set(grd)
            elif Total_Marks>=350 :
        
                grd="C"
                resofG.set(grd)
            elif Total_Marks>=300:
        
                grd="D"
                resofG.set(grd)
            elif Total_Marks >=175:
                grd="E"
                resofG.set(grd)
            
        else:
            grd="F"
            resofG.set(grd)
            
        if grd=="A" or grd=="B" or grd=="C" or grd=="D" or grd=="E" :
            res="PASS"
            result.set(res)
        else:
            res="FAIL"
            result.set(res)
        
        
        avg = (Total_Marks/5)
        
        rSA.set(avg)
        
        
        
#2.Creating window size and title
root.title("Student Records")

root.geometry("1920x1080")

#result functions:
rSn=StringVar()

rRn=StringVar()

rPn=StringVar()

rEI=StringVar()

rSb=StringVar()

rSs=StringVar()

rSa=StringVar()

rJM=StringVar()

rDM=StringVar()

rWM=StringVar()

rDBM=StringVar()

rPM=StringVar()

rTM=StringVar()

rGJ=StringVar()

rDJ=StringVar()

rWD=StringVar()

rDG=StringVar()

rPG=StringVar()

rSA=StringVar()

resofG=StringVar()

result=StringVar()


#3.Creating window label

Label(root,text="Enter Student Name:").grid(row=0, column=1)

Label(root,text="Enter Student Roll Number:").grid(row=1, column=1)

Label(root,text="Enter Student Phone Number:").grid(row=2, column=1)

Label(root,text="Enter Student Email ID:").grid(row=3, column=1)

Label(root,text="Enter Student Branch:").grid(row=4, column=1)

Label(root,text="Enter Student Section:").grid(row=5, column=1)

Label(root,text="Enter Student Address : ").grid(row=6, column=1)

Label(root,text="==========ENTER STUDENT MARKS========== ").grid(row=7, column=1)

Label(root,text="Enter Student Java Marks : ").grid(row=8, column=1)

Label(root,text="Employee Student Dot Net Marks : ").grid(row=9, column=1)

Label(root,text="Enter Student Web development Marks:").grid(row=10, column=1)

Label(root,text="Enter Student Database Marks:").grid(row=11, column=1)

Label(root,text="Enter Student python Marks:").grid(row=12, column=1)
#4.Creating text boxes

S_N = Entry(root)
S_N.grid(row=0, column=2)

Roll_num = Entry(root)
Roll_num.grid(row=1, column=2)

ph_num = Entry(root)
ph_num.grid(row=2, column=2)

E_I = Entry(root)
E_I.grid(row=3, column=2)

S_B = Entry(root)
S_B.grid(row=4, column=2)

S_S = Entry(root)
S_S.grid(row=5, column=2)

S_A = Entry(root)
S_A.grid(row=6, column=2)

S_JM = Entry(root)
S_JM.grid(row=8, column=2)

S_DNM = Entry(root)
S_DNM.grid(row=9, column=2)

S_WBM = Entry(root)
S_WBM.grid(row=10, column=2)

S_DBM = Entry(root)
S_DBM.grid(row=11, column=2)

S_PM = Entry(root)
S_PM.grid(row=12, column=2)


#5.Creating Button

Button(root, text="Submit", command=Details).grid(row=31, column=10)


#6.Result which prints given details
Label(root, text="Student Name:").grid(row=14, column=0)
Label(root, text="", textvariable=rSn).grid(row=14, column=1)

Label(root, text="Student Roll Number:").grid(row=14, column=2)
Label(root, text="", textvariable=rRn).grid(row=14, column=3)

Label(root, text="Student Phone Number:").grid(row=14, column=4)
Label(root, text="", textvariable=rPn).grid(row=14, column=5)

Label(root, text="Student Email:").grid(row=15, column=0)
Label(root, text="", textvariable=rEI).grid(row=15, column=1)

Label(root, text="Student Branch:").grid(row=15, column=2)
Label(root, text="", textvariable=rSb).grid(row=15, column=3)

Label(root, text="Student Section:").grid(row=15, column=4)
Label(root, text="", textvariable=rSs).grid(row=15, column=5)

Label(root, text="Student Address:").grid(row=16, column=0)
Label(root, text="", textvariable=rSa).grid(row=16, column=1)

#gap for marks of the subjects

Label(root, text="==========STUDENT MARKS==========").grid(row=17, column=0)

Label(root, text="Student Java Marks:").grid(row=18, column=0)
Label(root, text="", textvariable=rJM).grid(row=18, column=1)
Label(root,text="Grade:").grid(row=18, column=3)
Label(root, text="", textvariable=rGJ).grid(row=18, column=4)

Label(root, text="Student Dot Net Marks:").grid(row=19, column=0)
Label(root, text="", textvariable=rDM).grid(row=19, column=1)
Label(root,text="Grade:").grid(row=19, column=3)
Label(root, text="", textvariable=rDJ).grid(row=19, column=4)

Label(root, text="Student Web Development Marks:").grid(row=20, column=0)
Label(root, text="", textvariable=rWM).grid(row=20, column=1)
Label(root,text="Grade:").grid(row=20, column=3)
Label(root, text="",textvariable=rWD).grid(row=20,column=4)

Label(root, text="Student Database Marks:").grid(row=21, column=0)
Label(root, text="", textvariable=rDBM).grid(row=21, column=1)
Label(root,text="Grade:").grid(row=21, column=3)
Label(root, text="", textvariable=rDG).grid(row=21, column=4)

Label(root, text="Student python Marks:").grid(row=22, column=0)
Label(root, text="", textvariable=rPM).grid(row=22, column=1)
Label(root,text="Grade:").grid(row=22, column=3)
Label(root, text="", textvariable=rPG).grid(row=22, column=4)

#applying gaps for total marks and average

Label(root, text="==========TOTAL MARKS AND AVERAGE AND GRADE==========").grid(row=23, column=0)


Label(root, text="Student Total Marks:").grid(row=24, column=0)
Label(root, text="", textvariable=rTM).grid(row=24, column=1)

Label(root, text="Over all Grade :").grid(row=28, column=0)
Label(root, text="", textvariable=resofG).grid(row=28, column=1)

Label(root, text="Student Average is:").grid(row=26, column=0)
Label(root, text="", textvariable=rSA).grid(row=26, column=1)

Label(root, text="Result = ").grid(row=30, column=1)
Label(root, text="",textvariable=result).grid(row=30, column=2)

mainloop()