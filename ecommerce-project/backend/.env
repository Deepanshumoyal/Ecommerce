from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from .env (for local development)
load_dotenv()

# Get DATABASE_URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Check if DATABASE_URL exists
if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL environment variable is not set. "
        "Please add it to Railway Variables or your local .env file."
    )

try:
    # Create SQLAlchemy engine
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,  # Checks connection before using it
    )

    # Create session factory
    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )

    # Base class for models
    Base = declarative_base()

    print("✅ Database configuration loaded successfully.")

except Exception as e:
    print(f"❌ Database initialization error: {e}")
    raise


# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print(f"❌ Database session error: {e}")
        raise
    finally:
        db.close()