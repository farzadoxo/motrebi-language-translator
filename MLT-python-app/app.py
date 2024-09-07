from tkinter import Tk as TK
from tkinter import Button , Label , Text

bg_color = '#000000'
fg_color = '#ffffff'


app = TK()

app.title("🎷 MLT 0.1")
app.geometry('600x400')
app.iconbitmap('')
app.eval('tk::PlaceWindow . center')
app.configure(bg=bg_color)
app.resizable(False,False)

header_label = Label(text="Welcome to MLT 👋",fg=fg_color,bg=bg_color,font=('Helvetica',20))
header_line_label = Label(text="-----------------------------",fg=fg_color,bg=bg_color,font=('Helvetica',20))
input_textbox_label = Label(text="Input :",bg=bg_color,fg=fg_color,font=('Helvetica',12))
output_textbox_label = Label(text="Output :",bg=bg_color,fg=fg_color,font=('Helvetica',12))
input_textbox = Text(width=35,height=13)
output_textbox = Text(width=35,height=13)
# output_textbox.config(state='disabled')
resault_label = Label(text="",bg=bg_color,fg=fg_color)
translate_button = Button(text="TRANSLATE",bg='#fc931d',
                          command=lambda:translate(text=input_textbox.get("1.0",'end-1c')))


def translate(text:str):
        system_letters = ["آ","ا","ع"]
        new_word = ""
        words = text.split(" ")
        for i in words:
            first_leter = i[0]
            if i[0] not in system_letters:
                first_leter = i[0]
                new_word = i.replace(first_leter,"ا")
                new_word += new_word.join(first_leter)
                new_word += new_word.join("و")
                output_textbox.insert('1.0',new_word)
            elif i[0] in system_letters:
                first_leter = i[0]
                new_word = i.replace(first_leter,"ش")
                new_word += new_word.join(first_leter)
                new_word += new_word.join('و')
                output_textbox.insert('1.0',new_word)




header_label.place(x=4,y=7)
header_line_label.place(x=4,y=34.5)
input_textbox_label.place(x=4,y=65)
input_textbox.place(x=5,y=85)
output_textbox_label.place(x=300,y=65)
output_textbox.place(x=300,y=85)
translate_button.place(x=100,y=325)



app.mainloop()