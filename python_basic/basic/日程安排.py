class calendar():
    data={'给父母买礼物':'9:00', '学习':'10:00', '和朋友聚会':'18:30'}
    @classmethod
    def show(cls):
        for i in cls.data:
            print('{}:{}'.format(i,cls.data[i]))
    @classmethod
    def add(cls):
        A=input('请输入要增加的日程\n')
        B=input('请输入时间\n')
        cls.data[A]=B
    @classmethod
    def delete(cls):
        A=input('请输入要删除的日程\n')
        del cls.data[A]
def main():
        A=input('是否修改日程？ 是  否\n')
        if A=='是':
            while True:
                B=input('增加还是删除？  增加  删除\n')
                if B=='增加':
                    calendar.add()               
                elif B=='删除':
                    calendar.delete()
                C=input('是否继续删除或增加？  结束  继续\n')
                if C=='结束':
                    calendar.show()
                    break
                else:
                    pass
        else:
            calendar.show()
calendar.show()
main()

            
            
            


