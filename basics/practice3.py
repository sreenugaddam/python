Student_name = input("Enter student name")
Student_age = int(input("Enter student age"))
student_grade = int(input("Enter student grade"))
base_tution_fee = 10000
discount_percentage = 20
aca_rank = int(input("Enter student rank"))

if student_grade<= 12:
  print ("Student grade is:"+ str(student_grade))
else:
  print ("Student grade is inavlid")

if student_grade>=9 and student_grade<=12 and aca_rank==1:
   discount = base_tution_fee/100*80
   print("20 percent discount.Tution fee after discount is:"+ str(discount))
else:
   discount = base_tution_fee/100*90
   print("10 percent discount.Tution fee after discount is:"+ str(discount))


