#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Good import __all__ as all_submodules
import sys
import Good

def main(argv):
    if len(argv) > 1 and argv[1] in ["-l", "--list"]:
        print("Available submodules: ")
        for i, submodule in enumerate(all_submodules, 1):
            print("{}. good.{} / bad.{}".format(i, submodule, submodule))
            ==> Appeler tous les mains

if __name__ == "__main__":
    
    main(sys.argv)