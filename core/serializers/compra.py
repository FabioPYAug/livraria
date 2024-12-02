from rest_framework.serializers import CharField, ModelSerializer

from core.models import Compra

class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"
        status = CharField(source="get_status_display", read_only=True)
        usuario = CharField(source="usuario.email", read_only=True)