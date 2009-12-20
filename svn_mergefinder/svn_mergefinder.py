#!python
#
# svn_mergefinder.py
#
# Description: given a specific branch, find all other branches which contain
#   a merge reference to the given branch.

# The inputs to the program will be the XML file generated by Subversion
# (e.g., "svn propget svn:mergeinfo svn://Chinook/EPS") and some string to
# match agains, possibly the URL of the branch in question, with or without
# the trailing slash.
#
# Originally I was planning to parse the logs for the given branch back to the
# copy operation, but there's no reason to bother with that.  Just look for
# where the branch has been merged *to*.
#
# The hard part is deciding how much of the branch URL to use.  Maybe I should
# define the preamble as svn://Chinook/EPS/branches, and use whatever follows
# as the pattern to match.  Maybe a better idea is to match on whatever
# freeform hunk of text is provided.

import os.path
import sys
from xml.etree.ElementTree import ElementTree

DEBUG = False

class MergeFinder(object):
    '''DOCSTRING'''
    def __init__(self, data_file, branch_str):
        '''DOCSTRING'''
        self.data_file = data_file
        self.mi_dict = {}
        self.branch_str = os.path.normpath(branch_str)

    def mergeinfo_dict(self):
        '''return all URLs with properties containing PATH text'''
        tree = ElementTree(file=self.data_file)
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
        return self.mi_dict

    # NB: There are only zero or one possible matching paths per branch (TODO
    # why?), so this is sort of broken.  Usually a merge will consist of
    # multiple paths in the same base URL.  So while they are separated here,
    # if would be nice if all paths that share a common base URL were
    # collected together.
    def mergefinder(self):
        '''DOCSTRING'''
        path_dict = {}
        for url, paths in self.mi_dict.items():
            for path in paths:
                if self.branch_str in path:
                    path_dict[url] = path
        return path_dict

    def ugly_print(self, dict):
        '''DOCSTRING'''
        for key, values in dict.items():
            print "URL:", key
            for value in values.splitlines():
                print "  PATH:", value
            print

if __name__ == '__main__':
    mf = MergeFinder('mini.xml', r"branches/9.10/maintenance/9.10.0112")
    mf.mergeinfo_dict()
    mf.ugly_print(mf.mergefinder())

