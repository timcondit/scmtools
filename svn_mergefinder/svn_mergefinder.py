#!python
#
# svn_mergefinder.py: given a branch ID, find all other places that the branch
# has been merged into.  The inputs to the program are the XML file generated
# by Subversion (with "svn propget svn:mergeinfo URL") and a string
# representing a branch.

import os.path
import sys
from xml.etree.ElementTree import ElementTree

DEBUG = False

class MergeFinder(object):
    '''DOCSTRING'''
    def __init__(self, merge_dat, branch_str):
        '''DOCSTRING'''
        self.branch_str = os.path.normpath(branch_str)
        tree = ElementTree(file=merge_dat)
        print "# searching for merge targets for '%s'" % branch_str
        self.mi_dict = {}
        parent_map = dict((c, p) for p in tree.getiterator() for c in p)
        for target in parent_map:   # URL
            for property in target: # paths
                _list = []
                # CAREFUL: this matches on whitespace, so it's affected by
                # the formatting of the file
                if property.text:
                    for line in property.text.splitlines():
                        ln = line.strip()
                        if ln == "":
                            if DEBUG:
                                print "[DEBUG] skipping empty string"
                        else:
                            _list.append(os.path.normpath(ln))
                    if len(_list) > 0:
                        self.mi_dict[target.attrib['path']] = _list

    def match(self):
        '''DOCSTRING'''
        path_dict = {}
        for url, paths in self.mi_dict.items():
            for path in paths:
                if self.branch_str in path:
                    path_dict[url] = path
        return path_dict

    def path_reduce(self, _path):
        '''DOCSTRING'''
        top_level_contents = [
                '.classpath',
                '.project',
                'GenStubSkel.bat',
                'GenStubSkel.xml',
                'buildNativeServiceWin32.bat',
                'buildXFloorWnd.bat',
                'config',
                'docs',
                'documentation',
                'kill.exe',
                'sdk',
                'setup',
                'src',
                'workdir',
        ]
        for tlc in top_level_contents:
            if tlc in _path:
                _path = _path.partition(tlc)[0]
        # If we get here, assume for now that _path is already reduced.  I
        # don't care for the rstrip, but it's quick and effective.
        return _path.rstrip(r'/')

if __name__ == '__main__':
#    mf = MergeFinder('mini.xml', r"branches/9.10/maintenance/9.10.0112")
#    mf = MergeFinder('mergeinfo_chinook_eps_branches.xml', r"branches/9.10/maintenance/9.10.0112")
    mf = MergeFinder(sys.argv[1], sys.argv[2])
    reduced = []
    for line in sorted(mf.match()):
        redline = mf.path_reduce(line)
        if redline not in reduced:
            reduced.append(mf.path_reduce(line))
    for url in reduced:
        print "URL: %s" % url
