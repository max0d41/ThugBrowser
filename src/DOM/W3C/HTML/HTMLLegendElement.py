#!/usr/bin/env python
from __future__ import with_statement

from HTMLElement import HTMLElement
from attr_property import attr_property

class HTMLLegendElement(HTMLElement):
    @property
    def form(self):
        pass

    accessKey       = attr_property("accesskey")
    align           = attr_property("align")
