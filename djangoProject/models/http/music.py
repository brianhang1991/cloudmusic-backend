class Music(object):
    def __init__(self, id, name, local_path):
        self.id = id
        self.name = name
        self.local_path = local_path

def object_2_json(object):
    return {
        "id": object.id,
        "name": object.name,
        "path": object.local_path
    }