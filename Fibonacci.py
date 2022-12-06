from tkinter import *
root=Tk()
root.title("fibonaci")
root.geometry("400x400")


label_series=Label(root,text="fiboncci series")
label_flower=Label(root)
label_spiral=Label(root)

def fibonaci():
  num=10
  first_no=0
  second_no=1
  sum=0
  conter=0
  while(conter<=num):
     label_series["text"]+=str(sum)+" "
     conter=conter+1
     first_no=second_no
     second_no=sum
     sum=first_no+second_no
  label_flower["text"]=0+1+1+2+3+5+8+13+21+24


btn=Button(root,text="show fibonaci serirs",command=fibonaci)
btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()


mainloop()
