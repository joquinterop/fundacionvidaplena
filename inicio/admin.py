from django.contrib import admin # type: ignore
from .models import Usuario, Personal, Aportador, Sede, TipoPersonal, Rol, UsuarioRol, AporteHistorico, MandatoAporte, Fundacion, Aporte, Residente, Familiar, FichaMedica, AccionMedica, DetalleMedicamento, Medicamento, CompraInsumos, Insumos    

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Personal)
admin.site.register(Aportador)
admin.site.register(Sede)
admin.site.register(TipoPersonal)
admin.site.register(Rol)
admin.site.register(UsuarioRol)
admin.site.register(AporteHistorico)
admin.site.register(MandatoAporte)
admin.site.register(Fundacion)
admin.site.register(Aporte)
admin.site.register(Residente)
admin.site.register(Familiar)
admin.site.register(FichaMedica)
admin.site.register(AccionMedica)
admin.site.register(DetalleMedicamento)
admin.site.register(Medicamento)
admin.site.register(CompraInsumos)
admin.site.register(Insumos)