bb = []
dd = { }
for a in aa.values():
    if type(a) == int:
        bb.append(a)
        bb.sort()
for b in aa:
    if aa[b] in bb:

        dd[b]=aa[b]
with open("./p2.txt","w") as f:
    f.write(str(dd))
