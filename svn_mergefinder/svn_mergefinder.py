
# svn:mergeinfo text dump looks like one of these:
#
# svn://URL/path/to/file-or-dir -
#   /branches/a/b/c:9000
#   /branches/a/b/d:9006
#   /branches/a/c/x:2911
#   . . .
# svn://URL/path/to/file-or-dir - /branches/a/b/c:9000-9100
#
# svn://chinook/eps/branches/9.8/maintenance/PRN21648/src/tests/com/et/testframework/ETAssert.java - 
# svn://chinook/eps/branches/projects/merlin/src/tests/com/et/db/ETSerializableTest.java -
# /branches/9.10/maintenance/9.10.0112/src/tests/com/et/db/ETSerializableTest.java:9636
# /branches/9.10/maintenance/PRN22102/src/tests/com/et/db/ETSerializableTest.java:9169
# /branches/9.10/maintenance/PRN22136/src/tests/com/et/db/ETSerializableTest.java:9272-9284
#
#

#f = open('mergeinfo_chinook_eps_branches.txt', 'r')

#import xml.etree.ElementTree
#from xml.etree.ElementTree import ElementTree
#
#f = open('mini.xml', 'r')
#parsed = xml.parse(f)
#print parsed
#
#print "parsed is element:", xml.iselement(parsed)
# xml.dump(parsed)


#_element = xml.etree.ElementTree.Element(f)
#print "_element is an element:", xml.etree.ElementTree.iselement(_element)
#print _element.tag
#print _element.tail
#print _element.attrib
#print _element.items()
#
#_iterparse = xml.etree.ElementTree.Element(f)
#print "_iterparse is an element:", xml.etree.ElementTree.iselement(_iterparse)
#print _iterparse
#for event, elem in _iterparse:
#    print "none"
#    print event, elem

#print _iterparse.tag
#print _iterparse.tail
#print _iterparse.attrib
#print _iterparse.items()

#tree = ElementTree()
#tree.parse('mini.xml')
#print tree
#print "tree is an element:", xml.etree.ElementTree.iselement(tree)
#prop = tree.find("property")
#print "prop:", prop


E:\Source\git\scmtools\svn_mergefinder>python
Python 2.6.3 (r263rc1:75186, Oct  2 2009, 20:40:30) [MSC v.1500 32 bit (Intel)]
on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from xml.etree.ElementTree import ElementTree
>>> tree = ElementTree()
>>> tree.parse('mini.xml')
<Element properties at b99af8>
>>> target_iter = tree.getiterator("target")
>>> for element in target_iter:
...   for i in range(len(element.getchildren())):
...     if element.getchildren()[i].attrib['name'] == 'svn:mergeinfo':
...       print element.getchildren()[i].text
...



            /branches/9.10/maintenance/9.10.0112/src/tests/com/et/db/ETSerializableTest.java:9636
            /branches/9.10/maintenance/PRN22102/src/tests/com/et/db/ETSerializableTest.java:9169
            /branches/9.10/maintenance/PRN22136/src/tests/com/et/db/ETSerializableTest.java:9272-9284
            /branches/9.10/maintenance/PRN22174/src/tests/com/et/db/ETSerializableTest.java:9377-9605
            /branches/9.10/maintenance/PRN22180/src/tests/com/et/db/ETSerializableTest.java:9354-9494
            /branches/9.10/maintenance/PRN22193/src/tests/com/et/db/ETSerializableTest.java:9386-9406
            /branches/9.10/maintenance/base/src/tests/com/et/db/ETSerializableTest.java:8839-9353,9393
            /branches/9.10/maintenance/slider/src/tests/com/et/db/ETSerializableTest.java:8868-9350
            /branches/9.7/Initial/base/src/tests/com/et/db/ETSerializableTest.java:6330-6336
            /branches/9.7/SP1/EB/AFB/src/tests/com/et/db/ETSerializableTest.java:7083-7691
            /branches/9.7/SP1/EB/Lufthansa/src/tests/com/et/db/ETSerializableTest.java:6733-7809
            /branches/9.7/SP1/base/src/tests/com/et/db/ETSerializableTest.java:6337-6823
            /branches/9.8/Initial/PRN21559/src/tests/com/et/db/ETSerializableTest.java:8204
            /branches/9.8/Initial/maintenance/src/tests/com/et/db/ETSerializableTest.java:7598-8317
            /branches/9.8/maintenance/PRN18690/src/tests/com/et/db/ETSerializableTest.java:8458
            /branches/9.8/maintenance/PRN21731/src/tests/com/et/db/ETSerializableTest.java:8557-8570
            /branches/9.8/maintenance/PRN21869/src/tests/com/et/db/ETSerializableTest.java:8835-8858
            /branches/9.8/maintenance/base/src/tests/com/et/db/ETSerializableTest.java:9095-9229
            /branches/9.8/maintenance/src/tests/com/et/db/ETSerializableTest.java:8318-8452
            /branches/9.8/maintenance_TEMP/src/tests/com/et/db/ETSerializableTest.java:8453-8454
            /branches/9.9/maintenance-TEMP/src/tests/com/et/db/ETSerializableTest.java:8584
            /branches/9.9/maintenance/base/src/tests/com/et/db/ETSerializableTest.java:8585-8967
            /branches/9.9/maintenance/src/tests/com/et/db/ETSerializableTest.java:8317-8583
            /branches/projects/PKI09/src/tests/com/et/db/ETSerializableTest.java:7599-8298
            /tags/9.7/SP1/base/9.7.0100.32_r6820_buildtools_r527/src/tests/com/et/db/ETSerializableTest.java:6825-7082
            /trunk/src/tests/com/et/db/ETSerializableTest.java:2-5373,8869-9370




            /branches/9.10/maintenance/9.10.0112/src/tests/com/et/db/ETSerializableTest.java:9635-9643
            /branches/9.10/maintenance/PRN22102/src/tests/com/et/db/ETSerializableTest.java:9169
            /branches/9.10/maintenance/PRN22136/src/tests/com/et/db/ETSerializableTest.java:9272-9284
            /branches/9.10/maintenance/PRN22174/src/tests/com/et/db/ETSerializableTest.java:9377-9634
            /branches/9.10/maintenance/PRN22180/src/tests/com/et/db/ETSerializableTest.java:9424,9453
            /branches/9.10/maintenance/PRN22193/src/tests/com/et/db/ETSerializableTest.java:9384-9403
            /branches/9.10/maintenance/slider/src/tests/com/et/db/ETSerializableTest.java:8868-9350
            /branches/9.8/Initial/PRN21559/src/tests/com/et/db/ETSerializableTest.java:8204
            /branches/9.8/Initial/maintenance/src/tests/com/et/db/ETSerializableTest.java:7598-8317
            /branches/9.8/maintenance/PRN18690/src/tests/com/et/db/ETSerializableTest.java:8458
            /branches/9.8/maintenance/PRN21731/src/tests/com/et/db/ETSerializableTest.java:8557-8570
            /branches/9.8/maintenance/PRN21869/src/tests/com/et/db/ETSerializableTest.java:8835-8858
            /branches/9.8/maintenance/base/src/tests/com/et/db/ETSerializableTest.java:9095-9229
            /branches/9.8/maintenance/src/tests/com/et/db/ETSerializableTest.java:8318-8452
            /branches/9.8/maintenance_TEMP/src/tests/com/et/db/ETSerializableTest.java:8453-8454
            /branches/9.9/maintenance-TEMP/src/tests/com/et/db/ETSerializableTest.java:8584
            /branches/9.9/maintenance/base/src/tests/com/et/db/ETSerializableTest.java:8585-8967
            /branches/9.9/maintenance/src/tests/com/et/db/ETSerializableTest.java:8317-8583
            /branches/projects/merlin/src/tests/com/et/db/ETSerializableTest.java:9060
            /trunk/src/tests/com/et/db/ETSerializableTest.java:2-5373,7600-8865


            /branches/9.10/maintenance/9.10.0112/docs:9636
            /branches/9.10/maintenance/PRN22180/docs:9424


            /branches/9.8/maintenance/PRN18690/src/clients/AVPlayer/Dialogs/MiniRecorder.es.resx:8458
            /branches/9.9/maintenance/base/src/clients/AVPlayer/Dialogs/MiniRecorder.es.resx:8647-8676,8691-8770
            /trunk/src/clients/AVPlayer/Dialogs/MiniRecorder.es.resx:8559,8741


            /branches/9.7/Initial/base/src/server:6330-6336
            /branches/9.7/SP1/EB/DMCC/src/server:6683-7744
            /branches/9.7/SP1/base/src/server:6337-6682
            /branches/projects/DMCC09/src/server:7540-7863
            /branches/projects/July09/src/server:7600-8120
            /trunk/src/server:6542-7602

>>>

