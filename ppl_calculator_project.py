from tkinter import *


root=Tk()
root.geometry("570x600+100+200")
#When you run the application, you’ll observe that the position and size both are changed. Now the Tkinter window is appearing at a different position (100 shifted on Y-axis and 200 shifted on X-axis).
root.title("Simple Calculator - PPL LAB ")#sets title to window , replaces default tk as title

root.resizable(False,False)     #root.resizeable(height=none,width=none)-> In resizable() method user can pass either positive integer or True, to make the window resizable.-> To make window non-resizable user can pass 0 or False.

root.configure(bg="#17161b")#configure - to arrange or make desirable chnages in something


# globally declare a expression variable
expression=""
def show(val):
    global expression #Variables that are created outside of a function (as in all of the examples above) are known as global variables.
    expression+=val
    Label_top.config(text=expression)
    # If you want to configure the Label widget, you can use the configure() property. The configure() method allows you to edit the text as well other properties of the Label widget dynamically.
    # so here what happens is whenever user clicks that button where show() func is called , it will run command and update the text in expression by val



def clear():
    global expression
    expression=""
    Label_top.config(text=expression)


def calculate():
    global expression
    result=""
    if expression!="":
        try:
            result=eval(expression)
        except:
            result="error"
            expression=""
    Label_top.config(text=result)




Label_top=Label(root,text="",height=2,width=25,font=("arial",30))
Label_top.pack()

Button(root,text="AC",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#99ff43",command=lambda: clear()).place(x=10,y=100)
# bd is border width in pixels (bydefault value is 2)
# fg is normal foreground colour 
# bg is normal background color
# .place() method organizes widget by placing them on specific positions as directed by programmer
Button(root,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#404040",command=lambda: show("/")).place(x=150,y=100)
Button(root,text="%",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#404040",command=lambda: show("%")).place(x=290,y=100)
Button(root,text="*",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#404040",command=lambda: show("*")).place(x=430,y=100)

# SECOND ROW
Button(root,text="DEL",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#99ff43").place(x=10,y=200)
Button(root,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#404040",command=lambda: show("7")).place(x=150,y=200)
Button(root,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#404040",command=lambda: show("8")).place(x=290,y=200)
Button(root,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#404040",command=lambda: show("9")).place(x=430,y=200)

# THIRD ROW
Button(root,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#404040",command=lambda: show("-")).place(x=10,y=300)
Button(root,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#404040",command=lambda: show("4")).place(x=150,y=300)
Button(root,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#404040",command=lambda: show("5")).place(x=290,y=300)
Button(root,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#404040",command=lambda: show("6")).place(x=430,y=300)

# FOURTH ROW
Button(root,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#404040",command=lambda: show("+")).place(x=10,y=400)
Button(root,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#404040",command=lambda: show("1")).place(x=150,y=400)
Button(root,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#404040",command=lambda: show("2")).place(x=290,y=400)
Button(root,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#404040",command=lambda: show("3")).place(x=430,y=400)

# FOURTH ROW
Button(root,text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#404040",command=lambda: show(".")).place(x=10,y=500)
Button(root,text="!",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#404040",command=lambda: show("!")).place(x=150,y=500)
Button(root,text="0",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#404040",command=lambda: show("0")).place(x=290,y=500)
Button(root,text="=",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#ffffff",bg="#FF8C00",command=lambda: calculate()).place(x=430,y=500)

# command - function or method to be called whenever button is clicked 


root.mainloop()