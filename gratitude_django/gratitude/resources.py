from tastypie.resources import ModelResource
from .models import Entry
from tastypie.authorization import Authorization

class EntryResource(ModelResource):
    # author = fields.ToOneField(User, 'author')
    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'
        authorization = Authorization()