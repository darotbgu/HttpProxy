class Repository(object):

    def __init__(self, model, db_handler):
        self._model = model
        self._db = db_handler

    def find_all(self):
        """
        Retrieves all the objects in this repository
        :return: objects of type model
        """
        return self._db.findlall(self._model)

    def find(self, **kwargs):
        """
        Filters the repository with the given kwargs and returns the first one
        :param kwargs: filter options
        :return: object matching the filter
        """
        return self._db.find(self._model, **kwargs)

    def store(self, obj):
        """
        Store object in this repository
        :param obj: object to store
        """
        return self._db.store(obj)
