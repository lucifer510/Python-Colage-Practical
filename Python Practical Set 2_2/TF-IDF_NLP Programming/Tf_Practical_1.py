# Write regular expression code to varify email address.

import re

email = input("Enter your email address: ")
if re.match(r"^[a-zA-Z\d_.+-]+@[a-zA-Z\d]+\.[a-zA-Z\d.]+$", email):
    print("Valid email address")
else:
    print("Invalid email address")

