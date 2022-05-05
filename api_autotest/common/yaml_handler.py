import yaml
class YamlHandler:
    def __init__(self,file):
        self.file = file

    def read_yaml(self,encoding = 'utf-8'):
        '''读取yaml数据'''
        with open(self.file,encoding=encoding) as f:
            return yaml.load(f.read(),Loader=yaml.FullLoader)

    def write_yaml(self,data,encoding = 'utf-8'):
        '''向yaml文件写入数据'''
        with open(self.file,encoding=encoding,mode='w') as f:
            return yaml.dump(data, stream=f, allow_unicode=True)
yaml_data = YamlHandler('../config/config02.yaml').read_yaml()


if __name__=='__main__':
    data = {
        "data":{
            "user":"cjh",
            "pwd":"123456"
        }
    }
    #读取config.yaml配置文件
    read_data =YamlHandler('../config/config.yaml').read_yaml()
    print(read_data)
    write_data = YamlHandler('../config/config01.yaml').write_yaml(data)

