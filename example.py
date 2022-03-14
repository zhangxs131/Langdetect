from langdet.Langdet import Langdet
dect=Langdet()


#查看目前支持的语言
readme=dect.about_me()
print(readme)

english_text='this is a boy who is looking for his mother.'
japanese_text='海賊の王私はになる'

#检测文本
lang_idx=dect.detect_text(english_text)

print('the index of the language is ',lang_idx)

lang=dect.id_to_str(lang_idx)

print('the language is ',lang)

lang_in_chinese=dect.id_to_chinese(lang_idx)

print(english_text,'所用语言为 :',lang_in_chinese)

#日语
print(japanese_text,'is ',dect.id_to_str(dect.detect_text(japanese_text)))


#文件检测
lang_from_file=dect.detect_file('korean_test.txt')
print('the file is ',dect.id_to_str(lang_from_file))


'''
目前可识别的语言有:
1.汉语 Chinese     2.英语 English    3.日语 Japanese
4.法语 Frech       5.韩语 Korean     6.俄语 Russian 
7.西班牙语 Spanish  8.德语 German     9.越南语 vietnam 

少数民族语言有:
10.藏语 Tibetan    11.维吾尔语 uyghur 12.蒙古语 mongolian
13.哈萨克语 Kazakh


the index of the language is  2
the language is  english
this is a boy who is looking for his mother. 所用语言为 : 英语
海賊の王私はになる is  japanese
the file is  korean
'''