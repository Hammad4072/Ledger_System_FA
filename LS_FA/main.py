from fastapi import FastAPI
from LS_FA.router import user, transaction, stock, ledger, report
from LS_FA import models
from LS_FA.database import engine
# from dotenv import load_dotenv
import os

# Load environment variables from .env file
# load_dotenv()

# Create all database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Ledger System")

# Include routers
app.include_router(user.router)
app.include_router(transaction.router)
app.include_router(stock.router)
app.include_router(ledger.router)
app.include_router(report.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Ledger System Running"}