class BasResult:
    def __init__(self):
        pass

    @classmethod
    def ok(cls,data):
        return cls.createResult(True,"操作成功",data)

    @classmethod
    def not_ok(cls,msg=""):
        if(len(msg)==0):
            return cls.createResult(False,"操作失败",None)
        else:
            return cls.createResult(False, "操作失败："+msg,None)


    def createResult(success,msg,data):
        return {
            "success":success,
            "msg":msg,
            "data":data
        }