from arc_set import ArcSet


class ArcTable(ArcSet):

    def __init__(self, uri, folder, db_client, SR_id=4326):
        super().__init__(uri, folder, db_client, SR_id=SR_id)
        self.load_meta_data()

    def load_meta_data(self):
        try:
            self.loaded = super().load_meta_data()
        except Exception as e:
            self.add_error(e)
            self.loaded = False
        finally:
            return self.loaded
