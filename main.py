from wordGenerator import wordGenerator
# Bu kod, hangi harften sonra hangi harflerin gelmemesi gerektiği bilgisi eklenerek güncellenmeli. Böylelikle
# oluşturulacak olan yeni kelimeler, kişilerin belirlediği kısıtlama sayesinde farklı karakteristiklere sahip olacaktır.


def getInput():
    print("Please write the length of random word that you want to create: ")
    inp = int(input())
    return inp


class main:
    def __init__(self):
        word_length = getInput()
        self.new_generator = wordGenerator(word_length)


main()
