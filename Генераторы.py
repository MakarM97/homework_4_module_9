def all_variants(string):
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            yield string[i:j]


for variant in all_variants("abc"):
    print(variant)