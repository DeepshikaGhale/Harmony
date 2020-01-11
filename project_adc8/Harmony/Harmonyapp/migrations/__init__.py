
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True


    operations = [
        migrations.CreateModel(
            name='',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=10)),
                ('SongName', models.CharField(max_length=10)),
                ('Lyric', models.TextField())
            ],
        ),
    ]