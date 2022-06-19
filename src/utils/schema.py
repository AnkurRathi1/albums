from flask_marshmallow import Marshmallow


class FlaskMarshmallowFactory(Marshmallow):

    def __init__(self,  *args, **kwargs):
        super(FlaskMarshmallowFactory, self).__init__(*args, **kwargs)


ma = FlaskMarshmallowFactory()


