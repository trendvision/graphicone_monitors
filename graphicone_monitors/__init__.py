from sqlalchemy.orm import Session
import graphicone_models as models

def get_monitors_equity_data(db: Session, ticker: str):

    finance_data = db.query(
        models.IntrinioDump.name,
        models.IntrinioDump.hundred_days_trading_range.label('price'),
        models.IntrinioDump.change,
        models.Equity.tags,
        models.Equity.ticker
    ).join(models.Equity).filter(
        models.Equity.ticker == models.IntrinioDump.ticker
    ).filter(
        models.IntrinioDump.ticker == ticker
    ).first()

    return finance_data._asdict()