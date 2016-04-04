# A model for a RSA Certificate.
# Properties:
#  ID - id [UNIQUE]
#  Certificate Modulus - value [UNIQUE]
class Certificate(db.Model):
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(5000), index=True, unique=True)

    # Relationships
    hosts = db.relationship('Host', backref='Certificate', lazy='dynamic')

    def __repr__(self):
        return '<Certificate %r>' % (self.name)
