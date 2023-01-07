from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db_manager.utils import get_db
from . import service
from .app_models import RecordTemplate, EmotionRecord, DistortionRecord

router = APIRouter()


@router.get("/")
def start(db: Session = Depends(get_db)):
    print(db)
    pass


@router.post("/add_record")
def post_new_record(user_id: int, record_item: RecordTemplate, db: Session = Depends(get_db)):
    """Добавляет новую запись в бд"""
    record = service.add_records(db, record_item, user_id)
    return record


@router.delete("/delete_record")
def delete_record(user_id: int, record_id: int, db: Session = Depends(get_db)):
    """Добавляет новую запись в бд"""
    res = service.delete_record(db, user_id, record_id)
    return res


@router.post("/add_record/emotion")
def post_emotion_record(record_emotions: list[EmotionRecord], db: Session = Depends(get_db)):
    """Добавляет новую запись в бд"""
    record = service.add_emotion_records(db, record_emotions)
    return record


@router.post("/add_record/distortion")
def post_distortion_record(record_distortions: list[DistortionRecord], db: Session = Depends(get_db)):
    """Добавляет новую запись в бд"""
    record = service.add_distortion_records(db, record_distortions)
    return record


@router.put("/update_record")
def put_to_record(record_id: int, record_item: RecordTemplate, db: Session = Depends(get_db)):
    """Обновляет существующую запись в бд"""
    updated_record = service.update_record_by_id(db, record_id, record_item)
    return updated_record


@router.get("/records/{user_id}")
def get_users_records(user_id: int, db: Session = Depends(get_db)):
    """Вывести все записи для определонного юзера"""
    records = service.get_records(db, user_id)
    return records


@router.get("/records/{user_id}/{record_id}")
def get_users_record_specific(user_id: int, record_id: int, db: Session = Depends(get_db)):
    """Вывести все записи для определонного юзера"""
    record = service.get_specific_record(db, user_id, record_id)
    return record


@router.get("/emotion_record")
def get_emotion_record(record_id: int, db: Session = Depends(get_db)):
    """Вывести все записи для определонного юзера"""
    records = service.get_emotion_record(db, record_id)
    return records


@router.get("/distortion_record")
def get_distortion_record(record_id: int, db: Session = Depends(get_db)):
    """Вывести все записи для определонного юзера"""
    records = service.get_distortion_record(db, record_id)
    return records


@router.get("/emotions")
def get_all_emotions(db: Session = Depends(get_db)):
    """Вывести все записи для определонного юзера"""
    emotions = service.get_emotions(db)
    return emotions


@router.get("/distortions")
def get_all_distortions(db: Session = Depends(get_db)):
    """Вывести все записи для определонного юзера"""
    distortions = service.get_distortions(db)
    return distortions


@router.get("/user_emotion_list")
def get_users_emotions(user_id: int, db: Session = Depends(get_db)):
    """Вывести все записи для определонного юзера"""
    emotions = service.get_users_emotions(user_id, db)
    return emotions


@router.get("/user_distortion_list")
def get_users_distortions(user_id: int, db: Session = Depends(get_db)):
    """Вывести все записи для определонного юзера"""
    emotions = service.get_users_distortions(user_id, db)
    return emotions
