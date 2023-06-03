from rest_framework import serializers
from .models import *

class user_serializers(serializers.ModelSerializer):
  class Meta:
    model= student
    fields = "__all__"