# Generated by Django 4.2.13 on 2024-06-29 17:20

from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('thumbnail', image_cropping.fields.ImageCropField(upload_to='thumbnails/')),
                ('cropping', image_cropping.fields.ImageRatioField('thumbnail', '300x300', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping')),
            ],
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('blog_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.blogpost')),
            ],
        ),
    ]
