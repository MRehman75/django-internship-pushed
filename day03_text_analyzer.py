#ans q9:
#      In Python, string slicing lets you extract part of a string using the syntax: string[start:stop:step]
#      text = "Hello World"
#       H  e  l  l  o     W  o  r  l  d
#       0  1  2  3  4  5  6  7  8  9 10 [2-4-6 visuted]
#       out put "low" start from 2 then move two step one is 2 and second is 3 now reach 4 again move two step first 4 move then 5 move reach to 6 so now we stop before 8
#ans q10:
#        both are string method but do diff working 
#        .replace() replace one sub string with another and return a new string string.replace(old, new)
#        .split() breake string into pieces using seprator and return a list of string text = "apple,banana,orange"
#         result = text.split(",")
#         print(result) output ['apple','banana','orange']
#ans q11:
#        .strip() method removes unwanted characters from the beginning and end of a string. By default, it removes whitespace such as spaces,
#        tabs (\t), and newlines (\n).
#        1. clean user inputs 2.process data from files 3.validating form and web data 4.cleaning CSV and database data
#ans q12:
#        f"{12.3456:.2f}" out put 12.34
#        
from collections import Counter
sentence=input("enter a sentence with atleast 10 words : ").strip()
if len(sentence.split()) <10:
    print("please enter sentence with minimum 10 words")
    
else:
    print("\n ======ALL CASE CONVERSION======")
    print("UPPER CASE: ", sentence.upper())
    print("lower case: ", sentence.lower())
    print("Title case: ",sentence.title())
    print("sentence case: ",sentence.capitalize())
    
    print("\n ===CHAR COUNT===")
    print("charcter with space ", len(sentence))
    print("cahrcter with out space", len(sentence.replace(" ","")))
    
    print("\n ===WORD COUNRT===")
    print("total word: ", len(sentence.split()))
    
    print("\n ===REVISED SENTENCE CHAR BY CHAR===")
    print(sentence[::-1])
    
    print("\n ===VOWELS * - === ")
    vowel_replaced =""
    for char in sentence:
        if char.lower() in "aeiou":
            vowel_replaced +="*"
        else:
            vowel_replaced +=char
    print(vowel_replaced)
    
    print("\n ===PLANDROME CHECK===")
    cleaned="".join(sentence.lower().split())
    if cleaned== cleaned[::-1]:
        print("the sentence is pllidrome .")
    else:
        print("the sentence is not a plidrome.")
    
    print("\n===MOST COMMAN CHAR IN SENTENCE===")
    chars=[c.lower() for c in sentence if not c.isspace()]
    common=Counter(char).most_common(3)
    for char, count in common:
        print(f"'{chars}' appear {count} times")
    
    print("\n ===SEARCHED WORD===")
    searched_word=input("enter a word you want to search: ").strip()
    words=sentence.split()
    positions=[]
    for index, word in enumerate(words):
        if word.lower()==searched_word.lower():
            positions.append(index)
    
    print(f"{searched_word} appear {len(positions)} times. ")
    
    if positions:
        print("words position in index",positions)
    else:
        print("word not found")    
            
    
         
    