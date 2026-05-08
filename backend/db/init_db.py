from db.database import Base, engine
from models.alert import Alert
from models.incident import Incident
from models.action_log import ActionLog

def init_db():
    Base.metadata.create_all(bind=engine)
    print("All tables created successfully!")