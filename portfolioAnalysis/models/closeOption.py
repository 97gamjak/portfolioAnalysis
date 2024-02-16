import datetime as dt


class CloseOption:
    def __init__(self,
                 premium,
                 commission=0.0,
                 close_date=dt.date.today()
                 ):

        self.premium = premium
        self.commission = commission
        self.close_date = close_date
