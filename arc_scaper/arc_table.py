from arc_set import ArcSet


class ArcTable(ArcSet):

    def __init__(self, uri, folder, db_client):
        super().__init__(uri, folder, db_client)
        self.load_meta_data()

    def load_meta_data(self):
        try:
            self.loaded = super().load_meta_data()
        except Exception as e:
            self.add_error(e)
            self.loaded = False
        finally:
            return self.loaded
