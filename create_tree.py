import json

def create_tree():
    with open("static/data/apt_floor_split.json","r") as f1:
        apt=json.load(f1)


    list1=[]
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    list6=[]
    list7=[]
    list8=[]
    list9=[]
    list10=[]
    list11=[]
    list12=[]
    list13=[]

    for num in range(315):
        for i in range(apt['house_type'][num]):
            if(apt['floor_plans'][num]['floor_type'][i]['bed'].lower()=="studio" and apt['floor_plans'][num]['price_range'][i]<1000 and "Dog Friendly" in apt['amenities'][num]):
                if num not in list1:
                    list1.append(num)
            if(apt['floor_plans'][num]['floor_type'][i]['bed'].lower()=="studio" and apt['floor_plans'][num]['price_range'][i]<1000 and "Dog Friendly" not in apt['amenities'][num]):
                if num not in list2:
                    list2.append(num)
            if(apt['floor_plans'][num]['floor_type'][i]['bed'].lower()=="studio" and apt['floor_plans'][num]['price_range'][i]>1000 and "Dog Friendly" in apt['amenities'][num]):
                if num not in list3:
                    list3.append(num)
            if(apt['floor_plans'][num]['floor_type'][i]['bed'].lower()=="studio" and apt['floor_plans'][num]['price_range'][i]>1000 and "Dog Friendly" not in apt['amenities'][num]):
                if num not in list4:
                    list4.append(num)
            if (apt['floor_plans'][num]['floor_type'][i]['bed'].lower() == "1bed" and apt['floor_plans'][num]['price_range'][i]< 1000 and "Dog Friendly" in apt['amenities'][num]):
                if num not in list5:
                    list5.append(num)
            if (apt['floor_plans'][num]['floor_type'][i]['bed'].lower() == "1bed" and apt['floor_plans'][num]['price_range'][i]< 1000 and "Dog Friendly"  not in apt['amenities'][num]):
                if num not in list6:
                    list6.append(num)
            if (apt['floor_plans'][num]['floor_type'][i]['bed'].lower() == "1bed" and apt['floor_plans'][num]['price_range'][i]> 1000 and "Dog Friendly" in apt['amenities'][num]):
                if num not in list7:
                    list7.append(num)
            if (apt['floor_plans'][num]['floor_type'][i]['bed'].lower() == "1bed" and apt['floor_plans'][num]['price_range'][i]> 1000 and "Dog Friendly" not in apt['amenities'][num]):
                if num not in list8:
                    list8.append(num)
            if (apt['floor_plans'][num]['floor_type'][i]['bed'].lower() == "2beds" and apt['floor_plans'][num]['price_range'][i]< 2000 and "Dog Friendly"  in apt['amenities'][num]):
                if num not in list9:
                    list9.append(num)
            if (apt['floor_plans'][num]['floor_type'][i]['bed'].lower() == "2beds" and apt['floor_plans'][num]['price_range'][i]< 2000 and "Dog Friendly"   not in apt['amenities'][num]):
                if num not in list10:
                    list10.append(num)
            if (apt['floor_plans'][num]['floor_type'][i]['bed'].lower() == "2beds" and apt['floor_plans'][num]['price_range'][i]> 2000 and "Dog Friendly"   in apt['amenities'][num]):
                if num not in list11:
                    list11.append(num)
            if (apt['floor_plans'][num]['floor_type'][i]['bed'].lower() == "2beds" and apt['floor_plans'][num]['price_range'][i]> 2000 and "Dog Friendly"   not in apt['amenities'][num]):
                if num not in list12:
                    list12.append(num)
    list13=list(range(315))
    list13=list(set(list13).difference(set(list1+list2+list3+list4+list5+list6+list7+list8+list9+list10+list11+list12)))






    question_tree=("Do you want a 1 bedroom house or studio?",
                        ("Do you want a studio?",
                            ("Is the rent less than 1000 per month",
                                ("Is it dog-friendly?",
                                    list1,list2),
                                ("Is it dog-friendly?",
                                    list3,list4)),
                            ("Is the rent less than 1000 per month",
                                ("Is it dog-friendly?",
                                    list5,list6),
                                ("Is it dog-friendly?",
                                    list7,list8))),
                        ("Do you want a 2 bed house?",
                            ("Is the rent less than 1000 per month",
                                ("Is it dog-friendly?",
                                    list9, list10),
                                ("Is it dog-friendly?",
                                    list11, list12)),
                            list13))
    return question_tree





if __name__=="__main__":
    tree=create_tree()
    with open("static/data/tree.txt","w") as f:
        f.write(str(tree))