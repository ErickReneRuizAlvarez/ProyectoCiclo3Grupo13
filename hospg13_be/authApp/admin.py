from django.contrib import admin
from .models.usuario import User
from .models.Psalud import Personal_salud
from .models.paciente import Paciente
from .models.HistClinica import Historia_Clinica
from .models.familiar import Familiar
from .models.signos import SignosVitales

admin.site.register(User)
admin.site.register(Personal_salud)
admin.site.register(Paciente)
admin.site.register(Historia_Clinica)
admin.site.register(Familiar)
admin.site.register(SignosVitales)
