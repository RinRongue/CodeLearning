import operator as 原神
import itertools
a,b,c,d=map(int,input('a,b,c,d').split(','))
ls=[a,b,c,d]
result=[]
formula=[]
def main(a,b,c,d):
    global result,formula #不global也行吧
    sy=[原神.add,原神.sub,原神.mul,原神.truediv]
    sy1=['+','-',"*",'/']
    for ii in range(4):
        for jj in range(4):
            for kk in range(4):
                result.append(sy[kk](sy[jj](sy[ii](a,b),c),d))
                formula.append('(('+str(a)+sy1[ii]+str(b)+')'+sy1[jj]+str(c)+')'+sy1[kk]+str(d))
                try:
                    result.append(sy[kk](sy[jj](sy[ii](b,c),a),d))
                    formula.append(f'(({b}{sy1[ii]}{c}){sy1[jj]}{a}){sy1[kk]}{d}')
                except:
                    pass
                try:
                    result.append(sy[kk](sy[ii](a,b),sy[jj](c,d)))
                    formula.append(f'({a}{sy1[ii]}{b}){sy1[kk]}({c}{sy1[jj]}{d})')
                except:
                    pass
                try:
                    result.append(sy[kk](sy[jj](sy[ii](b,c),d),a))
                    formula.append(f'(({b}{sy1[ii]}{c}){sy1[jj]}{d}){sy1[kk]}{a}')
                except:
                    pass
                try:
                    result.append(sy[kk](sy[jj](sy[ii](c,d),b),a))
                    formula.append(f'(({c}{sy1[ii]}{d}){sy1[jj]}{b}){sy1[kk]}{a}')
                except:
                    pass
    return
for perm in itertools.permutations(ls):
    i, j, k, l = perm
    main(i, j, k, l)
# for i in ls:
#     ls.remove(i)
#     for j in ls:
#         ls.remove(j)
#         for k in ls:
#             ls.remove(k)
#             l=ls[0]
#             main(i,j,k,l)
max_result=max(result)
max_formula=formula[result.index(max_result)]
print(f'{max_formula}={max_result}')
try:
    formula_24=formula[result.index(24)]
except:
    print('无24点解')
else:
    print(f'{formula_24}=24')


