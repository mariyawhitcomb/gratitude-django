from rest_framework import serializers
from .models import Entry

class EntrySerializer(serializers.HyperlinkedModelSerializer):
