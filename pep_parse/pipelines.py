from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base
from itemadapter import ItemAdapter

Base = declarative_base


class Pep(Base):
    __tablename__ = 'pep'
    number = Column(String(10))
    name = Column(String(300))
    status = Column(String(60))


class PepParsePipeline:
    def process_item(self, item, spider):
        return item
