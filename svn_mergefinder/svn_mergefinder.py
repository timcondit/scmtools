#!python
#
# svn_mergefinder.py
#
# Description: given a specific branch, as identified by a copy operation,
#   find all other branches where the transactions of the current branch have
#   been merged.
#
#   In other words, take a branch.  Get the list of transactions on that
#   branch going back to the copy operation in which the branch was created.
#   Using that list, find all other branches in the same repository which
#   contain svn:mergeinfo records of each of those transactions, signifying a
#   merge operation.

from xml.etree.ElementTree import ElementTree


# Generates a dictionary with (key = target URL) and (value = list of paths
# with their transactions).  It looks like this.  Note the empty list at the
# end.
#
# {
# 'svn://chinook/eps/branches/projects/merlin10/docs': [
#    '/branches/9.10/maintenance/9.10.0112/docs:9636',
#    '/branches/9.10/maintenance/PRN22180/docs:9424' ],
#
# 'svn://chinook/eps/branches/developers/danf/RadUpdate/src/server': [
#    '/branches/9.7/Initial/base/src/server:6330-6336',
#    '/branches/9.7/SP1/EB/DMCC/src/server:6683-7744',
#    '/branches/9.7/SP1/base/src/server:6337-6682',
#    '/branches/projects/DMCC09/src/server:7540-7863',
#    '/branches/projects/July09/src/server:7600-8120',
#    '/trunk/src/server:6542-7602' ],
#
# 'svn://chinook/eps/branches/projects/Dartboard09/setup/installs/Server': [],
# }

tree = ElementTree(file='mini.xml')
parent_map = dict((c, p) for p in tree.getiterator() for c in p)
mergeinfo_dict = {}
for target in parent_map:   # parent (URL)
    for property in target: # child (paths and txns)
        mergeinfo = property.text.splitlines()
        # TODO separate function?
        _list = []
        for line in mergeinfo:
            ln = line.strip()
#            _list.append(ln)
            # TODO Should I leave empty paths in for now?  I probably
            # shouldn't be doing *any* kind of processing at this point.
            if ln == "":
                pass
            else:
                _list.append(ln)
        mergeinfo_dict[target.attrib['path']] = _list
print mergeinfo_dict
#f = open("mergeinfo_dict.txt", "a")
#f.write(mergeinfo_dict)

# http://effbot.org/zone/element-lib.htm#prettyprint
# in-place prettyprint formatter
def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


