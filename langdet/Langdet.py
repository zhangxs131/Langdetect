import chardet
import joblib
import os
import platform

import warnings
warnings.filterwarnings('ignore')

class Langdet():
    def __init__(self) -> None:
        super().__init__()
        #查看使用环境，linux和window不同的路径选择
        sys=platform.system()

        if sys=='Linux':
            #获取安装后该文件的路径,如果为window系统使用，则改为\\即可
            path = (__file__).split("/")[0:-1]
            filepath = path[0]
            for i in path[1:]:
                filepath = filepath + "/" + i
        else:
            path = (__file__).split("\\")[0:-1]
            filepath = path[0]
            for i in path[1:]:
                filepath = filepath + "\\" + i

        file_count="count_vec_model.m"
        file_classifier="classifier_model.m"
        self.count_vec = joblib.load(os.path.join(filepath,file_count))
        self.classifer = joblib.load(os.path.join(filepath,file_classifier))
        self.to_index={
            'chinese':1,
            'english':2,
            'japanese':3,
            'french':4,
            'korean':5,
            'Russian':6,
            'Spanish':7,
            'German':8,
            'vietnam':9,
            'Tibetan':10,
            'uyghur':11,
            'mongolian':12,
            'Kazakh':13
        }
        self.to_ctag={
            1:'汉语',
            2:'英语',
            3:'日语',
            4:'法语',
            5:'韩语',
            6:'俄语',
            7:'西班牙语',
            8:'德语',
            9:'越南语',
            10:'藏语',
            11:'维吾尔语',
            12:'蒙古语',
            13:'哈萨克语'
        }
        self.to_etag=dict([val,key] for key,val in self.to_index.items())

    def decode_file(self,file_path):
        context = open(file_path, 'rb').read()
        if file_path.split('.')[-1] != "txt":
            print("Error:the type of data file is not the txt file")
        # use the chardet module to predict the encoding type of file
        encoding_type = chardet.detect(context)['encoding']
        # print(encoding_type)
        decode = context.decode(encoding=encoding_type)
        return decode

    def detect_text(self,text):
        result = self.classifer.predict(self.count_vec.transform([text]))[0]
        return self.to_index[result]


    def detect_file(self,file_path):
        file = self.decode_file(file_path)
        return self.detect_text(file)

    def get_encoding_type(self,file_path):
        context = open(file_path, 'rb').read()
        if file_path.split('.')[-1] != "txt":
            print("Error:the type of data file is not the txt file")
        # use the chardet module to predict the encoding type of file
        encoding_type = chardet.detect(context)['encoding']
        # print(encoding_type)
        return encoding_type

    def id_to_str(self,index):
        return self.to_etag[index]

    def str_to_id(self,string):
        return self.to_index(string)

    def id_to_chinese(self,index):
        return self.to_ctag[index]

    def about_me(self):
        return str('目前可识别的语言有:\n'
                          '1.汉语 Chinese     2.英语 English    3.日语 Japanese\n'
                          '4.法语 Frech       5.韩语 Korean     6.俄语 Russian \n'
                          '7.西班牙语 Spanish  8.德语 German     9.越南语 vietnam \n\n'
                          '少数民族语言有:\n'
                          '10.藏语 Tibetan    11.维吾尔语 uyghur 12.蒙古语 mongolian\n'
                           '13.哈萨克语 Kazakh\n\n'
                  )

