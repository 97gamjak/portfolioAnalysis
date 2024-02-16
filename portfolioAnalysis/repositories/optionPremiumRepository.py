import datetime as dt
import yfinance as yf
import pandas as pd
import time

from sqlmodel import Session, select
from PyQt6.QtCore import pyqtSignal, QObject

from portfolioAnalysis.db import sql_engine
from portfolioAnalysis.models.option import Option
from portfolioAnalysis.models.optionPremium import OptionPremium


class OptionPremiumRepository(QObject):
    maximum_progress = pyqtSignal(int)
    progress = pyqtSignal(int)

    def update(self):
        with Session(sql_engine) as session:
            statement = select(Option).where(
                Option.expiration_date >= dt.date.today())
            options = session.exec(statement).all()
            self.maximum_progress.emit(len(options))
            for i, option in enumerate(options):
                option_premium = get_option_premium_from_yf(option)

                if option_premium is None:
                    self.progress.emit(i)
                    continue

                statement = select(OptionPremium).where(
                    OptionPremium.option_id == option_premium.option_id)
                statement = statement.where(
                    OptionPremium.date == option_premium.date)

                exists = session.exec(statement).first() is not None
                if not exists:
                    session.add(option_premium)
                self.progress.emit(i)

            session.commit()

    def add_initial_option_premium_by_option(self, option):
        with Session(sql_engine) as session:
            option_premium = OptionPremium(
                option_id=option.id, premium=option.premium, date=option.execution_date)
            session.add(option_premium)
            session.commit()
            session.refresh(option_premium)

    def change_initial_option_premium_by_option(self, option):
        with Session(sql_engine) as session:
            statement = select(OptionPremium).where(
                OptionPremium.option_id == option.id)
            option_premium = session.exec(statement).first()
            option_premium.premium = option.premium
            option_premium.date = option.execution_date
            session.add(option_premium)
            session.commit()
            session.refresh(option_premium)

    def get_option_premiums_by_option(self, option):
        with Session(sql_engine) as session:
            statement = select(OptionPremium).where(
                OptionPremium.option_id == option.id)
            return session.exec(statement).all()

    def delete_option_premium_by_id(self, option_id):
        with Session(sql_engine) as session:
            statement = select(OptionPremium).where(
                OptionPremium.option_id == option_id)
            premiums = session.exec(statement).all()
            for premium in premiums:
                session.delete(premium)
            session.commit()


def get_option_premium_from_yf(option):
    ticker = yf.Ticker(option.underlying_ticker)
    if option.option_type.is_call:
        option_chain_index = 0
    else:
        option_chain_index = 1
    option_chain = ticker.option_chain(str(option.expiration_date))[
        option_chain_index]

    data = option_chain[option_chain["contractSymbol"] == option.ticker]

    if data.empty:
        return None

    premium = data["lastPrice"]
    last_trade_date = data["lastTradeDate"].values[0]
    last_trade_date = pd.Timestamp(last_trade_date)
    last_trade_date = pd.to_datetime(last_trade_date).date()

    return OptionPremium(option_id=option.id, premium=premium, date=last_trade_date)
