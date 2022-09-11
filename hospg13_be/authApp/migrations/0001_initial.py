# Generated by Django 4.1 on 2022-09-11 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('perfil', models.CharField(max_length=30, verbose_name='Password')),
                ('nombre', models.CharField(max_length=35, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=35, verbose_name='Apellidos')),
                ('telefono', models.CharField(max_length=35, verbose_name='Telefono')),
                ('genero', models.CharField(max_length=35, verbose_name='Genero')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_Paciente', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=45, verbose_name='Direccion')),
                ('ciudad', models.CharField(max_length=35, verbose_name='Ciuad')),
                ('fechaNacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SignosVitales',
            fields=[
                ('id_signos', models.AutoField(primary_key=True, serialize=False)),
                ('oximetria', models.IntegerField(default=0)),
                ('respiracion', models.IntegerField(default=0)),
                ('frecuencia', models.IntegerField(default=0)),
                ('temperatura', models.IntegerField(default=0)),
                ('glicemia', models.IntegerField(default=0)),
                ('presion', models.CharField(max_length=35, verbose_name='PresionArterial')),
                ('fechasignos', models.DateTimeField()),
                ('idpaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signos', to='authApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Personal_salud',
            fields=[
                ('id_Personal_salud', models.AutoField(primary_key=True, serialize=False)),
                ('rol', models.CharField(max_length=35, verbose_name='Rol')),
                ('especialidad', models.CharField(max_length=35, verbose_name='Especialidad')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Psalud', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='persalud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='authApp.personal_salud'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.CreateModel(
            name='Historia_Clinica',
            fields=[
                ('id_historia', models.AutoField(primary_key=True, serialize=False)),
                ('sugerenciacuidado', models.CharField(max_length=70, verbose_name='SugerenciaCuidado')),
                ('fechasugerencia', models.DateTimeField()),
                ('diagnostico', models.CharField(max_length=70, verbose_name='Diagnostico')),
                ('entorno', models.CharField(max_length=35, verbose_name='Entorno')),
                ('descripcion', models.CharField(max_length=70, verbose_name='Descripcion')),
                ('idpaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HistClinica', to='authApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id_Familiar', models.AutoField(primary_key=True, serialize=False)),
                ('parentesco', models.CharField(max_length=35, verbose_name='Parentesco')),
                ('correo', models.CharField(max_length=35, verbose_name='Correo')),
                ('idpaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familiar', to='authApp.paciente')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familiar', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]