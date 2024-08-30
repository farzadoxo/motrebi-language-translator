import string


class MotrebiLang:
    
    def translate(word:str):
        new_word = ""
        words = word.split(" ")
        for i in words:
            first_leter = i[0]
            if i[0] != "ا" or "آ" :
                first_leter = i[0]
                new_word = i.replace(first_leter,"ا")
                new_word += new_word.join(first_leter)
                new_word += new_word.join("و")
                print(new_word)
            elif i[0] == "ا" or "آ" or "ع":
                first_leter = i[0]
                new_word = i.replace(first_leter,"ش")
                new_word += new_word.join(first_leter)
                new_word += new_word.join('و')
                print(new_word)


MotrebiLang.translate("سلام علیکم ")