from lxml import etree

xlst_doc = etree.parse("C:\\Users\\shuqing\\Desktop\\xslt.xsl")
transformer = etree.XSLT(xlst_doc)

source_xml = etree.parse("C:\\Users\\shuqing\\Desktop\\test.xml")
output_doce =  transformer(source_xml)

output_doce.write("output-toc.html", pretty_print=True)