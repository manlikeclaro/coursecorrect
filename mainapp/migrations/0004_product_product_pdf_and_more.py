# Generated by Django 4.2.7 on 2023-11-29 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_product_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_pdf',
            field=models.FileField(blank=True, default='pdf/product.pdf', null=True, upload_to='pdf/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale',
            field=models.BooleanField(default=False),
        ),
    ]
