from util.oss import helper
from util.oss import const_var
oss_catalog = const_var.CATALOG
oss_http_url = const_var.URL
def upload_many_to_oss(image_bytes_points):
    # print(image_bytes_points)
    path_points = []
    for item in image_bytes_points:
        _path = _upload_one_to_oss(item['byte'])
        path_points.append({'path': _path, 'points': item['points']})
    return path_points



def _upload_one_to_oss(file_name,_byte):
    """上传到oss"""
    path = '{0}{1}'.format(oss_catalog,file_name)
    if helper.upload(path, _byte):
        return oss_http_url+path
    else:
        return False
