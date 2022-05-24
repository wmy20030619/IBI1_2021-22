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
file1 = open('cut_genes.fa','w')
marker = 0
for i in seq:
    marker += 1
    if i.count('GAATTC') != 0:
        file1.write('>' + name[marker] + '      ' + str(len(i))+'\n')
        file1.write(seq[marker]+'\n')
file1.close()
