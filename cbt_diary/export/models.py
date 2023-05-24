import datetime

from pydantic import BaseModel


class EmotionRequest(BaseModel):
    messages: list[str]


class EmotionResponse(BaseModel):
    positive: float
    negative: float
    neutral: float
    skip: float
    speech: float


class DateInterval(BaseModel):
    start_date: datetime.datetime
    end_date: datetime.datetime
