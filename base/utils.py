import os
import uuid


def rename_uploaded_file(instance, filename):
    """
    Rename a file uploaded (not via Django-ckeditor).
    """

    extension = os.path.splitext(filename)[1]
    new_filename = f"{uuid.uuid4().hex}{extension}"
    return os.path.join(instance.image_upload_folder, new_filename)

def rename_uploaded_file_ckeditor(filename, request):
    """
    Rename a file uploaded via Django-ckeditor.
    """

    extension = os.path.splitext(filename)[1]
    new_filename = f"{uuid.uuid4().hex}{extension}"
    return new_filename