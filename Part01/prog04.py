### “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”という文を単語に分解し、1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字、それ以外の単語は先頭の2文字を取り出し、取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ。
def extract(i,word):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        return (word[0],i)
    else:
        return (word[:2],i)

char = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
clean_text = char.replace(".","").split()

ans = [extract(i,word) for i ,word in enumerate(clean_text,1)]
print(dict(ans))