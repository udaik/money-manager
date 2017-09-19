from pymodm import EmbeddedMongoModel, fields

class CreditCard(EmbeddedMongoModel):
    cardName = fields.CharField()
    cardNumber = fields.IntegerField()
    cardType = fields.CharField()
    totalLiability = fields.CharField()
    creditLimit = fields.FloatField()
    cashLimit = fields.FloatField()
    availableCredit = fields.FloatField()
    loyaltyPoints = fields.FloatField()
    minimumPaymentDue = fields.FloatField()
    dueDate = fields.DateTimeField()
