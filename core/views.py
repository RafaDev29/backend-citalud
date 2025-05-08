
from rest_framework import viewsets
from .models import Paciente
from .serializers import PacienteSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import MedicoRegisterSerializer
from rest_framework import viewsets, permissions

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [permissions.IsAuthenticated]

class MedicoRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = MedicoRegisterSerializer