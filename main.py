from .lib.file_one import ClassOne
from .lib.file_three import ClassTwo


def main():
    cls = ClassOne()
    cls.functionOne()
    cls.functionTwo()
    cls.functionThree()

    clsTwo = ClassTwo()
    cls.functionOne()
    cls.functionTwo()
    cls.functionThree()
