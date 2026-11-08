import os

from expec import(
    FileNotFound, TooBig, BinaryFile, InvalidType
)

def readContent(path:str, ignoreWarns = False, treshHold:int = 209715200):
    if not path:
        raise ValueError("PATH CANT BE EMPTY")
    if not os.path.exists(path):
        raise FileNotFound("PATH DONT EXSITS")
    if os.path.getsize(path) > treshHold:
        if not ignoreWarns:
            raise TooBig("FILE TOO BIG")
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = file.read() 
    except UnicodeDecodeError:
        if not ignoreWarns:
            raise BinaryFile("FILE IS BINARY")
            
        with open(path, "rb") as file:
            data = file.read()
    return data

def size(path:str, type:str = "MB"):
    if not path:
        raise ValueError("PATH CANT BE EMPTY")
    if not os.path.exists(path):
        raise FileNotFound("PATH DONT EXSITS")
    types = ["B", "KB", "MB", "GB"]
    siz = os.path.getsize(path)
    if type in types:
        index = 1024 ** types.index(type)
        if siz % index == 0:
            return siz // index
        else:
            return siz / index
    else:
        raise InvalidType(f"INVALID TYPE MUST BE ONE OF {types}")