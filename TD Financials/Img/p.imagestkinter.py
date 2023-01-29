from tkinter *
from PIL import Image,ImageTk 
root=Tk()
root.title('Photo Viewer')
root.iconbitmap('apple.ico')

Img1 = ImageTk.PhotoImage(Image.open("Bristol Myers.jpg"))
label = label(root,image = img1)
label.pack()

Button_quit = Button(root, text = "Exit Image", command = quit_file)
Button_quit.pack()

root.mainloop()