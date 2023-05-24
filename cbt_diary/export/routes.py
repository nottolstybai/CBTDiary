import pandas as pd
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from cbt_diary.export.emotion_recognition.dostoevsky_model import sentiment_analysis_model
from cbt_diary.export.models import EmotionRequest, EmotionResponse, DateInterval
from cbt_diary.export.reporter import Reporter
from db_manager.database import engine
from db_manager.utils import get_db

router = APIRouter()


@router.post("/get_emotions")
def post_emotions(text: EmotionRequest) -> list[EmotionResponse]:
    results = sentiment_analysis_model.predict(text.messages, k=5)
    return results


@router.post("/get_report")
async def post_distortion_record(datetime_interval: DateInterval, db: Session = Depends(get_db)):
    """Добавляет новую запись в бд"""
    query = f"""select trigger_event, automated_thought, body_sens, behaviour, rational_answer, conclusion, 
                        e.name emotion, cd.name as cognitive_distortion
                from record
                join emotion_record er on record.id = er.record_id
                join emotion e on e.id = er.emotion_id
                join distortion_record dr on record.id = dr.record_id
                join cognitive_distortion cd on cd.id = dr.distortion_id
                where date_time >= '{datetime_interval.start_date}' and 
                      date_time < '{datetime_interval.end_date}'"""
    automated_thoughts = db.execute(f"""select automated_thought 
                                        from record 
                                        where date_time >= '{datetime_interval.start_date}' and 
                                              date_time < '{datetime_interval.end_date}'""")
    df = pd.read_sql_query(query, engine)
    automated_thoughts = [row[0] for row in automated_thoughts]
    label = [max(x, key=x.get) for x in sentiment_analysis_model.predict(automated_thoughts, k=5)]
    df["model_preidction"] = label

    # report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports', 'report.docx')
    reporter = Reporter()
    reporter.create_artifact(datetime_interval.start_date.date(), datetime_interval.end_date.date(), df)
    return
