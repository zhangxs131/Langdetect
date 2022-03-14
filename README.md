

# README

目前支持识别 13 种语言： Chinese  English  Japanese French Korean Russian Spanish German vietnam Tibetan uyghur  mongolian Kazakh

## 1. Install

下载whl到本地后，pip进行安装

```
pip install langdet-1.0-py3-none-any.whl
```

测试是否安装成功

```python
from langdet.Langdet import Langdet
```

或者使用git下载

```
git clone https://github.com/zhangxs131/Langdetect.git
pip install chardet
cd Langdet
python example.py
```

导入类，成功安装

## 2. How to use

创建类

```
dect=Langdet()
```

查看使用说明和语种索引说明

```python
dect.about_me()
```

检测文件所用主要语种，返回索引 int，这里目前仅支持.txt文件。

```
dect.detect_file(file_path)
```

直接检测字符串文件内容，返回索引 int

```
dect.detect_text(str)
```

将int索引解码为字符串或中文显示

```
dect.id_to_str(index)
dect.id_to_chinese(index)
```

检测文本编码类型

```
dect.get_encoding_type(file_path)
```

将其他编码文件解码，转为Unicode

```
dect.decode(file_path)
```



## 3.About

```
目前可识别的语言有:
1.汉语 Chinese     2.英语 English    3.日语 Japanese
4.法语 Frech       5.韩语 Korean     6.俄语 Russian 
7.西班牙语 Spanish  8.德语 German     9.越南语 vietnam 

少数民族语言有:
10.藏语 Tibetan    11.维吾尔语 uyghur 12.蒙古语 mongolian
13.哈萨克语 Kazakh
```

Author ：张晓松

Email    ：zhangxs131@163.com

From    ：Beijing Institute University .the Lab of NLPIR

website：www.nlpir.org

Mentor：张华平博士 
