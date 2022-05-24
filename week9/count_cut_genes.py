import re
file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
a = file.read().rstrip()
name = re.findall(r'>(.+?)_',a)
seq0 = re.findall(r']([ATCG\n]+)',a)
file.close()
seq = []
for x in seq0:
    x = x.replace('\n','')
    seq.append(x)

file1 = open(input('please enter the file name you want:') + '.fa','w')
marker = 0
for i in seq:
    marker += 1
    number = i.count('GAATTC')
    if number != 0:
        file1.write('>' + name[marker] + '   ' + str(number) + '\n')
        file1.write(seq[marker])
file1.close()
