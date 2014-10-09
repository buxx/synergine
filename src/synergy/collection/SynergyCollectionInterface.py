class SynergyCollectionInterface():

    def get_computable_objects(self):
        raise NotImplementedError

    def cycle(self, context):
        raise NotImplementedError