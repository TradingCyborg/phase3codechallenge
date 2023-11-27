def solve(s):
    vowels = 'aeiou'
    consonant_substrings = []

    #Split he string into consonant substrings
    current_substring = ""
    for char in s:
        if char not in vowels:
            current_substring += char
        else:
            if current_substring:
                consonant_substrings.append(current_substring)
                current_substring = ""
    
    #Handle the last substring if it ends with a consonant
    if current_substring:
        consonant_substrings.append(current_substring)
    
    #Calculate the value for each consonant and return the maximum
    max_value = 0
    for substring in consonant_substrings:
        substring_value = sum(ord(char) - ord('a') + 1 for char in substring)
        max_value = max(max_value, substring_value)

    return max_value

print(solve("zodiacs"))
print(solve("strength"))