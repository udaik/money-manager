from pymodm import connect
from pymongo.write_concern import WriteConcern
from pymodm import EmbeddedMongoModel, MongoModel, fields
from pymodm.errors import ValidationError, ConfigurationError

import config as CONFIG

connect(CONFIG.URI, alias=CONFIG.CONN_NAME)

class BaseClass(MongoModel):
    name = fields.CharField(primary_key = True)
    baseattr = fields.CharField()

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = CONFIG.CONN_NAME
        collection_name = "BaseClass"

class DerivedClass(BaseClass):
    dspecific = fields.CharField()

baseClass = BaseClass(name="SBI-Salary1", baseattr="ASSET").save()
baseClass = BaseClass(name="SBI-Salary2", baseattr="ASSET").save()
baseClass = BaseClass(name="SBI-Salary3", baseattr="ASSET").save()
baseClass = BaseClass(name="SBI-Salary4", baseattr="ASSET").save()

derivedObj = DerivedClass(name="d-salary1", baseattr="d-Asset1", dspecific='xyz1').save()
derivedObj = DerivedClass(name="d-salary2", baseattr="d-Asset2", dspecific='xyz2').save()
derivedObj = DerivedClass(name="d-salary3", baseattr="d-Asset3", dspecific='xyz3').save()
derivedObj = DerivedClass(name="d-salary4", baseattr="d-Asset4", dspecific='xyz4').save()

# print(BaseClass.objects.all())
print("base class count", BaseClass.objects.count())
print("derived class count", DerivedClass.objects.count())
