
from rest_framework import viewsets
from .models import Paciente
from .models import Cita
from .models import Atencion
from .models import Medicamento
from .models import ServicioMedico
from .serializers import PacienteSerializer
from .serializers import CitaSerializer
from .serializers import AtencionSerializer
from .serializers import MedicamentoSerializer
from .serializers import ServicioMedicoSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import MedicoRegisterSerializer
from rest_framework import viewsets, permissions




class ServicioMedicoViewSet(viewsets.ModelViewSet):
    queryset = ServicioMedico.objects.all().order_by('nombre')
    serializer_class = ServicioMedicoSerializer
    permission_classes = [permissions.IsAuthenticated]

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all().order_by('nombre')
    serializer_class = MedicamentoSerializer
    permission_classes = [permissions.IsAuthenticated]


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [permissions.IsAuthenticated]

class MedicoRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = MedicoRegisterSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all().order_by('-fecha_cita')
    serializer_class = CitaSerializer
    permission_classes = [permissions.IsAuthenticated]

class AtencionViewSet(viewsets.ModelViewSet):
    queryset = Atencion.objects.all().order_by('-fecha_atencion')
    serializer_class = AtencionSerializer
    permission_classes = [permissions.IsAuthenticated]