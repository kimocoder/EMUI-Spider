#!/usr/bin/python
import esp
import confrw
import os

 
def get_text_file(filename):
        with open(filename, "r") as f:
                content = f.read()
        return content


filename = r'conf.ini'
if os.path.exists(filename):
        b=get_text_file(filename)
        if ("bg" not in b or "g" not in b or "f" not in b or "stv" not in b
            or "env" not in b):
                confrw.confcr()
else:
        confrw.confcr()

esp.main()

