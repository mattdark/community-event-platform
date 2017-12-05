from lxml import etree
import cairosvg
import json

def showspeaker():

    with open('./speakers.json') as data_file:
        data = json.load(data_file)

    id = list()
    name = list()

    for i in range(len(data["speakers"])):
        id.append(data["speakers"][i]["id"])
        name.append(data["speakers"][i]["name"])

    #for i in range(len(data["attendees"])):
    return id, name

def generate(speakers):
    SVGNS = u"http://www.w3.org/2000/svg"

    with open('./static/assets/cert.svg', 'r') as mysvg:
        svg = mysvg.read()

    utf8_parser = etree.XMLParser(encoding='utf-8')

    xml_data = etree.fromstring(svg.encode('utf-8'), parser=utf8_parser)
    find_name = etree.ETXPath("//{%s}tspan[@id='tspan3951']" % (SVGNS))

    namelist = list()
    filelist = list()

    with open('./speakers.json') as data_file:
        data = json.load(data_file)

    for i in speakers:
        id = data["speakers"][int(i)-1]["id"]
        name = data["speakers"][int(i)-1]["name"]
        namelist.append(name)
        find_name(xml_data)[0].text = name
        new_svg = etree.tostring(xml_data).decode('utf-8')
        svg_file = './static/certificates/' + id + '.svg'
        f = open(svg_file, 'w+')
        f.write(new_svg)
        f.close()
        pdf_file = './static/certificates/' + id + '.pdf'
        filelist.append(id + '.pdf')
        cairosvg.svg2pdf(url=svg_file, write_to=pdf_file)

    return namelist, filelist
