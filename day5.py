import re
from read_input import read_file

lines = read_file('input5.txt')

# Part 1
def process_pass(ps):
    
    rowl, rowu = 0, 127
    coll, colu = 0, 7
    
    for i in range(len(ps)):
        if i < 7:
            mid = (rowl + rowu) // 2
            if ps[i] == 'F':
                rowu = mid
            else:
                rowl = mid + 1
            # print('row', rowl, rowu)
        else:
            mid = (coll + colu) // 2
            if ps[i] == 'L':
                colu = mid
            else:
                coll = mid + 1
            # print('col', coll, colu)
    assert rowl == rowu, f'rows not equal {rowl} {rowu}, passport {ps}'
    assert coll == colu, f'cols not equal {coll} {colu}, passport {ps}'
    
    return rowl*8 + coll
# 4 5
# process_pass('BBFFFFBRLL')

def get_passids(passes):
    
    passids = []
    for ps in passes:
        ps = ps[:10]
        passids.append(process_pass(ps))
    
    return passids

print(max(get_passids(lines)))

# Part 2
all_passids = sorted(get_passids(lines))
mn = min(all_passids)
mx = max(all_passids)

for i in range(len(all_passids)):
    if i > 0 and all_passids[i] - all_passids[i-1] > 1:
        print(all_passids[i]-1)