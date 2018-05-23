# codign=utf-8

import logging,os

class Log():
    # def __int__(self,clevel = logging.DEBUG):
    #     self.logger = logging.getLogger("name")
    #     self.logger.setLevel(logging.DEBUG)
    #     formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s,%(funcName)s')
    #     #设置文件格式
    #     filehandler = logging.FileHandler('log.txt') #日志文件储存的位置
    #     filehandler.setFormatter(formatter)   #日志输出的格式
    #     filehandler.setLevel(clevel)   #日志输出的等级
    #     self.logger.addHandler(filehandler)

    def go(self):
        self.level=logging.DEBUG
        self.filename = os.path.join(os.getcwd(),'log.txt')
        self.datefmt="%a %b %d %H:%M:%S %Y"
        self.filemode='w'
        self.format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
        logging.basicConfig(level=self.level,filename=self.filename,datefmt=self.datefmt,filemode=self.filemode,format=self.format)
        self.logger = logging.getLogger("simple_example")

    def debug(self,message):
        self.logger.debug(message)

    def info(self,message):
        self.logger.info(message)

    def warning(self,message):
        self.logger.warning(message)

    def error(self,message):
        self.logger.error(message)

    def critical(self,message):
        self.logger.critical(message)
