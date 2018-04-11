import exiftool
import translate
exiftool.executable='./ExifTool/exiftool'

def getMetaData(file):
    with exiftool.ExifTool() as et:
        metadata = et.get_metadata(file)
    return showMetaData(metadata)

def getMetaDataBatch(files):
    with exiftool.ExifTool() as et:
        metadata =et.get_metadata_batch(files)
    return metadata

def showMetaData(data):
    list = []
    for key in data:
        keytemp=key.split(':')
        if(len(keytemp)>1):
            name_cn=translate.translate(keytemp[1])
            each = {'type': keytemp[0],'name':keytemp[1],'name_cn':name_cn,'value': data[key]}
            list.append(each)
        else:
            each = {'type': '', 'name': keytemp, 'value': data[key]}
            list.append(each)
    return list

def showMetaDataBatch(data):
    for item in data:
        showMetaData(item)