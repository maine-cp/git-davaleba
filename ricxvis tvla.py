def letter_count(s):

    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


print(letter_count("flugengengenxoleni"))