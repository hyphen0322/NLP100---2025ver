### 2つの文字列「パトカー」と「タクシー」の文字を先頭から交互に連結し、文字列「パタトクカシーー」を得よ。＋文字列そろってない場合も実装！
str1 = "パトカーだよ"
str2 = "タクシー"
str_mix = ""

mini = min(len(str1),len(str2))
# 文字数が少ないほうに合わせて交互連結
for i in range(mini):
    str_mix += str1[i] + str2[i]

# 片方がまだ残ってたら、残りを追加
str_mix += str1[mini:] + str2[mini:]

print(str_mix)