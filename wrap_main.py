import wikipedia

wikipedia.set_lang("jp")

words = wikipedia.search("メンヘラ")
print(words)

res = wikipedia.page(words[0])

print(res.summary)
