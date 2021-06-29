from tkinter import *
from PIL import Image, ImageTk


#globals
BLUE = 'white'
TEXT_COLOR = '#0000a4'
FONT = 'verdana'

#create window
window = Tk()
window.title("Bol.com Shop Alert")
window.config(padx=25, pady=12, bg=BLUE)

canvas = Canvas(width=250, height=150, bg=BLUE, highlightthickness=0)


# commands
def submit():
    url = e1.get()
    prijs = e2.get()
    email = e3.get()
    new_lijst = (url,prijs,email)
    print(new_lijst[0])
    return new_lijst


def quitting():
    window.quit()


# labels of GUI
label_url= Label(text="URL : ", bg=BLUE, highlightthickness=0, font=(FONT, 15, "bold"), fg=TEXT_COLOR)
label_url.grid(column=1, row=1)
e1 = Entry(window, show=None, font=('Arial', 14))
e1.grid(column=2, row=1)

label_melding_ontvangen_bij_deze_prijs = Label(text="Melding ontvangen bij deze prijs: ", bg=BLUE, highlightthickness=0, font=(FONT, 15, "bold"), fg=TEXT_COLOR)
label_melding_ontvangen_bij_deze_prijs.grid(column=1, row=2)
e2 = Entry(window, show=None, font=('Arial', 14))
e2.grid(column=2, row=2)

label_email = Label(text="Email: ", bg=BLUE, highlightthickness=0, font=(FONT, 15, "bold"), fg=TEXT_COLOR)
label_email.grid(column=1, row=3)
e3 = Entry(window, show=None, font=('Arial', 14))
e3.grid(column=2, row=3, padx=(10))


# buttons of GUI
button_start = Button(text="Submit", bg=BLUE, font=(FONT, 12, 'bold'), fg=TEXT_COLOR, command=submit, )
button_start.grid(column=2, row=5, columnspan=2, pady=(10))

button_quit = Button(text="Exit", bg=BLUE, font=(FONT, 12, 'bold'), fg=TEXT_COLOR, command=quitting, )
button_quit.grid(column=0, row=5, columnspan=2, pady=(10))

# image
house_img = PhotoImage(file="shopping-cart.png")
smaller_image = house_img.subsample(6, 6)
canvas.create_image(120, 75, image=smaller_image)
canvas.grid(column=1, row=0, columnspan=2)

window.quit()
window.mainloop()