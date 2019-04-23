"""
Ransom note: This is a fucntion that takes two list and sees if the second list
is a subset of the first specifically. The original problem is that a thief using a magazine as his corpus,
can only use the words in the mag, and lower case letters are considered different words


"""


def checkMagazine(magazine: list, note: list) -> str:


    magazine_dict = {x: magazine.count(x) for x in magazine}
    word_dict = {x: note.count(x) for x in note}
    print(word_dict)
    for word in word_dict:
        if word not in magazine_dict:
            print("No")
            return
        if magazine_dict[word] < word_dict[word]:
            print("No")
            return
        
    print("Yes")





if __name__ == "__main__":
    print(checkMagazine(["one", "fish", "two", "fish", "red", "fish", "blue", "fish"], ["fish", "two", "two","red"]))