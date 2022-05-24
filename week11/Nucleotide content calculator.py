def f(seq0):
# seq0 = input('Please enter your desired DNA sequence')
    seq = seq0.upper()
# check whether the sequence only contains ATCG
    base = ['A','C','G','T']
    check=True
    detector = ""
    for i in range(len(seq)):
        detector = seq[i]
        if detector not in base:
            check = False
    while check == False:
        seq0 = input('Please enter the right sequence')
        seq = seq0.upper()
        check = True
        for i in range(len(seq)):
            detector = seq[i]
            if detector not in base:
                check = False
# calculate each percentage in base
    for i in base:
        count = 0
        for j in range(len(seq)):
            if seq[j] == i:
                count += 1
        percentage = '{:.2%}'.format(count/len(seq))
        print('The ' + i + 'content is:',percentage)
    return
# input the sequence
f(input('Please enter your desired DNA sequence'))





