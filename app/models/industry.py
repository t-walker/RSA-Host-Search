# A model for an industry.
# Properties:
#  ID - id [UNIQUE]
#  Industry Name - name [UNIQUE]
class Industry(db.Model):
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    organizations = db.relationship('Organization', backref='industry', lazy='dynamic')

    # Relationships
    hosts = db.relationship('Host', backref='Industry', lazy='dynamic')

    def __repr__(self):
        return '<Industry %r>' % (self.name)
