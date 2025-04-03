import uuid

from sqlalchemy import Table, MetaData, Column, String, DateTime, Text, UUID, Boolean
from sqlalchemy.sql import func


metadata = MetaData()

ouvidoria = Table(
    'ouvidoria',
    metadata,
    Column('uuid', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column('canal', String, nullable=False),
    Column('cpf', String, nullable=False, index=True),
    Column('atendimento', String, nullable=False),
    Column('motivo', String, nullable=False),
    Column('titulo', String, nullable=False),
    Column('descricao', Text, nullable=False),
    Column('situacao', Boolean, nullable=False, default=False),
    Column('data', DateTime, default=func.now())
)

ludopatia = Table(
    'ludopatia',
    metadata,
    Column('uuid', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column('email', String, nullable=False, index=True),
    Column('resultado', Text, nullable=False),
    Column('situacao', Boolean, nullable=False, default=False),
    Column('criado', DateTime, default=func.now()),
    Column('atualizado', DateTime, default=func.now(), onupdate=func.now())
)
