from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy import text, UniqueConstraint
from src.utils import db


class BaseModel(object):

    __mapper_args__ = {'always_refresh': True}
    id = db.Column(UUID(as_uuid=True), index=True, primary_key=True, server_default=text("uuid_generate_v4()"))
    created_on = db.Column(db.TIMESTAMP(timezone=True), server_default=text("current_timestamp"), index=True)
    updated_on = db.Column(db.TIMESTAMP(timezone=True), onupdate=db.func.current_timestamp(),
                           server_default=text("current_timestamp"))


class Images(BaseModel, db.Model):
    url = db.Column(db.String(256), nullable=True)
    width = db.Column(db.String(25), nullable=True)
    height = db.Column(db.String(25), nullable=True)


class Artists(BaseModel, db.Model):
    name = db.Column(db.String(256), nullable=False)
    href = db.Column(db.String(25), nullable=False)
    type = db.Column(db.String(25), nullable=False)
    img_id = db.Column(db.ForeignKey('images.id', ondelete='CASCADE'))
    images = db.relationship('Images', uselist=False, foreign_keys=[img_id], backref='artists')
    url = db.Column(db.String(256), nullable=True)
    popularity = db.Column(db.Integer(), default=1, nullable=True)
    UniqueConstraint(name, type)

class Items(BaseModel, db.Model):
    name = db.Column(db.String(256), nullable=True, unique=True)
    href = db.Column(db.String(25), nullable=True)


class Tracks(BaseModel, db.Model):
    limit = db.Column(db.Integer(), default=1, nullable=False)
    offset = db.Column(db.Integer(), default=1, nullable=False)
    total = db.Column(db.Integer(), default=1, nullable=False)
    previous = db.Column(db.String(256), nullable=True)
    href = db.Column(db.String(256), nullable=True)
    next = db.Column(db.String(256), nullable=True)
    width = db.Column(db.String(25), nullable=True)
    height = db.Column(db.String(25), nullable=True)


class Albums(BaseModel, db.Model):
    album_type = db.Column(db.String(25), nullable=True)
    name = db.Column(db.String(256), nullable=True)
    release_date = db.Column(db.TIMESTAMP(timezone=True), nullable=True)
    url = db.Column(db.String(256), nullable=True)
    type = db.Column(db.String(256), nullable=True)
    href = db.Column(db.String(256), nullable=True)
    available_markets = db.Column(JSON(), default=[])
    img_id = db.Column(db.ForeignKey('images.id', ondelete='CASCADE'))
    artist_id = db.Column(db.ForeignKey('artists.id', ondelete='CASCADE'))
    track_id = db.Column(db.ForeignKey('tracks.id', ondelete='CASCADE'))
    UniqueConstraint(album_type, name, type)

