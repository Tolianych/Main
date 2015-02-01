import base64, zlib, os
from xml.dom.minidom import parseString

PATH = 'D:\\Polygon\\ACEP\\'
RESULT_PATH = 'D:\\Polygon\\ACEP\\' 

def fileScaner():
    xmlfiles = [os.path.join(root, name)
                for root, dirs, files in os.walk(PATH)
                for name in files
                if name.endswith((".xml"))]

    count = 0
    for filePath in xmlfiles:
        print(filePath)
        count = count + 1

    print(count)
    return xmlfiles
    
def converter(fileList):
    number = 0
    for item in fileList:
        number += 1
        
        file = open(item, 'r')
        text = file.read()    

        base_start = text.find('<![CDATA[')
        base_end = text.find(']]></HostStatistic>')
        base = text[base_start + 9 : base_end]

        archive = bytes(base, 'UTF-8') 
        zipped = base64.b64decode(archive)
        unzipped = zlib.decompress(zipped)
        cuted = unzipped[3 : ]

        xml = str(cuted, 'utf-8')
        if number <= 9:
            result = open(str(RESULT_PATH) + 'resultACEP-0000' + str(number) + '.xml', 'w', encoding='utf-8')
        elif number > 9 and number <= 99:
            result = open(str(RESULT_PATH) + 'resultACEP-000' + str(number) + '.xml', 'w', encoding='utf-8')
        elif 999 >= number > 99:
            result = open(str(RESULT_PATH) + 'resultACEP-00' + str(number) + '.xml', 'w', encoding='utf-8')
        elif 9999 >= number >999:
            result = open(str(RESULT_PATH) + 'resultACEP-0' + str(number) + '.xml', 'w', encoding='utf-8')
        elif number > 99999:
            result = open(str(RESULT_PATH) + 'resultACEP-' + str(number) + '.xml', 'w', encoding='utf-8')

        result.write(xml)
        result.close()
        
def findOStypes():
    acepFiles = os.listdir(RESULT_PATH)
    for acepFile in acepFiles:
        file = open(acepFile, 'r', encoding='utf-8')
        text = file.read()
        tegVMsBegin = text.find('<VirtualMachine>')
        tegVMsEnd = text.find('</VirtualMachine>')
        tegVMs = text[tegVMsBegin + 1 : tegVMsEnd - 1]
        
        osNameStart = tegVMs.find('OperatingSystem=')
        osNameEnd = tegVMs.find(' Parent')
        osName = tegVMs[osNameStart + 1 : osNameEnd - 1]
        

def execute():
    fileList = fileScaner()
    converter(fileList)

if __name__ == '__main__':
    execute()