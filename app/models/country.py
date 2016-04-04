# A model for a country.
# Properties:
#  ID - id [UNIQUE]
#  Country Name - name [UNIQUE]
class Country(db.Model):
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    organizations = db.relationship('Organization', backref='country', lazy='dynamic')

    # Relationships
    hosts = db.relationship('Host', backref='country', lazy='dynamic')
    def __repr__(self):
        return '<Country %r>' % (self.name)
