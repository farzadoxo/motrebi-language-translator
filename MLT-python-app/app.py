from tkinter import Tk as TK
from tkinter import Label , Text , Button


bg_color = '#000000'
fg_color = '#ffffff'

# Define application window
app = TK()
# Window properties
app.title('🎷 MLT 0.1')
app.geometry('700x500')
app.resizable(False,False)
app.eval('tk::PlaceWindow . center')
app.configure(bg=bg_color)


header_label = Label(text="Welcome to MLT 👋",bg=bg_color,fg=fg_color,font=("Arial",18,'bold'))
header_line_label = Label(text="-------------------------------",bg=bg_color,fg='#3df67b',font=("Arial",18,'bold'))
input_label = Label(text="Input :",bg=bg_color,fg=fg_color,font=("Arial",13))
input_textbox = Text(width=41,height=20)
output_label = Label(text="Output :",bg=bg_color,fg=fg_color,font=("Arial",13))
output_textbox = Text(width=41,height=20)
translate_button = Button(text="TRANSLATE",bg='#f6a93d',
                          command=lambda:translate(text=input_textbox.get('1.0', 'end-1c')))


def translate(text:str):
        system_letters = ["آ","ا","ع"]
        new_word = ""
        resaultـwords = []
        resault = ""
        words = text.split(" ")
        for i in words:
            if i[0] not in system_letters:
                first_leter = i[0]
                new_word = i.replace(first_leter,"ا")
                new_word += new_word.join(first_leter)
                new_word += new_word.join("و")
                resaultـwords.append(new_word)
            elif i[0] in system_letters:
                first_leter = i[0]
                new_word = i.replace(first_leter,"ش")
                new_word += new_word.join(first_leter)
                new_word += new_word.join('و')
                resaultـwords.append(new_word)
        for j in resaultـwords:
            resault += f"{j} "
        
        output_textbox.delete('1.0','end')
        output_textbox.insert('1.0',resault)



header_label.place(x=4,y=5)
header_line_label.place(x=4,y=35)
input_label.place(x=5,y=65)
input_textbox.place(x=7,y=90)
output_label.place(x=355,y=65)
output_textbox.place(x=357,y=90)
translate_button.place(x=120,y=444)




app.mainloop()