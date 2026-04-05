travel_log={
    "India":["Delhi","himachal Pradesh","Uttrakhand","Shimla"],
    " Germeny":["Stuttgart","Berlin","tokyo"]
}

#print(travel_log[" Germeny"][2])

nested_list= ["A","B",["C","D",["Deepak","Manish","Rohit",["palak","nikki"]]]]
#print(nested_list[2][2][3][0])

nested_dict={
    "India":{
        "Delhi":["Ghitorni","Arjan Garh","Qutab Minaar","Chattarpur"],
        "HP":["solan","shimla","Kasauli","Baddi"]
    },
    "Germeny":{
        "Berlin":["city1","city2","city3"]

    }
}
print(nested_dict["India"]["HP"][1])