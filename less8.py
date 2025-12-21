"""
import logging
logging.basicConfig(level=logging.DEBUG,filename="logs.log",filemode="w",format="We have next login messange: %(asctime)s - %(name)s - %(levelname)s - %(message)s")
try:
    print(10/0)
except Exception:
    logging.exception("No.")
logging.debug("Debug")
logging.info("Program works with loops")
logging.warning("Warning")
logging.error("Error")
logging.critical("Critical")
"""
#assert 2+2 == 5, "Dawg...........2+2=4......................"
"""
#>>> 2+2
4
"""
"""
if __name__ == '__main__':
    import doctest
    doctest.testmod()
"""
def adder(*args,**kwargs):
    result = 0
    for arg in args:
        result += arg
    for kwarg in kwargs:
        result += kwarg
    return result