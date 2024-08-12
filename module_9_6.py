def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text) - i):
            str_text = text[j:i+j+1]
            yield str_text

a = all_variants("abc")
for i in a:
    print(i)