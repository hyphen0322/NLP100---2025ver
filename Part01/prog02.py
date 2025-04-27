### 文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ。
str = "stressed"
str_ans = ""
for char in reversed(str):
    str_ans += char
print(str_ans)