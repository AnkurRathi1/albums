import json

from flask import request
from src.utils import bp, db
from flask import make_response, jsonify
from flask.views import MethodView
from .schemas import ImagesSchema, ArtistsSchema, ItemsSchema, AlbumsSchema, TracksSchema
from .models import Images, Artists, Items, Albums, Tracks


class ImagesResourceView(MethodView):

    def get(self):
        try:
            data = request.args
            default_limit = 5
            if 'limit' in data and data['limit']:
                default_limit = data['limit']
            entry = Images.query.limit(default_limit).all()
            json_data = [ImagesSchema().dump(en) for en in entry]
            return make_response(jsonify({"data": json_data, "error": False}), 200)
        except Exception as e:
            return make_response(jsonify({'error': True, 'error_messages': str(e)}), 422)

    def post(self):
        data = request.json
        try:
            data = ImagesSchema().load(data, many=False, session=db)
            try:
                db.session.add(data)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return make_response(jsonify(e), 422)
            return make_response(jsonify({'error': False, 'data': json.loads(ImagesSchema().dumps(data)),
                                          'message': 'Items added successfully'}), 200)
        except Exception as e:
            return make_response(jsonify({'error': True, 'error_messages': str(e)}), 422)

    def patch(self):
        slug = request.args
        if 'id' in slug and slug['id']:
            obj = Images.query.get(slug['id'])
            if obj:
                try:
                    obj = ImagesSchema().load(request.json, instance=obj, partial=True, session=db)
                    if obj:
                        obj = json.loads(ImagesSchema().dumps(obj))
                        exist_record = Images.query.filter(Images.id == slug['id'])
                        exist_record.update(obj)
                        db.session.commit()
                        return make_response(jsonify({'error': False, 'message': 'Resource Updated successfully'}), 200)
                    else:
                        return make_response(jsonify({'error': True, 'message': 'Resource not found'}), 404)
                except Exception as e:
                    db.session.rollback()
                    return make_response(jsonify(e), 422)
            else:
                return make_response(jsonify({'error': True, 'message': 'Resource not found'}), 404)

        else:
            return make_response(jsonify({'error': True, 'message': 'Slug is missing for the request'}), 400)

    def delete(self):
        slug = request.args
        if 'id' in slug and slug['id']:
            obj = Images.query.get(slug['id'])
            if obj:
                try:
                    db.session.delete(obj)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    return make_response(jsonify(e), 422)
                return make_response(jsonify({'error': False, 'message': 'Resource deleted successfully'}), 200)
            else:
                return make_response(jsonify({'error': True, 'message': 'Resource not found'}), 404)
        else:
            return make_response(jsonify({'error': True, 'message': 'Slug is missing for the request'}), 400)


bp.add_url_rule('/images_resource_view', view_func=ImagesResourceView.as_view('images_resource_view'))


class ArtistsResourceView(MethodView):

    def get(self):
        try:
            data = request.args
            default_limit = 5
            if 'limit' in data and data['limit']:
                default_limit = data['limit']
            entry = Artists.query.limit(default_limit).all()
            json_data = [ArtistsSchema().dump(en) for en in entry]
            return make_response(jsonify({"data": json_data, "error": False}), 200)
        except Exception as e:
            return make_response(jsonify({'error': True, 'error_messages': str(e)}), 422)

    def post(self):
        data = request.json
        try:
            data = ArtistsSchema().load(data, many=False, session=db)
            try:
                db.session.add(data)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return make_response(jsonify(e), 422)
            return make_response(jsonify({'error': False, 'data': json.loads(ArtistsSchema().dumps(data)),
                                          'message': 'Items added successfully'}), 200)
        except Exception as e:
            return make_response(jsonify({'error': True, 'error_messages': str(e)}), 422)

    def patch(self):
        slug = request.args
        if 'id' in slug and slug['id']:
            obj = Artists.query.get(slug['id'])
            if obj:
                try:
                    obj = ArtistsSchema().load(request.json, instance=obj, partial=True, session=db)
                    if obj:
                        obj = json.loads(ArtistsSchema().dumps(obj))
                        exist_record = Artists.query.filter(Artists.id == slug['id'])
                        exist_record.update(obj)
                        db.session.commit()
                        return make_response(jsonify({'error': False, 'message': 'Resource Updated successfully'}), 200)
                    else:
                        return make_response(jsonify({'error': True, 'message': 'Resource not found'}), 404)
                except Exception as e:
                    print(e)
                    db.session.rollback()
                    return make_response(jsonify({'errors': str(e)}), 422)
            else:
                return make_response(jsonify({'error': True, 'message': 'Resource not found'}), 404)

        else:
            return make_response(jsonify({'error': True, 'message': 'Slug is missing for the request'}), 400)

    def delete(self):
        slug = request.args
        if 'id' in slug and slug['id']:
            obj = Artists.query.get(slug['id'])
            if obj:
                try:
                    db.session.delete(obj)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    return make_response(jsonify(e), 422)
                return make_response(jsonify({'error': False, 'message': 'Resource deleted successfully'}), 200)
            else:
                return make_response(jsonify({'error': True, 'message': 'Resource not found'}), 404)
        else:
            return make_response(jsonify({'error': True, 'message': 'Slug is missing for the request'}), 400)


bp.add_url_rule('/artists_resource_view', view_func=ArtistsResourceView.as_view('artists_resource_view'))


class ItemsResourceView(MethodView):

    def get(self):
        try:
            data = request.args
            default_limit = 5
            if 'limit' in data and data['limit']:
                default_limit = data['limit']
            entry = Items.query.limit(default_limit).all()
            json_data = [ItemsSchema().dump(en) for en in entry]
            return make_response(jsonify({"data": json_data, "error": False}), 200)
        except Exception as e:
            return make_response(jsonify({'error': True, 'error_messages': str(e)}), 422)

    def post(self):
        data = request.json
        try:
            data = ItemsSchema().load(data, many=False, session=db)
            try:
                db.session.add(data)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return make_response(jsonify(e), 422)
            return make_response(jsonify({'error': False, 'data': json.loads(ItemsSchema().dumps(data)),
                                          'message': 'Items added successfully'}), 200)
        except Exception as e:
            return make_response(jsonify({'error': True, 'error_messages': str(e)}), 422)

    def patch(self):
        slug = request.args
        if 'id' in slug and slug['id']:
            obj = Items.query.get(slug['id'])
            if obj:
                try:
                    obj = ItemsSchema().load(request.json, instance=obj, partial=True, session=db)
                    if obj:
                        obj = json.loads(ItemsSchema().dumps(obj))
                        exist_record = Items.query.filter(Items.id == slug['id'])
                        exist_record.update(obj)
                        db.session.commit()
                        return make_response(jsonify({'error': False, 'message': 'Resource Updated successfully'}), 200)
                    else:
                        return make_response(jsonify({'error': True, 'message': 'Resource not found'}), 404)
                except Exception as e:
                    print(e)
                    db.session.rollback()
                    return make_response(jsonify({'errors': str(e)}), 422)
            else:
                return make_response(jsonify({'error': True, 'message': 'Resource not found'}), 404)

        else:
            return make_response(jsonify({'error': True, 'message': 'Slug is missing for the request'}), 400)

    def delete(self):
        slug = request.args
        if 'id' in slug and slug['id']:
            obj = Items.query.get(slug['id'])
            if obj:
                try:
                    db.session.delete(obj)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    return make_response(jsonify(e), 422)
                return make_response(jsonify({'error': False, 'message': 'Resource deleted successfully'}), 200)
            else:
                return make_response(jsonify({'error': True, 'message': 'Resource not found'}), 404)
        else:
            return make_response(jsonify({'error': True, 'message': 'Slug is missing for the request'}), 400)


bp.add_url_rule('/items_resource_view', view_func=ItemsResourceView.as_view('items_resource_view'))


class TracksResourceView(MethodView):

    def get(self):
        try:
            data = request.args
            default_limit = 5
            if 'limit' in data and data['limit']:
                default_limit = data['limit']
            entry = Tracks.query.limit(default_limit).all()
            json_data = [TracksSchema().dump(en) for en in entry]
            return make_response(jsonify({"data": json_data, "error": False}), 200)
        except Exception as e:
            return make_response(jsonify({'error': True, 'error_messages': str(e)}), 422)

    def post(self):
        data = request.json
        try:
            data = TracksSchema().load(data, many=False, session=db)
            try:
                db.session.add(data)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return make_response(jsonify(e), 422)
            return make_response(jsonify({'error': False, 'data': json.loads(TracksSchema().dumps(data)),
                                          'message': 'Items added successfully'}), 200)
        except Exception as e:
            return make_response(jsonify({'error': True, 'error_messages': str(e)}), 422)

    def patch(self):
        slug = request.args
        if 'id' in slug and slug['id']:
            obj = Tracks.query.get(slug['id'])
            if obj:
                try:
                    obj = TracksSchema().load(request.json, instance=obj, partial=True, session=db)
                    if obj:
                        obj = json.loads(TracksSchema().dumps(obj))
                        exist_record = Tracks.query.filter(Tracks.id == slug['id'])
                        exist_record.update(obj)
                        db.session.commit()
                        return make_response(jsonify({'error': False, 'message': 'Resource Updated successfully'}), 200)
                    else:
                        return make_response(jsonify({'error': True, 'message': 'Resource not found'}), 404)
                except Exception as e:
                    print(e)
                    db.session.rollback()
                    return make_response(jsonify({'errors': str(e)}), 422)
            else:
                return make_response(jsonify({'error': True, 'message': 'Resource not found'}), 404)

        else:
            return make_response(jsonify({'error': True, 'message': 'Slug is missing for the request'}), 400)

    def delete(self):
        slug = request.args
        if 'id' in slug and slug['id']:
            obj = Tracks.query.get(slug['id'])
            if obj:
                try:
                    db.session.delete(obj)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    return make_response(jsonify(e), 422)
                return make_response(jsonify({'error': False, 'message': 'Resource deleted successfully'}), 200)
            else:
                return make_response(jsonify({'error': True, 'message': 'Resource not found'}), 404)
        else:
            return make_response(jsonify({'error': True, 'message': 'Slug is missing for the request'}), 400)


bp.add_url_rule('/tracks_resource_view', view_func=TracksResourceView.as_view('tracks_resource_view'))


class AlbumsResourceView(MethodView):

    def get(self):
        try:
            data = request.args
            default_limit = 5
            if 'limit' in data and data['limit']:
                default_limit = data['limit']
            entry = Albums.query.limit(default_limit).all()
            json_data = [AlbumsSchema().dump(en) for en in entry]
            return make_response(jsonify({"data": json_data, "error": False}), 200)
        except Exception as e:
            return make_response(jsonify({'error': True, 'error_messages': str(e)})), 422

    def post(self):
        data = request.json
        try:
            data = AlbumsSchema().load(data, many=False, session=db)
            try:
                db.session.add(data)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return make_response(jsonify(e), 422)
            return make_response(jsonify({'error': False, 'data': json.loads(AlbumsSchema().dumps(data)),
                                          'message': 'Items added successfully'}), 200)
        except Exception as e:
            return make_response(jsonify({'error': True, 'error_messages': str(e)}), 422)

    def patch(self):
        slug = request.args
        if 'id' in slug and slug['id']:
            obj = Albums.query.get(slug['id'])
            if obj:
                try:
                    obj = AlbumsSchema().load(request.json, instance=obj, partial=True, session=db)
                    if obj:
                        obj = json.loads(AlbumsSchema().dumps(obj))
                        exist_record = Albums.query.filter(Albums.id == slug['id'])
                        exist_record.update(obj)
                        db.session.commit()
                        return make_response(jsonify({'error': False, 'message': 'Resource Updated successfully'}), 200)
                    else:
                        return make_response(jsonify({'error': True, 'message': 'Resource not found'}), 404)
                except Exception as e:
                    print(e)
                    db.session.rollback()
                    return make_response(jsonify({'errors': str(e)}), 422)
            else:
                return make_response(jsonify({'error': True, 'message': 'Resource not found'}), 404)

        else:
            return make_response(jsonify({'error': True, 'message': 'Slug is missing for the request'}), 400)

    def delete(self):
        slug = request.args
        if 'id' in slug and slug['id']:
            obj = Albums.query.get(slug['id'])
            if obj:
                try:
                    db.session.delete(obj)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    return make_response(jsonify(e), 422)
                return make_response(jsonify({'error': False, 'message': 'Resource deleted successfully'}), 200)
            else:
                return make_response(jsonify({'error': True, 'message': 'Resource not found'}), 404)
        else:
            return make_response(jsonify({'error': True, 'message': 'Slug is missing for the request'}), 400)


bp.add_url_rule('/albums_resource_view', view_func=AlbumsResourceView.as_view('albums_resource_view'))
