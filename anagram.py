a=list(input("Str=").split())
g_anagrams={}
for i in a:
    s=str(sorted(i))
    if s in g_anagrams:
        g_anagrams[s].append(i)
    else:
        g_anagrams[s]=[i]
print(list(g_anagrams.values()))
    
