# Python program to validate an Email

# import re module

# re module provides support
# for regular expressions
import re

# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Define a function for
# for validating an Email


def check(email):

	# pass the regular expression
	# and the string into the fullmatch() method
	if(re.fullmatch(regex, email)):
		print("Valid Email")

	else:
		print("Invalid Email")


# Driver Code
if __name__ == '__main__':

	# Enter the email
	email = "ankitrai326@gmail.com"

	# calling run function
	check(email)

	email = "my.ownsite@our-earth.org"
	check(email)

	email = "ankitrai326.com"
	check(email)
