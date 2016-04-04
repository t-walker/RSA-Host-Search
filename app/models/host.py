# A model for a host found on a network.
# Properties:
#  IP Address - ipaddr [UNIQUE]
#  Host Name - hostname [UNIQUE]
#  RSA Certificate - rsacertificate_id (from rsacertificate)
#  Device Type - devicetype_id (from devicetype)
#  Organization - organization_id (from organization)
#  Country - country_id (from country)
#  Operating System - os_id (from country)
#  Industry - industry_id (from industry)
class Host(db.Model):
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    ipaddr = db.Column(db.String(1000), index=True, unique=True)
    hostname = db.Column(db.String(1000), index=True, unique=True)
    certificate_id = db.Column(db.Integer, db.ForeignKey('certificate.id'))
    devicetype_id = db.Column(db.Integer, db.ForeignKey('devicetype.id'))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    industry_id = db.Column(db.Integer, db.ForeignKey('industry.id'))

    def __repr__(self):
        return '<Host %r>' % (self.name)
