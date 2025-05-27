import itertools
import operator as 原神

a, b, c, d = map(int, input('a,b,c,d：').split(','))
ls = [a, b, c, d]
result = []
formula = []

def main(a, b, c, d):
    global result, formula
    sy = [原神.add, 原神.sub, 原神.mul, 原神.truediv]
    sy1 = ['+', '-', '*', '/']
    for ii in range(4):
        for jj in range(4):
            for kk in range(4):
                res = sy[kk](sy[jj](sy[ii](a, b), c), d)
                result.append(res)
                formula.append(f'(({a}{sy1[ii]}{b}){sy1[jj]}{c}){sy1[kk]}{d}')
                try:
                    res = sy[kk](sy[jj](sy[ii](b, c), a), d)
                    result.append(res)
                    formula.append(f'(({b}{sy1[ii]}{c}){sy1[jj]}{a}){sy1[kk]}{d}')
                except:
                    pass
                try:
                    res = sy[kk](sy[ii](a, b), sy[jj](c, d))
                    result.append(res)
                    formula.append(f'({a}{sy1[ii]}{b}){sy1[kk]}({c}{sy1[jj]}{d})')
                except:
                    pass
                try:
                    res = sy[kk](sy[jj](sy[ii](b, c), d), a)
                    result.append(res)
                    formula.append(f'(({b}{sy1[ii]}{c}){sy1[jj]}{d}){sy1[kk]}{a}')
                except:
                    pass
                try:
                    res = sy[kk](sy[jj](sy[ii](c, d), b), a)
                    result.append(res)
                    formula.append(f'(({c}{sy1[ii]}{d}){sy1[jj]}{b}){sy1[kk]}{a}')
                except:
                    pass

for perm in itertools.permutations(ls):
    i, j, k, l = perm
    main(i, j, k, l)

max_result = max(result)
max_formula = formula[result.index(max_result)]
print(f'{max_formula}={max_result}')

for i in range(len(result)):
    try:
        result[i]=round(result[i],4)
    except:
        pass
    else:
        result[i]=int(result[i])

try:
    idx = result.index(24)
    formula_24 = formula[idx]
except:
    print('无24点解')
else:
    print(f'{formula_24}=24')
