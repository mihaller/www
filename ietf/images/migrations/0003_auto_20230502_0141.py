# Generated by Django 3.2.18 on 2023-05-02 00:41

from django.db import migrations
import wagtail.images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_alter_ietfimage_file_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ietfimage',
            name='file',
            field=wagtail.images.models.WagtailImageField(height_field='height', upload_to=wagtail.images.models.get_upload_to, verbose_name='file', width_field='width'),
        ),
        migrations.AlterField(
            model_name='ietfrendition',
            name='file',
            field=wagtail.images.models.WagtailImageField(height_field='height', upload_to=wagtail.images.models.get_rendition_upload_to, width_field='width'),
        ),
    ]