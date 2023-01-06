from sqlalchemy import func
from sqlalchemy.orm import Session
from db_manager.database import Base
from . import db_models
from . import app_models


def get_records(db: Session, user_id):
    res = db.query(db_models.Record).filter_by(user_id=user_id).all()
    return res


def get_specific_record(db: Session, user_id, record_id):
    res = db.query(db_models.Record).filter_by(user_id=user_id, id=record_id).one()
    return res


def get_emotion_record(db: Session, record_id: int):
    res = db.query(db_models.EmotionRecord).filter_by(record_id=record_id).all()
    return res


def get_distortion_record(db: Session, record_id: int):
    res = db.query(db_models.DistortionRecord).filter_by(record_id=record_id).all()
    return res


def add_records(db: Session, record_item: app_models.RecordTemplate, user_id):
    record_template_dict = record_item.dict()
    record_template_dict["user_id"] = user_id
    record = db_models.Record(**record_template_dict)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def delete_record(db, user_id: int, record_id: int):
    emotion_del_res = db.query(db_models.DistortionRecord).filter_by(record_id=record_id).delete()
    distortion_del_res = db.query(db_models.EmotionRecord).filter_by(record_id=record_id).delete()
    res = db.query(db_models.Record).filter_by(user_id=user_id, id=record_id).delete()
    db.commit()
    return emotion_del_res, distortion_del_res, res


def add_emotion_records(db: Session, emotion_records: list[app_models.EmotionRecord]):
    status = "Success"
    for emotion_record in emotion_records:
        emotion_record_entity = db_models.EmotionRecord(**emotion_record.dict())
        db.add(emotion_record_entity)
        db.commit()
        db.refresh(emotion_record_entity)
    return status


def add_distortion_records(db: Session, distortion_records: list[app_models.DistortionRecord]):
    status = "Success"
    for distortion_record in distortion_records:
        distortion_record_entity = db_models.DistortionRecord(**distortion_record.dict())
        db.add(distortion_record_entity)
        db.commit()
        db.refresh(distortion_record_entity)
    return status


def update_record_by_id(db: Session, record_id: int, record_item: app_models.RecordTemplate):
    update_record_attrs = record_item.dict()
    update_record_attrs = {key: value for key, value in update_record_attrs.items() if value not in [None, ""]}
    status = "Success"
    try:
        db.query(db_models.Record).filter_by(id=record_id).update(update_record_attrs)
        db.commit()
    except Exception as e:
        status = e
    return status


def get_from_entity_all(db: Session, db_model: Base):
    try:
        res = db.query(db_model).all()
    except Exception as e:
        res = e
    return res


def get_emotions(db: Session):
    res = get_from_entity_all(db, db_models.Emotion)
    return res


def get_distortions(db: Session):
    res = get_from_entity_all(db, db_models.CognitiveDistortion)
    return res
