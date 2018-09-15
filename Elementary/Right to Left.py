def left_join(phrases):
    phrases = list(phrases)
    new_phrases = []

    for phrase in phrases:
         new_phrases.append(phrase.replace('right','left'))

    text = ','.join(new_phrases)

    return text

print(left_join(("left", "right", "left", "stop")))