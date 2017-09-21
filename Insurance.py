from pymodm import fields

class Insurance(BaseAccount):
    sumAssured = fields.CharField()
    tenure = fields.CharField()
    premiumDate = fields.DateTimeField()
    startDate = fields.DateTimeField()
    maturityDate = fields.DateTimeField()
    frequency = fields.CharField()
    policyType = fields.CharField()
    premiumPaymentTerm = fields.IntergerField()
    policyName = fields.CharField()
    bonus = fields.FloatField()
    maturityBenefit = fields.FloatField()

    def populate(self):
        print("Adding Insurance Account")
        self.name = input("Name: ")
        self.balance = 0.0
        self.description = input("Description: ")
        self.sumAssured = 0.0
        self.tenure = 0.0
        self.frequency = 0.0
