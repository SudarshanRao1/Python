# fibonaci series
# fibonacci series
a, b = 0, 1
count = 0

# Change 10 to your desired number of terms
while count < 10:
    print(a, end=" ")  # Added a space for readability
    a, b = b, a + b
    count += 1
