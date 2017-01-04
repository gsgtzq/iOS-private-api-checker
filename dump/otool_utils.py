#coding=utf-8
'''
Created on 2015年10月29日

@author: atool
'''

import subprocess
import re

otool_path = "otool" #otool所在的位置

def otool_app(app_path):
    """
    Get framework included in app
    Args:
        Mach-o path
    Returns:
        two sets, one is public framework, one is private framework
    """
    out = subprocess.check_output([otool_path, '-L', app_path])
    pattern = re.compile(r"PrivateFrameworks\/(\w*)\.framework")
    pub_pattern = re.compile(r"Frameworks\/([\.\w]*)")

    private = set()
    public = set()

    for r in re.finditer(pattern, out):
        private.add(r.group(1))

    for r in re.finditer(pub_pattern, out):
        public.add(r.group(1))

    return private, public
