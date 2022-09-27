from __init__ import *
root = Root()
root.nameroot("intro")
def ok():
    root.destroy()
hello = Text(root, text="hello and welcome to cone core\ndo what you want ,ok\nthis is your first favorate code now\n you will love it", font="report", fg="red")
oks = button(root, text="ok", bg="orange", fg="white", font=90, width="20",height=2, command=ok)
hello.pack()
oks.pack()
mainloop()