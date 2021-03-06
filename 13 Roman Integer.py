s = "III"
runningTotal = 0

numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

for c in reversed(s):
    try:
        runningTotal += numerals[c]
    except Exception as e:
        # print(e)
        print(f"{e} not a Roman Numeral")

print(runningTotal)
