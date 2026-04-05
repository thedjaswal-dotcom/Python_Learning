'''a book it is '''
''' A Book It Is '''



def to_title(f_name):
    capital_f_name=""
    char_arry=[]
    for word in f_name: 
        char_arry.append(word)
    lenght_arry=len(char_arry)
    capital_f_name+=char_arry[0].upper()
    for a in range(1,lenght_arry):
        if char_arry[a].isupper():
          char_arry[a]=char_arry[a].lower()
          capital_f_name+=char_arry[a]
        else:
             capital_f_name+=char_arry[a]            
    return capital_f_name


new=to_title("ramesh")
print(new)
    
text =" hist is a radnom string WIth CaPtial WoRd in BetWeen"

def final_function(text):
 new_text=text.split()
 format=""
 for i in range(len(new_text)):
     format+=to_title(new_text[i])
     format+=" "
 return format

my_value=final_function("THis isd FYunny Iam KHAFNL")
print(my_value)


    



   










            













        