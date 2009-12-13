# http://www.mail-archive.com/svnmerge@orcaware.com/msg00618.html

import os
from xml.dom import pulldom

class SvnLogParser:
    def __init__(self, f):
        self._events = pulldom.parse(f)
    def __getitem__(self, idx):
        for event, node in self._events:
            if event == pulldom.START_ELEMENT and node.tagName == "logentry":
                self._events.expandNode(node)
                return self.SvnLogRevision(node)
        raise IndexError

    class SvnLogRevision:
        def __init__(self, xmlnode):
            self._node = xmlnode
        def revision(self):
            return self._node.getAttribute("revision")
        def author(self):
            return self._node.getElementsByTagName("author")[0].firstChild.data
        def msg(self):
            return self._node.getElementsByTagName("msg")[0].firstChild.data
        def paths(self):
            paths = []
            for n in self._node.getElementsByTagName("path"):
                paths.append(self.SvnLogPath(n))
            return paths

        class SvnLogPath:
            def __init__(self, xmlnode):
                self._node = xmlnode
            def action(self):
                return self._node.getAttribute("action")
            def pathid(self):
                return self._node.firstChild.data
            def copyfrom_rev(self):
                return self._node.getAttribute("copyfrom-rev")
            def copyfrom_pathid(self):
                return self._node.getAttribute("copyfrom-path")
            def copyfrom_msg(self):
                return self._node.getAttribute("copyfrom-msg")

def svnlog(target):
    #return SvnLogParser(os.popen("svn log --xml -v %s" % target))
    return SvnLogParser(os.popen("svn log --xml --verbose --stop-on-copy %s" % target))

if __name__ == "__main__":
    import sys
    URL = sys.argv[1]
    #URL = "http://svn.collab.net/repos/svn/trunk/contrib/client-side/svnmerge/svnmerge.py";
    #URL = "svn://chinook/eps/branches/projects/PKI09";
    #URL = 'svn://chinook/eps/branches/projects/PKI09'
    #URL = 'svn://chinook/eps/branches/9.0/SP4/PRN21413'
    #URL = 'svn://chinook/eps/branches/9.8/Initial/maintenance'
    #URL = 'svn://chinook/Tate'
    for chg in svnlog(URL):
        msg = chg.msg().encode('utf-8').strip()
        # this doesn't work - maybe it's the wrong encoding?
        if msg.startswith("00000"):
            pass
        print chg.msg(), '(r' + chg.revision() + ',', chg.author() + ')'

        # TODO sort messages by PRN no., then pretty print PRN header followed
        # by a list of the associated commits underneath (maybe indented a
        # couple spaces)

#        print '  ', 'author:', chg.author()
#        print '  ', chg.msg()
#        for p in chg.paths():
#            print "   ", p.action(), p.pathid(), p.copyfrom_rev(), p.copyfrom_pathid()#, p.copyfrom_msg()

