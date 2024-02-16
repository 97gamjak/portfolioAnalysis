import datetime as dt


class RollOption:
    def __init__(self,
                 premium,
                 commission=0.0,
                 roll_date=dt.date.today(),
                 expiration_date=dt.date.today()
                 ):

        self.premium = premium
        self.commission = commission
        self.roll_date = roll_date
        self.expiration_date = expiration_date
