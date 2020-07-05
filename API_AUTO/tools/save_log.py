import logging


class SaveLog():
    def save_log(self, msg, level):
        # 定义一个日志收集器
        my_logger = logging.getLogger('python11')

        # 设置收集的级别
        my_logger.setLevel('DEBUG')

        # 创建输出渠道
        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')

        # 两者对接
        my_logger.addHandler(ch)

        # 搜集日志
        if level == "DEBUG":
            my_logger.debug(msg)
        elif level == "INFO":
            my_logger.debug(msg)
        elif level == "WARNING":
            my_logger.debug(msg)
        elif level == "ERROR":
            my_logger.debug(msg)
        elif level == "CRITICAL":
            my_logger.debug(msg)

        # 关闭日志收集器
        my_logger.removeHandler(ch)

    def Debug(self, msg):
        self.save_log(msg, 'DEBUG')

    def Info(self, msg):
        self.save_log(msg, 'INFO')

    def Warning(self, msg):
        self.save_log(msg, 'WARNING')

    def Error(self, msg):
        self.save_log(msg, 'ERROR')

    def Critical(self, msg):
        self.save_log(msg, 'CRITICAL')


if __name__ == '__main__':
    SaveLog().save_log("1", "ERROR")
    SaveLog().save_log("2", "ERROR")
    SaveLog().save_log("3", "ERROR")
