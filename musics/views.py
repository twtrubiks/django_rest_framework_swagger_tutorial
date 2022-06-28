from musics.models import Musics
from musics.serializers import MusicSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Musics.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (IsAuthenticated,)
