from LAC import LAC
from collections import Counter

lac = LAC(mode='lac')

def count_hanzi(text: str) -> list:
    text = lac.run(text.replace("\n", " ").strip())
    text = clean_words(text)
    hanzi_counts = Counter(text)
    return hanzi_counts.most_common()

def clean_words(texts: list) -> str:
    words = texts[0]
    character_type = texts[1]
    cleaned_words = []

    for index in range(len(words)):
        if character_type[index] != "w":
            cleaned_words.append(words[index])

    return cleaned_words

if __name__ == "__main__":
    print(count_hanzi("""
        LAC全称Lexical Analysis of Chinese，是百度自然语言处理部研发的一款联合的词法分析工具，实现中文分词、词性标注、专名识别等功能。该工具具有以下特点与优势：
        效果好：通过深度学习模型联合学习分词、词性标注、专名识别任务，词语重要性，整体效果F1值超过0.91，词性标注F1值超过0.94，专名识别F1值超过0.85，效果业内领先。
        效率高：精简模型参数，结合Paddle预测库的性能优化，CPU单线程性能达800QPS，效率业内领先。
        可定制：实现简单可控的干预机制，精准匹配用户词典对模型进行干预。词典支持长片段形式，使得干预更为精准。
        调用便捷：支持一键安装，同时提供了Python、Java和C++调用接口与调用示例，实现快速调用和集成。
        支持移动端: 定制超轻量级模型，体积仅为2M，主流千元手机单线程性能达200QPS，满足大多数移动端应用的需求，同等体积量级效果业内领先。
        """)
    )
