import tkinter as tk
from tkinter import *
from tkinter.font import *

win =Tk()
win.geometry("1000x600")
win.title("shop bill management")

smallfont  = Font(family='Consolas',size=25,weight='bold')
largefont  = Font(family='Consolas',size=50,weight='bold')

#QUANTITIY VARIABLES
GULAHMEDQT =0
GRACEQT =0
WASHISNGWEARQT =0
PASHAHCOTTONQT =0
IT_COTTONQT =0
CUTPIECEQT =0
SOFTCOTTONQT=0


#PRICEVARAIBLES 
GULAHMEDPRICE =0
GRACEPRICE =0
WASHISNGWEARPRICE =0
PASHAHCOTTONPRICE =0
IT_COTTONPRICE =0
CUTPIECEPRICE =0
SOFTCOTTONPRICE =0

#TOTAL AMOUNT QUANTITI WISE VARAIABLES

GULAHMED_TOTAL_AMOUNT = GULAHMEDPRICE * GULAHMEDQT
GRACE_TOTAL_AMOUNT   =    GRACEPRICE * GRACEQT
WASHISNGWEAR_TOTAL_AMOUNT = WASHISNGWEARPRICE * WASHISNGWEARQT
PASHAHCOTTON_TOTAL_AMOUNT = PASHAHCOTTONPRICE * PASHAHCOTTONQT
IT_COTTON_TOTAL_AMOUNT =IT_COTTONPRICE * IT_COTTONQT
CUTPIECE_TOTAL_AMOUNT = CUTPIECEPRICE * CUTPIECEQT
SOFTCOTTON_TOTAL_AMOUNT= SOFTCOTTONPRICE * SOFTCOTTONQT






SUBTOTALAMOUNT  = GULAHMED_TOTAL_AMOUNT + GRACE_TOTAL_AMOUNT +WASHISNGWEAR_TOTAL_AMOUNT + PASHAHCOTTON_TOTAL_AMOUNT + IT_COTTON_TOTAL_AMOUNT + CUTPIECE_TOTAL_AMOUNT+ SOFTCOTTON_TOTAL_AMOUNT








for i in range(0,4):
    win.rowconfigure(i,weight=1)

for i in range(0,10):
    win.columnconfigure(i,weight=1)

Label(win,text="SHOP BILL MANGEMENT ",font=largefont,bg='black',fg= 'red').grid(row=0,column=0,sticky=NSEW,columnspan=4)
Label(win,text="QUALITY NAMES ",font=smallfont,bg='black',fg= 'red').grid(row=1,column=0,sticky=NSEW)
Label(win,text="QUANTITY ",font=smallfont,bg='black',fg= 'red').grid(row=1,column=1,sticky=NSEW)
Label(win,text="PRICE  ",font=smallfont,bg='black',fg= 'red').grid(row=1,column=2,sticky=NSEW)
Label(win,text="TOTAL ",font=smallfont,bg='black',fg= 'red').grid(row=1,column=3,sticky=NSEW)




lblgulahmed = Label(win,text='GUL AHMED COTTON',bg='black',fg='red',font=smallfont).grid(row =2,column =0,sticky=SW,pady=20)
entgulahmed_qt =Entry(textvariable=GULAHMEDQT,bg='black',fg='yellow',font=smallfont).grid(row=2,column=1,sticky=SW,padx=10)
entgulahmed_pr =Entry(textvariable=GULAHMEDPRICE,bg='black',fg='yellow',font=smallfont).grid(row=2,column=2,sticky=SW,padx=10)
lblgulahmed_am =Label(win,text=GULAHMED_TOTAL_AMOUNT,bg='black',fg='red',font=smallfont).grid(row=2,column=3,sticky=EW,padx=10)



lblgrace = Label(win,text='GRACE',bg='black',fg='red',font=smallfont).grid(row=3,column=0,sticky=SW,pady=10)
entgrace_qt =Entry(textvariable=GRACEQT,bg='black',fg='yellow',font=smallfont).grid(row=3,column=1,sticky=SW,padx=10)
entgrace_pr =Entry(textvariable=GRACEPRICE,bg='black',fg='yellow',font=smallfont).grid(row=3,column=2,sticky=SW,padx=10)
lblgrace_am =Label(win,text=GULAHMED_TOTAL_AMOUNT,bg='black',fg='red',font=smallfont).grid(row=2,column=3,sticky=EW,padx=10)



lblwashingwear = Label(win,text='WASHING WEAR NORMAL',bg='black',fg='red',font=smallfont).grid(row=4,column=0,sticky=SW,pady=10)
entwashingwear_qt =Entry(textvariable=WASHISNGWEARQT,bg='black',fg='yellow',font=smallfont).grid(row=4,column=1,sticky=SW,padx=10)
entwashingwear_pr =Entry(textvariable=WASHISNGWEARPRICE,bg='black',fg='yellow',font=smallfont).grid(row=4,column=2,sticky=SW,padx=10)
lblwashingwear_am =Label(win,text=WASHISNGWEAR_TOTAL_AMOUNT,bg='black',fg='red',font=smallfont).grid(row=4,column=3,sticky=EW,padx=10)


lblpashahcotton = Label(win,text='PASHAH COTTON',bg='black',fg='red',font=smallfont).grid(row=5,column=0,sticky=SW,pady =10)
entpashahcotton_qt =Entry(textvariable=PASHAHCOTTONQT,bg='black',fg='yellow',font=smallfont).grid(row=5,column=1,sticky=SW,padx=10)
entpashahcotton_pr =Entry(textvariable=PASHAHCOTTONPRICE,bg='black',fg='yellow',font=smallfont).grid(row=5,column=2,sticky=SW,padx=10)
lblpashahcotton_am =Label(win,text=PASHAHCOTTON_TOTAL_AMOUNT,bg='black',fg='red',font=smallfont).grid(row=5,column=3,sticky=EW,padx=10)


lblsoftcotton = Label(win,text='SOFT COTTON',bg='black',fg='red',font=smallfont).grid(row=6,column=0,sticky=SW,pady =10)
entsoftcotton_qt =Entry(textvariable=PASHAHCOTTONQT,bg='black',fg='yellow',font=smallfont).grid(row=6,column=1,sticky=SW,padx=10)
entsoftcotton_pr =Entry(textvariable=PASHAHCOTTONPRICE,bg='black',fg='yellow',font=smallfont).grid(row=6,column=2,sticky=SW,padx=10)
lblsoftcotton_am =Label(win,text=SOFTCOTTON_TOTAL_AMOUNT,bg='black',fg='red',font=smallfont).grid(row=6,column=3,sticky=EW,padx=10)



lblitcotton = Label(win,text='IT COTTON',bg='black',fg='red',font=smallfont).grid(row=7,column=0,sticky=SW,pady=10)
entitcotton_qt=Entry(textvariable=IT_COTTONQT,bg='black',fg='yellow',font=smallfont).grid(row=7,column=1,sticky=SW,padx=10)
entitcotton_pr=Entry(textvariable=IT_COTTONPRICE,bg='black',fg='yellow',font=smallfont).grid(row=7,column=2,sticky=SW,padx=10)
lblitcotton_am =Label(win,text=IT_COTTON_TOTAL_AMOUNT,bg='black',fg='red',font=smallfont).grid(row=7,column=3,sticky=EW,padx=10)

lblcutpiece = Label(win,text ='CUT PIECE ',bg='black',fg= 'red',font=smallfont).grid(row=8,column=0,sticky=SW,pady=10)
entcutpiece_qt =Entry(textvariable=CUTPIECEQT,bg='black',fg='yellow',font=smallfont).grid(row=8,column=1,sticky=SW,padx=10)
entcutpiece_pr =Entry(textvariable=CUTPIECEPRICE,bg='black',fg='yellow',font=smallfont).grid(row=8,column=2,sticky=SW,padx=10)
lblcutpiece_am =Label(win,text=CUTPIECE_TOTAL_AMOUNT,bg='black',fg='red',font=smallfont).grid(row=8,column=2,sticky=EW,padx=10)



Button(win,text= 'SUB_TOTAL',bg='black',fg='red',font=smallfont).grid(row=9,column=0,columnspan=2,sticky=NSEW,pady=10)
lblsubtotal_am =Label(win,text=SUBTOTALAMOUNT,bg='black',fg='red',font=largefont).grid(row=9,column=3,columnspan =2,sticky=EW,padx=10)

win.mainloop()