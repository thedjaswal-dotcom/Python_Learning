def calculate_love_score(name1,name2):
    criteria=["t","r","u","e"]
    sum_criteria=0
    
    criteria_2=["l","o","v","e"]
    sum_criteria2=0
    
    final_name=name1+name2
   
    
    for i in range(len(criteria)):
        for letter in final_name:
            if criteria[i] == letter:
             
             sum_criteria+=1

    for i in range(len(criteria_2)):
     for letter in final_name:
      if criteria_2[i] == letter:
              
               sum_criteria2+=1 
    
    final_score=str(sum_criteria)+str(sum_criteria2)
    print(final_score)
                
calculate_love_score("Kanye West", "Kim Kardashian")

