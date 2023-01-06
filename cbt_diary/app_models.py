from pydantic import BaseModel


class Emotion(BaseModel):
    id: int
    name: str


class CognitiveDistortion(BaseModel):
    id: int
    name: str
    description: str


class RecordTemplate(BaseModel):
    trigger_event: str | None
    automated_thought: str | None
    trust_level: int | None
    body_sens: str | None
    behaviour: str | None
    rational_answer: str | None
    conclusion: str | None
    date_time: str | None


class Record(RecordTemplate):
    id: int
    user_id: int


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    is_admin: bool


class EmotionRecord(BaseModel):
    emotion_id: int
    record_id: int
    intensity: int


class DistortionRecord(BaseModel):
    distortion_id: int
    record_id: int
