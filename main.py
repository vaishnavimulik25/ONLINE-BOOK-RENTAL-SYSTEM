from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
# Add your own database name and password here to reflect in the code
mypass = "test"
mydatabase="vaishnavi"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same=True
n=6.0

# Adding a background image
background_image =Image.open("library_img.jpeg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.15)

headingLabel = Label(headingFrame1, text="Welcome to COEP\n BOOK STORE", bg='white', fg='black', font=('ARIAL',40,"bold"))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.1,rely=0.28,relwidth=0.8,relheight=0.13)

headingLabel = Label(headingFrame1, text="The only true equalizers in the world are books\nThe only treasure house open to all comers is a library\nThe only wealth which will not decay is wisdom", bg='powder blue', fg='black', font=('Courier',25))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Book Details",bg='yellow', fg='black',font=('ARIAL',20,"bold"), command=addBook)
btn1.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='yellow', fg='black',font=('ARIAL',20,"bold"), command=delete)
btn2.place(relx=0.28,rely=0.55, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="Available Books",bg='yellow', fg='black',font=('ARIAl',20,"bold"), command=View)
btn3.place(relx=0.28,rely=0.65, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book",bg='yellow', fg='black',font=('ARIAL',20,"bold"), command = issueBook)
btn4.place(relx=0.28,rely=0.75, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book",bg='yellow', fg='black',font=('ARIAL',20,"bold"), command = returnBook)
btn5.place(relx=0.28,rely=0.85, relwidth=0.45,relheight=0.1)

root.mainloop()
