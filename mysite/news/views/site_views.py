from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..serializers import SiteSerializer
from ..models import Site


class SiteCreate(generics.CreateAPIView):
    """
    언론사를 생성한다.
    """

    serializer_class = SiteSerializer
    permission_classes = [IsAuthenticated]


class SiteUpdate(generics.UpdateAPIView):
    """
    언론사를 수정한다.
    """

    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [IsAuthenticated]