from rest_framework import serializers
from musics.models import Musics


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musics
        # fields = '__all__'
        fields = ('id', 'song', 'singer', 'last_modify_date', 'created')
