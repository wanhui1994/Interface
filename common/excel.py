# coding=utf-8
import xlwt,xlrd

class Excelread():
    def __init__(self):
        pass

    def open(self,path,name):
        try:
              self.wb = xlrd.open_workbook(path)
              self.sh = self.wb.sheet_by_name(name)
        except Exception:
            raise NameError

    def lines(self,number):
        value = self.sh.row_values(int(number))
        return value

    def columns(self,number):
        value = self.sh.col_values(int(number))
        return value

    def allshee(self):
        value = self.wb.sheet_names()
        return value


class Excelwrite():

    def new_excel(self,filname,name):
        self.filname=filname
        try:
            self.wr=xlwt.Workbook(filname)  #The name of the file created
            self.sh=self.wr.add_sheet(name)  #The created table name
        except Exception:
            print('文件创建失败，请检查创建的文件名是否存在！')

    def write(self,lines,col,name):
        value = self.sh.write(lines,col,name)
        return value

    def save(self,path):
        path=path+self.filname+'.xls'
        self.wr.save(path)
