import nltk
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords

def detect_language(text):
    words = wordpunct_tokenize(text.lower())
    lang_ratio = {}
    tokens = set(words)
    words_set = set(stopwords.words('english'))
    for lang in stopwords.fileids():
        stopwords_set = set(stopwords.words(lang))
        common_elements = tokens.intersection(stopwords_set)
        lang_ratio[lang] = len(common_elements)

    arCuObLimbi = []
    for cheie in lang_ratio:
        if lang_ratio[cheie] > 0 :
            arCuObLimbi.append({cheie: lang_ratio[cheie]})
    # print(arCuObLimbi, '---------------')
    arSortat  = sorted(arCuObLimbi, key=lambda x: list(x.values())[0], reverse=True)
    return arSortat


text = "Cum este pe afara azi ?"
# print(detect_language(text))

