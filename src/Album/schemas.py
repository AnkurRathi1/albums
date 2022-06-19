from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from .models import Images, Artists, Items, Tracks, Albums


class ImagesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Images
        include_relationships = True
        load_instance = True
    url = auto_field(allow_none=True)
    width = auto_field(allow_none=True)
    height = auto_field(allow_none=True)


class ArtistsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Artists
        include_relationships = True
        load_instance = True
    name = auto_field(allow_none=False)
    href = auto_field(allow_none=False)
    type = auto_field(allow_none=False)
    url = auto_field(allow_none=True)
    img_id = auto_field(allow_none=True)
    images = auto_field(allow_none=True, uselist=True)
    popularity = auto_field(allow_none=True)


class ItemsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Items
        include_relationships = True
        load_instance = True
    name = auto_field(allow_none=False)
    href = auto_field(allow_none=False)


class TracksSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Tracks
        include_relationships = True
        load_instance = True
    limit = auto_field(allow_none=False)
    offset = auto_field(allow_none=False)
    total = auto_field(allow_none=False)
    previous = auto_field(allow_none=True)
    next = auto_field(allow_none=True)
    href = auto_field(allow_none=True)
    width = auto_field(allow_none=True)
    height = auto_field(allow_none=True)


class AlbumsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Albums
        include_relationships = True
        load_instance = True
    album_type = auto_field(allow_none=False)
    name = auto_field(allow_none=False)
    release_date = auto_field(allow_none=False)
    url = auto_field(allow_none=True)
    type = auto_field(allow_none=True)
    href = auto_field(allow_none=True)
    available_markets = auto_field(allow_none=True)
    img_id = auto_field(allow_none=True)
    artist_id = auto_field(allow_none=True)
    track_id = auto_field(allow_none=True)
