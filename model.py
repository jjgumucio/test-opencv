from google.appengine.ext import ndb


class FileReference(ndb.Model):
    """Saves needed info of a file generated in Compute Engine instance

    Extends:
        ndb.Model

    Variables:
        path {str} -- The path where the file was stored
        other_info {JSON} -- Other field to store (date and time processed)
    """
    file_path = ndb.StringProperty()
    # JSON cannot be used when inserting using API
