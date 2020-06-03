dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

words = input().split()
fail = False
for word in words:
    if word not in dictionary:
        print(word)
        fail = True

if not fail:
    print('OK')
