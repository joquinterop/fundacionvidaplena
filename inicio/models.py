from django.db import models # type: ignore

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=20)
    email = models.EmailField()
    tipo_usuario = models.CharField(max_length=50, choices=[('Personal', 'Personal'), ('Aportador', 'Aportador')])

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Personal(Usuario):
    telefono = models.CharField(max_length=20)
    sede = models.ForeignKey('Sede', on_delete=models.CASCADE)
    tipo_personal = models.ForeignKey('TipoPersonal', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Personal"

    class Meta:
        verbose_name_plural = "Personales"

class Aportador(Usuario):
    numero_cel = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Aportador"

    class Meta:
        verbose_name_plural = "Aportadores"

class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class TipoPersonal(models.Model):
    nombre_tipo_personal = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_tipo_personal

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_rol

class UsuarioRol(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'rol')

class AporteHistorico(models.Model):
    id_aporte = models.AutoField(primary_key=True)
    id_aportador = models.ForeignKey(Aportador, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()

class MandatoAporte(models.Model):
    id_mandato_aporte = models.AutoField(primary_key=True)
    aportador = models.ForeignKey(Aportador, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    num_tarjeta = models.CharField(max_length=50)
    fecha_inicio = models.DateField()

class Fundacion(models.Model):
    id_fundacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion_principal = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Aporte(models.Model):
    id_aporte = models.AutoField(primary_key=True)
    mandato = models.ForeignKey(MandatoAporte, on_delete=models.CASCADE)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

class Residente(models.Model):
    id_residente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=20)
    fecha_nac = models.DateField()
    direccion = models.CharField(max_length=200)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Familiar(models.Model):
    id_familiar = models.AutoField(primary_key=True)
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE)
    nombre_familiar = models.CharField(max_length=100)
    apellido_familiar = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    parentesco = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre_familiar} {self.apellido_familiar}"

class FichaMedica(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f"Ficha Medica de {self.residente.nombre} {self.residente.apellido}"

class AccionMedica(models.Model):
    id_accion = models.AutoField(primary_key=True)
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f"Accion Medica: {self.descripcion[:50]}..."

class DetalleMedicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    medicamento = models.ForeignKey('Medicamento', on_delete=models.CASCADE)
    dosis = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=100)

    def __str__(self):
        return f"Medicamento: {self.medicamento.nombre} - Dosis: {self.dosis}"

class Medicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class CompraInsumos(models.Model):
    id_compra = models.AutoField(primary_key=True)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"Compra de Insumos en {self.sede.nombre} - Fecha: {self.fecha}"

class Insumos(models.Model):
    id_insumo = models.AutoField(primary_key=True)
    nombre_insumo = models.CharField(max_length=100)
    descripcion = models.TextField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre_insumo
