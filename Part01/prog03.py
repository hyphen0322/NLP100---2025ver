### “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し、各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ。
str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str_clean = str.replace(",","").replace(".","").split()
# print(str_clean)
str_count = [len(word) for word in str_clean]
print(str_count)