def all_unique(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return False
        seen.add(ch)
    return True


print(all_unique("kopa"))  
print(all_unique("satamasho"))    
