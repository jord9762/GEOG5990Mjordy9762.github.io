---
title: Jordys coding website
---

 <b>Exercise 19 learn python the hard way <b>
def cheese_and_crackers(cheese_count, boxes_of_crackers, grapes):#colon must be there for code to work
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Also have {grapes} grapes")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
#The def function cheese and crackers is essentially saying when the words cheese and crackers are put into the code the following variables need to 
#be assigned. The lines after are interpolaring the line to tell python that variables will appear in this string. Line 5 is just a text string.
#Line 6 makes a gap at the end of line 6, known as an escape sequence.
print("We can just give the function numbers directly:")
cheese_and_crackers
#This is telling the code that cheese is 20, crackers 30 and grapes 70, these will be assigned into the string starting in line 2
print("OR, we can use variables from our script:")
amount_of_cheese = int(input())
amount_of_crackers = int(input())
amount_of_grapes = int(input())
#These int inputs were an addition to the excercise, add this to my conversion exercise!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#This is directly assiging the individual variables from the script, looks inefficient compared with line 11's method
cheese_and_crackers(amount_of_cheese, amount_of_crackers, amount_of_grapes)
#Because variables were assigned on lines 14-16, the code on line 18 becomes possible.
print("We can even do math inside too:")Ragu6697
cheese_and_crackers(10 + 20, 5 + 6, 4+5)
#line 21 is doing a maths calculation for each respective variable. In the order cheese, crackers and then grapes
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000, amount_of_grapes + 900)
#Finally line 24 adds the following numbers to the intergers assigned to each respective variable, on lines 14-16
