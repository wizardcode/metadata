from flask import Flask
from flask import render_template
from flask import request
import time,json
from metadata import metadata as meta
application = Flask(__name__)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','bmp','doc','docx','html','mp3','zip'])
IMG_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif','bmp'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/upload',methods=['POST'])
def upload():
    f=request.files['file']
    if f and allowed_file(f.filename):
        name='./static/file/'+str(time.time())+'.'+str(f.filename.rsplit('.', 1)[1])
        f.save(name)
        metaData=meta.getMetaData(name)
        if f.filename.rsplit('.', 1)[1].lower() in IMG_EXTENSIONS:
            isImg=1
        else:
            isImg=0
        return json.dumps([isImg,name,metaData])
    else:
        return '0'

if __name__ == '__main__':
    application.debug=False
    application.run()
