from wtforms import Form, StringField


class JobListingForm(Form):
    posting = StringField('posting')
    exclude = StringField('exclude')
