# A model for a country.
# Properties:
#  ID - id [UNIQUE]
#  Device Type - name [UNIQUE]
class DeviceType(db.Model):
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    # Relationships
    hosts = db.relationship('Host', backref='DeviceType', lazy='dynamic')

    def __repr__(self):
        return '<Device Type %r>' % (self.name)
