from lxml import etree
import cairosvg
import json
from modules import dates

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

    with open('./static/assets/invitation.svg', 'r') as mysvg:
        svg = mysvg.read()

    utf8_parser = etree.XMLParser(encoding='utf-8')

    xml_data = etree.fromstring(svg.encode('utf-8'), parser=utf8_parser)
    find_name = etree.ETXPath("//{%s}tspan[@id='tspan5652']" % (SVGNS))
    find_org = etree.ETXPath("//{%s}tspan[@id='tspan5656']" % (SVGNS))
    fecha = list()
    fecha.append(etree.ETXPath("//{%s}tspan[@id='tspan5934-3']" % (SVGNS)))
    fecha.append(etree.ETXPath("//{%s}tspan[@id='tspan5930']" % (SVGNS)))
    fecha.append(etree.ETXPath("//{%s}tspan[@id='tspan5932']" % (SVGNS)))
    fecha.append(etree.ETXPath("//{%s}tspan[@id='tspan5934']" % (SVGNS)))

    namelist = list()
    filelist = list()
    ds = dates.dates()

    with open('./speakers.json') as data_file:
        data = json.load(data_file)

    for i in speakers:
        id = data["speakers"][int(i)-1]["id"]
        name = data["speakers"][int(i)-1]["name"]
        org = data["speakers"][int(i)-1]["org"]
        namelist.append(name)
        find_name(xml_data)[0].text = name
        find_org(xml_data)[0].text = org
        for i in range(4):
            fecha[i](xml_data)[0].text = ds[i]
        new_svg = etree.tostring(xml_data).decode('utf-8')
        svg_file = './static/invitations/' + id + '.svg'
        f = open(svg_file, 'w+')
        f.write(new_svg)
        f.close()
        pdf_file = './static/invitations/' + id + '.pdf'
        filelist.append(id + '.pdf')
        cairosvg.svg2pdf(url=svg_file, write_to=pdf_file)

    return namelist, filelist
