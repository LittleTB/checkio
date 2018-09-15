def correct_sentence(text: str) -> str:
    lst = list(text)

    if not lst[0].isupper():
        lst[0] = lst[0].upper()

    if lst[-1] != '.':
         lst.append('.')

    return ''.join(lst)

print(correct_sentence("greetings, friends"))