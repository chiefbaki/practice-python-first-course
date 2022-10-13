import datetime
# import sys
#
#
# class Tee(object):
#     def __init__(self, name, mode):
#         self.file = open(name, mode)
#         self.stdout = sys.stdout
#
#     def __del__(self):
#         self.close()
#
#     def write(self, data):
#         self.stdout.write(data)
#         self.file.write(data)
#
#     def flush(self):
#         self.stdout.flush()
#         self.file.flush()
#
#    # def close(self):
#     #    if sys.stdout is self:
#   #          sys.stdout = self.stdout
#  #       self.file.close()
#
#
# #sys.stdout = Tee('log2.log', 'a')

def Log(key, comment):
    File = open("Log.txt", "a")
    if key == "CRE":
        File.write("создание экземпляра класса")
    if key == "INF":
        File.write("изменение")
    if key == "ERR":
        File.write("сработало исключение")
    File.write(f" --- {datetime.datetime.now()} --- {comment}\n")
    File.close()
