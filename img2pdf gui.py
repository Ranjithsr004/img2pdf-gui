from tkinter import *
from tkinter.filedialog import askopenfilenames
import img2pdf
root = Tk()
root.geometry('1080x1260')
root.title("ImageToPDF")
root.bg("red")
def select_file():
	global file_names
	file_names=askopenfilenames(initialdir="/",title="Select Files")
def images_to_pdf():
	with open(f"file.pdf","wb") as f:
		f.write(img2pdf.convert(file_names))

Label(root, text="IMAGE CONVERSION", font="italic 15 bold").pack(pady=10)
Button(root, text="Select Images", relief="solid",command=select_file,bg="red", font=14).pack(pady=10)
Button(root,text="Images  To PDf",relief ="solid",command=images_to_pdf,bg="green",font=14).pack(pady=10 )
root.mainloop()