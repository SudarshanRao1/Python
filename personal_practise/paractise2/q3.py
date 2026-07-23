s = "madam"

rev = "" .join(reversed(s))

if s == rev:
    print("palindrome")
else:
    print("not palindrome")