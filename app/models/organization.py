# A model for an organization.
# Properties:
#  ID - id [UNIQUE]
#  Organization Name - name [UNIQUE]
#  Country - country_id
#  Industry - industry_id
class Organization(db.Model):
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    industry_id = db.Column(db.Integer, db.ForeignKey('industry.id'))

    # Relationships
    hosts = db.relationship('Host', backref='Organization', lazy='dynamic')

    def __repr__(self):
        return '<Organization %r>' % (self.name)
