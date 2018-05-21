import sys, tempfile, operator, traceback, StringIO
import StringIO

class functions:

    # def add(self, code):
    #     str(num1)
    #     try:
    #         c = 2 + num1
    #         return c
    #     except:
    #         exc_type, exc_value, exc_traceback = sys.exc_info()
    #         return repr(traceback.format_exception(exc_type, exc_value,
    #                                                exc_traceback))

    def fun(self, code):
        mycor = compile(code,'','exec')
        exec(mycor)
        result =eval('code()')
        return result


