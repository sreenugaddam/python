Student_name = input("Enter student name:")
Student_age = int(input("Enter student age:"))
stud_grd = int(input("Enter student grade:"))
base_tution_fee = 10000
aca_rank = int(input("Enter student acadamic rank:"))

Tdiscount = base_tution_fee

if stud_grd>=9 and stud_grd<=12:
    if aca_rank==1:
        discount = base_tution_fee/100*20
        print("discount is"+str(discount))
        Tdiscount = base_tution_fee-discount
        print("Tution fee after discount is:"+ str(Tdiscount))
    else:
        discount = base_tution_fee/100*10
        print("discount is"+str(discount))
        Tdiscount = base_tution_fee-discount
        print("Tution fee after discount is:"+ str(Tdiscount))
elif stud_grd>=6 and stud_grd<=8:
    discount = base_tution_fee/100*5
    print("discount is"+str(discount))
    Tdiscount = base_tution_fee-discount
    print("Tution fee after discount is:"+ str(Tdiscount))
elif stud_grd>12:
    print ("Student grade is inavlid")
else:
    print("No discount")

match stud_grd:
     case 10:
      Ediscount=Tdiscount/100*3
      print("Extra discount:"+str(Ediscount))
      Fdiscount=Tdiscount-Ediscount
      print("Final discount:"+str(Fdiscount))
     case 12:
      Ediscount=Tdiscount/100*5
      print("Extra discount:"+str(Ediscount))
      Fdiscount=Tdiscount-Ediscount
      print("Final discount:"+str(Fdiscount))

print(Student_name)
print(stud_grd)
print(Student_age)
print(Tdiscount)
print(Fdiscount)
        

        


