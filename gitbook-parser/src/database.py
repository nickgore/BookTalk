import os
from datetime import datetime

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
    Index
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from pgvector.sqlalchemy import Vector


Base = declarative_base()

POSTGRES_DB = os.environ.get("POSTGRES_DB")
if POSTGRES_DB is None:
    raise ValueError("no POSTGRES_DB env var")

POSTGRES_USER = os.environ.get("POSTGRES_USER")
if POSTGRES_USER is None:
    raise ValueError("no POSTGRES_USER env var")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
if POSTGRES_PASSWORD is None:
    raise ValueError("no POSTGRES_PASSWORD env var")
    
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", "5432")


CONN_STRING = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
SCHEMA = 'public'


def get_db_session() -> Session:
    """
    Initializes a session for interacting with the database.

    Returns:
        Returns a database session object that can be used to interact with the database.
    """
    session = sessionmaker(bind=create_engine(CONN_STRING))
    return session()


class Document(Base):
    """Document table for storing GitBook documentation metadata."""
    
    __tablename__ = 'documents'
    __table_args__ = {'schema': SCHEMA}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    url = Column(Text, nullable=False)
    content = Column(Text, nullable=True)
    processed_at = Column(DateTime, nullable=datetime.now)
    created_at = Column(DateTime, default=datetime.now)
    
    # Relationship to chunks
    chunks = relationship("DocumentChunk", back_populates="document", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Document(id={self.id}, title='{self.title}', url='{self.url}')>"

class DocumentChunk(Base):
    """Document chunks table for storing text chunks with embeddings."""
    
    __tablename__ = 'document_chunks'
    __table_args__ = (
        Index('idx_document_chunks_document_id', 'document_id'),
        Index('idx_document_chunks_embedding', 'embedding', postgresql_using='ivfflat', 
              postgresql_ops={'embedding': 'vector_cosine_ops'}),
        {'schema': SCHEMA}
    )
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    document_id = Column(Integer, ForeignKey(f'{SCHEMA}.documents.id', ondelete='CASCADE'), nullable=False)
    chunk_text = Column(Text, nullable=False)
    chunk_index = Column(Integer, nullable=False)
    embedding = Column(Vector(384))  # 384 dimensions (all-MiniLM-L6-v2)
    created_at = Column(DateTime, default=datetime.now)
    
    # Relationship to document
    document = relationship("Document", back_populates="chunks")
    
    def __repr__(self):
        return f"<DocumentChunk(id={self.id}, document_id={self.document_id}, chunk_index={self.chunk_index})>"
