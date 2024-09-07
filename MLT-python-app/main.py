import string


class MotrebiLanguage:
    
    def translate(word:str):
        system_letters = ["آ","ا","ع"]
        new_word = ""
        words = word.split(" ")
        for i in words:
            first_leter = i[0]
            if i[0] not in system_letters:
                print(i[0])
                first_leter = i[0]
                new_word = i.replace(first_leter,"ا")
                new_word += new_word.join(first_leter)
                new_word += new_word.join("و")
                print(new_word)
            elif i[0] in system_letters:
                first_leter = i[0]
                new_word = i.replace(first_leter,"ش")
                new_word += new_word.join(first_leter)
                new_word += new_word.join('و')
                print(new_word)

