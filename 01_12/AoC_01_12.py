
with open('input_01_12.txt', 'r') as f:
    puzzle_input = f.readlines()

# puzzle_input = '''3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3'''.splitlines()

#%%
#parse input
left_list = []
right_list = []
for line in puzzle_input:
    a,b = line.split('   ')
    left_list.append(int(a))
    right_list.append(int(b))

#%%
#Part1
distances = [abs(x-y) for x,y in zip(sorted(left_list),sorted(right_list))]

ans = sum(distances)

print(f'The total distance between my lists is {ans}.')
#%%
#Part2
similarity = []
for ID in left_list:
    similarity.append(ID * right_list.count(ID))

similarity_score = sum(similarity)

print(f'The similarity score of the left and right list is {similarity_score}.')
#%%
