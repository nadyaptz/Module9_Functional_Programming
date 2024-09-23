def all_variants(text):
    for len_seq in range(len(text)):
        for l in range(len(text) - len_seq):
            yield text[l:l+len_seq+1]


a = all_variants("abcd")
for i in a:
    print(i)

