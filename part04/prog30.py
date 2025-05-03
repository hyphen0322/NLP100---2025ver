import MeCab

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

def extract_verbs(doc):
    mecab = MeCab.Tagger()
    node = mecab.parseToNode(doc)
    verbs = []
    while node:
        if node.feature.startswith('動詞'):
            verbs.append(node.surface)
        node = node.next
    return verbs

def main():
    verbs = extract_verbs(text)
    print(verbs)

if __name__ == "__main__":
    main()
