### 文字列「パタトクカシーー」の2, 4, 6, 8文字目を取り出し、それらを連結した文字列を得よ。
str = "パタトクカシーー"
str_ans = ""
## // は整数除算(rangeがintのみなので)
sum = len(str) // 2
for i in range(sum):
    j = i * 2 + 1
    str_ans += str[j]

print(str_ans)