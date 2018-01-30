from flask import Blueprint,jsonify,request
from translate import main as translate
from werkzeug.utils import secure_filename
from util.oss import oss_helper
import os,time,uuid
# import app
upload = Blueprint('upload',__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['pdf'])
GENERATE_FOLDER ='generates'
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@upload.route('',methods=['POST'])
def upload_file():
    file = request.files['file_data']
    if file and allowed_file(file.filename):
        start = time.time()
        ec_file,oc_file = translate.main(file)
        print('use time {0} S'.format(time.time()-start))
        filename = secure_filename(file.filename)
        # file.save(os.path.join(UPLOAD_FOLDER, filename))
        file_ec_name = str(uuid.uuid4()).replace('-', '')+'.docx'
        file_oc_name = str(uuid.uuid4()).replace('-', '')+'.docx'
        _path_ec = os.path.join(GENERATE_FOLDER, file_ec_name)
        _path_oc = os.path.join(GENERATE_FOLDER, file_oc_name)
        ec_file.save(_path_ec)
        oc_file.save(_path_oc)
        with open(_path_ec,'rb') as f:
            file_ec_name_url = oss_helper._upload_one_to_oss(file_ec_name,f)
            if not file_ec_name_url:
                file_ec_name_url =''
        with open(_path_oc,'rb') as f:
            file_oc_name_url = oss_helper._upload_one_to_oss(file_oc_name,f)
            if not file_oc_name_url:
                file_oc_name_url =''
        # oss_helper._upload_one_to_oss(file_oc_name,_path_oc)
        return jsonify({'code':200,'msg':'success','data':{'ec_url':file_ec_name_url,'oc_url':file_oc_name_url}})
        
    return jsonify({'code':400,'msg':'not pdf or no file'})