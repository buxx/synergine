class MetaCollections():
    def __init__(self):
        self._metas = {}

    def reset(self):
        self._metas = {}

    def get_collection(self, name):
        if name not in self._metas:
            self._metas[name] = {}
        return self._metas[name]

    def get(self, name, subject, allow_empty=False):
        metas = self.get_collection(name)
        if subject not in metas and allow_empty:
            metas[subject] = []
        return metas[subject]

    def add(self, name, subject, value, assert_not_in=True, allow_multiple=False):
        collection = self.get(name, subject, allow_empty=True)
        if value in collection:
            if assert_not_in:
                raise Exception()  # TODO: Exception perso
            if not allow_multiple:
                return
        collection.append(value)

    def remove(self, name, subject, value, allow_empty=False, allow_not_in=False):
        collection = self.get(name, subject, allow_empty=allow_empty)
        try:
            collection.remove(value)
        except ValueError:
            if not allow_not_in:
                raise

    def have(self, name, subject, value, allow_empty=False):
        collection = self.get(name, subject, allow_empty)
        return value in collection

    def clean(self, name):
        metas = self.get_collection(name)
        cleaned_metas = dict(metas)
        for meta in metas:
            if not len(metas[meta]):
                del (cleaned_metas[meta])
        self._metas[name] = cleaned_metas
