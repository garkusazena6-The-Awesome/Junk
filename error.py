import warnings
warnings.simplefilter('ignore',UserWarning)
warnings.simplefilter('always',ImportWarning)
warnings.warn("Warning! Program NoCode",UserWarning)
warnings.warn("Warning! No imported module",ImportWarning)
"""
words_list= ["Olexij","Artem","Sofija","Dmitro","Vanya","Evgen"]
try:
    index = int(input("Enter index of word: "))
    word = words_list[index]
    print("Word from index ",index," :",word)
except ValueError:
    print("Entered value aint no number")
except IndexError:
    print("Whoa your index is out of charts")
"""
"""
try:
    chisl = int(input("Enter your chislenuk: "))
    znam = int(input("Enter your znamenuk: "))
    rez = chisl / znam
    print("Resultat:",rez)
except ValueError:
    print("Your inputed data aint no number")
except ZeroDivisionError:
    print("Are yo sick dividing zero")
"""
"""
class Error(Exception):
    def __str__(self):
        return f"With help of recent amount of material we aint building that house"
def perevirka_mat(amount_mat,limit):
        if amount_mat > limit:
            return print("You got enough of those materials")
        else:
            raise Error(amount_mat)
materials = 500
perevirka_mat(materials,499)
"""
"""
def perevirka(str_1):
    if type(str_1) != str:
        raise TypeError(f"This type zminnoi"f"{type(str_1)} not string")
    else:
        return str_1
str_2 = "123"
print(perevirka(str_2))
"""