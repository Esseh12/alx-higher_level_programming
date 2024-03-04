#!/usr/bin/python3

class Man:
    eye = True
    nose = False

    def __init__(self, eye, nose):
        self.eye = eye
        self.nose = nose


        def serialize (self):
            return self.__dict__

        m = man(True, False)
        print(m.serialize())
