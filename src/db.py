from sqlalchemy import create_engine
import os

def create_db_engine():
    """
    Initialize a SQLAlchemy engine for a SQLite database.
    This engine acts as the interface between Python/Pandas and the SQL database.
    """
    # The '///' indicates a relative path to the data folder
    engine = create_engine('sqlite:///../data/amazon.db')
    return engine