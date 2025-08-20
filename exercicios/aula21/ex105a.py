def notas(*n, sit = False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)

    if sit:
        if r['media'] >=7:
            situacao = 'boa'
        elif 5 <= r['media'] < 7:
            situacao = 'razoavel'
        elif r['media'] < 5:
            situacao = 'ruim'
        r['situacao'] = situacao
    return r


resp = notas(5,2,9,8, sit=True)
print(resp)