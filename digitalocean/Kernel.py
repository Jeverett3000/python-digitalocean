# -*- coding: utf-8 -*-
from .baseapi import BaseAPI


class Kernel(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.name = ""
        self.id = ""
        self.version = ""
        super(Kernel, self).__init__(*args, **kwargs)

    def __str__(self):
        return f"<Kernel: {self.name} {self.version}>"
