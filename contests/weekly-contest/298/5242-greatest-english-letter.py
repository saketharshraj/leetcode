# https://leetcode.com/contest/weekly-contest-298/problems/greatest-english-letter-in-upper-and-lower-case/

# Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.

# An English letter b is greater than another letter a if b appears after a in the English alphabet.

# Input: s = "lEeTcOdE"
# Output: "E"
# Explanation:
# The letter 'E' is the only letter to appear in both lower and upper case.

# Input: s = "arRAzFif"
# Output: "R"
# Explanation:
# The letter 'R' is the greatest letter to appear in both lower and upper case.
# Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.


def greatestLetter(s: str) -> str:
    d = {}
    greatest = ''

    for i in s:
        if i.lower() in d:
            if i.isupper() and d[i.lower()] == -1:
                 d[i.lower()] += 1
            elif i.islower() and d[i.lower()] == 1:
                 d[i.lower()] += -1

            if i.lower() > greatest.lower() and d[i.lower()] == 0:
                greatest = i.upper()
        else:
            if i.isupper():
                d[i.lower()] = 1
            else:
                d[i.lower()] = -1
    return greatest

print(greatestLetter('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAabBaaAAAAAAAAA'))
