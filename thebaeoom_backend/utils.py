import datetime
import os
import uuid


def get_file_upload_path(instance, filename):
    ext = filename.split(".")[-1]
    d = datetime.datetime.now()
    filepath = d.strftime("%Y/%m/%d")
    suffix = d.strftime("%Y%m%d%H%M%S")
    filename = "%s_%s.%s" % (uuid.uuid4().hex, suffix, ext)
    return os.path.join(filepath, filename)


def get_ckeditor_upload_path(filename, request):
    ext = filename.split(".")[-1]
    d = datetime.datetime.now()
    filepath = d.strftime("%Y/%m/%d")
    suffix = d.strftime("%Y%m%d%H%M%S")
    filename = "%s_%s.%s" % (uuid.uuid4().hex, suffix, ext)
    return os.path.join(filepath, filename)
