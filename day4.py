import re
from read_input import read_file

lines = read_file('input4.txt')

lines = ''.join(lines).replace('\n', ' ')

# Process passports
lines = lines.split('  ')
passports = []
for line in lines:
    p = {}
    items = line.split(' ')
    for item in items:
        key, val = item.split(':')
        p[key] = val
    passports.append(p)
        
must_haves = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# Part 1
def count_valid(passports, must_haves):
    
    total = 0
    for passport in passports:
        valid = True
        
        for key in must_haves:
            if key not in passport:
                valid = False
                break
        total += valid*1
    
    return total

print(count_valid(passports, must_haves))
          
# Part 2
def count_valid2(passports, must_haves):
    
    total = 0
    for passport in passports:
        valid = True
        
        for key in must_haves:
            if key not in passport:
                valid = False
                break
        
        if (
            valid and \
            (1920 <= int(passport['byr']) <= 2002) and \
            (2010 <= int(passport['iyr']) <= 2020) and \
            (2020 <= int(passport['eyr']) <= 2030) and \
            (bool(re.match('[0-9]+(cm|in)', passport['hgt']))) and (('cm' in passport['hgt'] and 150 <= int(passport['hgt'][:-2]) <= 193) or ('in' in passport['hgt'] and 59 <= int(passport['hgt'][:-2]) <= 76)) and \
            (bool(re.match('#[a-f0-9]{6}', passport['hcl']))) and \
            (passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) and \
            (bool(re.match('[0-9]{9}', passport['pid'])))
        ):
            valid = True
        else:
            valid = False
            
        total += valid*1
    
    return total

print(count_valid2(passports, must_haves)-1)
         