d = {"1.html": {"2.html"}, "2.html": {"1.html", "3.html"}, "3.html": {"2.html", "4.html"}, "4.html": {"2.html"}}
'''d.setdefault("2.html", set()).add("4.html")
print(d["2.html"])
print(len(d))
for i in d:
    print(i)



print("2.html" in d["1.html"])
import random
print(random.choice(list(d.keys())))

for i in d.keys():
    print(i)

b = dict.fromkeys(d, 0)
print(b)
b["1.html"] += 1
b["1.html"] += 1

print(b)

'''

d2 = dict.fromkeys(d, [])
print("d2 bl", d2)
for page in d2:
    print("page ch")
    for key in d:
        if page in d[key]:
            d2[page] = d2[page] + [key]


