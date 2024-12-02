unusual_data = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''.splitlines()

with open('input_02_12.txt', 'r') as f:
    unusual_data = f.readlines()

#%%
def check_safety(report):
    # print(report)
    if sorted(report)==report or sorted(report, reverse=True)==report:
        check = [abs(report[i]-report[i+1]) for i in range(len(report)-1)]
        if min(check)>=1 and max(check)<=3:
            return True
        else:
            return False
    else:
        return False

#%%
#Part 1
safe_reports1 = 0
for rep in unusual_data:
    rep = [int(x) for x in rep.split(' ')]
    if check_safety(rep): safe_reports1+=1

print(f'How many reports are safe?: {safe_reports1}')
#%%
#Part2
safe_reports2 = 0
for rep in unusual_data:
    rep = [int(x) for x in rep.split(' ')]
    # print(rep)
    if check_safety(rep): safe_reports2+=1
    else:
        for i, level in enumerate(rep):
            newrep = [rep[x] for x in range(len(rep)) if x!=i]
            if check_safety(newrep):
                safe_reports2+=1
                break

print(f'How many reports are safe?: {safe_reports2}')
#%%

#%%
