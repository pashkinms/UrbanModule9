
def all_variants(text: str):
    for i in range(1, len(text)+1):
        for j in range(len(text)+1):
            if (j + i) <= len(text):
                yield text[j: j+i]


a = all_variants("abc")
for i in a:
    print(i)
