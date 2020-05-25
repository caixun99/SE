# Generated by Django 3.0.3 on 2020-05-24 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('points', models.IntegerField(default=0)),
                ('department', models.CharField(blank=True, default='', max_length=50)),
                ('grade', models.CharField(blank=True, default='', max_length=50)),
                ('contact', models.CharField(blank=True, default='', max_length=50)),
                ('communities', models.ManyToManyField(blank=True, related_name='users', to='market.Community')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='goods')),
                ('name', models.CharField(default='null', max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('publish_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('sold_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buy', to='market.USER')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='market.Category')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sell', to='market.USER')),
            ],
        ),
        migrations.CreateModel(
            name='Dynamic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('publish_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='uploads')),
                ('kind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kinds', to='market.Category')),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publish_dynamic', to='market.USER')),
            ],
        ),
        migrations.CreateModel(
            name='Comment_To_Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('publish_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('belong', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='market.Product')),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publish_goods_comment', to='market.USER')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('publish_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('Dynamic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='market.Dynamic')),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publish_dynamic_comment', to='market.USER')),
            ],
            options={
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('publish_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('belong', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat', to='market.Community')),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publish_chat', to='market.USER')),
            ],
        ),
    ]
