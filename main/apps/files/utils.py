import uuid


def uuid_gen_path(instance, filename):
    return '{0}/{1}'.format(uuid.uuid4(), filename)
