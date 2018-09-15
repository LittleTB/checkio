"""你将得到一些可能含有有意义的词汇的文本。你需要统计在给出文本中包含的词汇数量。
一个词汇可能是一个整体或者另一个词汇的一部分。检查文本时不区分大小写，你需要检查的词汇将被以小写形式给出且不会重复。
如果一个词在文本中出现多次，你只需要计数一次。
举个例子，文本："How aresjfhdskfhskd you?"，词汇：("how", "are", "you", "hello")。输出结果是3。"""


def count_words(text,words):
    count=0
    for word in words:
        if text.lower().count(word):
            count += 1
    print(count)

count_words("How aresjfhdskfhskd you?", ["how", "are", "you", "hello"])
count_words("Bananas, give me bananas!!!", ["banana", "bananas"])
count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
            ["sum", "hamlet", "infinity", "anything"])
