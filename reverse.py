def reverse_string(s):

    reversed_s = ""
    for ch in s:
        reversed_s = ch + reversed_s
    return reversed_s

print(reverse_string("daviti maswi kargi kacia"))
