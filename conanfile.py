#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class OpenMAXDLConan(ConanFile):
    name = "openmax_dl"
    version = "1.0.2"
    url = "https://github.com/bincrafters/conan-openmax_dl"
    author = "Bincrafters <bincrafters@gmail.com>"
    description = "OpenMAX™ is a royalty-free, cross-platform API that provides comprehensive streaming media codec " \
                  "and application portability by enabling accelerated multimedia components to be developed, " \
                  "integrated and programmed across multiple operating systems and silicon platforms"
    no_copy_source = True
    license = "Khronos"
    exports = ["LICENSE.md"]

    def source(self):
        tools.get('https://www.khronos.org/registry/OpenMAX-DL/api/1.0/omx_dl_v1_0_2.h.zip')

    def package(self):
        self.copy(pattern="*.h", dst="include")

    def package_id(self):
        self.info.header_only()
