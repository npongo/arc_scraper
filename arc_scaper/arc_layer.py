from arc_set import ArcSet


class ArcLayer(ArcSet):

    def __init__(self, uri, folder, db_client):
        super().__init__(uri, folder, db_client)
        self.load_meta_data()

    @property
    def has_Z(self):
        return bool(self.raw_json.get('hasZ', False))

    @property
    def has_M(self):
        return bool(self.raw_json.get('hasM', False))

    @property
    def geometry_field_name(self):
        return ([f['name'] for f in self.fields if f['type'] == "esriFieldTypeGeometry"] + [""])[0]

    def load_meta_data(self):
        try:
            self.loaded = super().load_meta_data()
        except Exception as e:
            self.add_error(e)
        finally:
            return self.loaded

