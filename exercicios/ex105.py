def notas(*n, sit=False):
    r = dict()
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["media"] = sum(n)/len(n)
    if sit:
        if r["media"] >= 7:
            r["situação"] = "boa"
        elif r["media"] >= 5:
            r["situação"] = "Razoavel"
        else:
            r["situação"] = "Ruim!"
    return r 

resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
