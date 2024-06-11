# Example: 0001_initial.py
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_auto_20210611_1200'), 
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('powers', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
