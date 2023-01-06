from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db_manager.database import Base
from user.db_models import User


class Emotion(Base):
    __tablename__ = "emotion"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)


class CognitiveDistortion(Base):
    __tablename__ = "cognitive_distortion"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    description = Column(String)


class Record(Base):
    __tablename__ = "record"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    trigger_event = Column(String)
    automated_thought = Column(String)
    trust_level = Column(String)
    body_sens = Column(String)
    behaviour = Column(String)
    rational_answer = Column(String)
    conclusion = Column(String)
    date_time = Column(DateTime)
    user_id = Column(Integer, ForeignKey("user.id"))
    user_record_fk = relationship(User)


class DistortionRecord(Base):
    __tablename__ = "distortion_record"
    distortion_id = Column(Integer, ForeignKey("cognitive_distortion.id"), primary_key=True, index=True, unique=True)
    distortion_id_fk = relationship(CognitiveDistortion)
    record_id = Column(Integer, ForeignKey("record.id"), primary_key=True, index=True, unique=True)
    record_id_fk = relationship(Record)


class EmotionRecord(Base):
    __tablename__ = "emotion_record"
    emotion_id = Column(Integer, ForeignKey("emotion.id"), primary_key=True, index=True, unique=True)
    emotion_id_fk = relationship(Emotion)
    record_id = Column(Integer, ForeignKey("record.id"), primary_key=True, index=True, unique=True)
    record_id_fk = relationship(Record)
    intensity = Column(Integer)

