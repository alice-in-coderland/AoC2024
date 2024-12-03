import re

corrupted_memory = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

with open('input_03_12.txt', 'r') as f:
    corrupted_memory = f.readlines()

# %%
corrupted_memory = ''.join(corrupted_memory)
corrupted_memory = 'do' + corrupted_memory


# %%
# Part 1

def find_instructions(mem):
    instructions = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)',
                              mem)

    addup = 0
    for instruction in instructions:
        a, b = [int(x) for x in re.findall(r'[0-9]{1,3}', instruction)]
        addup += a * b

    return addup


print(f'If you add up all of the results of the multiplications, you get {find_instructions(corrupted_memory)}.')
# %%
# Part 2
# corrupted_memory = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''
# corrupted_memory = 'do'+corrupted_memory
# %%
chunks = corrupted_memory.split('don\'t')
# %%
addup_p2 = 0
for chunk in chunks:
    ind_do = chunk.find('do')
    if ind_do >= 0:
        operate_chunk = chunk[ind_do::]
        addup_p2 += find_instructions(operate_chunk)

print(f'If you add up all of the results of just the enabled multiplications, you get {addup_p2}.')

#%%
