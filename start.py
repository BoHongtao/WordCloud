# -*- coding: utf-8 -*-
from os import path
import os
import jieba
from wordcloud import WordCloud
import matplotlib as mpl
import numpy as np
from PIL import Image
mpl.use("TkAgg")
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# 分词
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

text = open('./log/clean.txt',encoding='utf-8').read()
cut_text = ' '.join(jieba.cut(text))
j_text = jieba.cut(text)
cut1_text = ''.join(jieba.cut(text))

font = './font/SimHei.ttf'
# Heart_coloring = np.array(Image.open(path.join(d, "heart.png")))
stopwords = set(STOPWORDS)
stopwords.add("said")

# 用分词做词云
wc = WordCloud(background_color="white", collocations=False, font_path=font, width=3000, height=2500, margin=2,
                                    max_font_size=220, min_font_size=20).generate(cut_text)
# image_colors = ImageColorGenerator(Heart_coloring)
# plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
#plt.imshow(wc)
# plt.axis("off")
# plt.show()

# 把词云保存下来
wc.to_file('show_Chinese.png') 