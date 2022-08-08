# Check Number Palindrome Or Not

num = int(input("Enter The Number: "))
numO = num
revnum = 0
while num != 0:
    digit = num % 10
    num2 = num // 10
    num = num2
    revnum = revnum * 10 + digit
print(revnum)

if numO == revnum:
    print(f"{numO} is Palindrome..")
else:
    print(f"{numO} Is Not Palindrome..")
