import configparser
from tools.project_path import mail_config_path


class ReadConfig:
    @staticmethod
    def get_config(filepath, section, option):
        cf = configparser.ConfigParser()
        cf.read(filepath, encoding='utf-8')
        return cf[section][option]


rc = ReadConfig()
if __name__ == '__main__':
    # print(ReadConfig.get_config(case_config_path, 'Mode', 'mode'))
    print(rc.get_config(mail_config_path, 'Mail', 'mail'))
    print(type(rc.get_config(mail_config_path, 'Mail', 'mail')))
