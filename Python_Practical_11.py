# Write a program to create a dictionary of student details and perform basic operation on
# it.
d1 = {"Mihir":"200220131002","Mobin":"200220131010","Vrushti":"200220131005","Yashvi":"200220131021"}

# To Add Element In Dictionary
d1.update({"Smit":"200220131075"})


# For Printing Dictionary.
# Meth-1
print(d1)

# To Delete Element From Dictionary
d1.pop("Smit")

# Printing Meth-2
for key,value in d1.items():
    print(f"Student's Name is {key} And His/Her Enrollment Number Is {value}")