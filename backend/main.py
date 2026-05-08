from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from db.database import engine, Base  # ADD THIS

load_dotenv()

app = FastAPI(title="SOC Copilot Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://*.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")          # ADD THIS
def startup():
    Base.metadata.create_all(bind=engine)
    print("✅ Database connected successfully!")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "SOC Copilot Backend is running!"}

@app.get("/")
def root():
    return {"message": "SOC Copilot Backend - Security Operations Center Assistant"}