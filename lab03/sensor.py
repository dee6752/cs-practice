porog=float(input())
n=int(input())
count_error=0
perebor = 0
max_s=-999999
sum=0
for i in range(n):
    s=input()
    if s=='error':
        count_error+=1
    else:
        if float(s)>max_s:
            max_s=float(s)
        if float(s)>porog:
            perebor+=1
        if True:
            sum+=float(s)
print(n)
print(count_error)
print(perebor)
print(f'{max_s:.1f}')
print(f'{(sum/(n-count_error)):.1f}')
