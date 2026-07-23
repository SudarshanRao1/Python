s = "education"

vowels = "aeiou"
count = 0

for ch in s:
    if ch.lower() not in vowels:
        count += 1
        
print("consonants=" , count)
