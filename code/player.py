#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.class1 import Class1
from code.class8 import Class8
from code.entity1 import Entity1


class Class1:
    pass


class Player(Class8, Class1, Entity1):
    def __init__(self):
        self.Attribute1 = None

    def move(self, ):
        pass
