# Generated by Django 3.1.4 on 2021-01-12 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_name', models.CharField(max_length=100)),
                ('book_serial_id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_description', models.CharField(blank=True, max_length=1000, null=True)),
                ('book_image', models.ImageField(upload_to='media/')),
                ('book_pdf', models.FileField(upload_to='media/')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('review_stars_count', models.IntegerField(default=0)),
                ('author', models.CharField(max_length=200)),
                ('publication', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('no_of_pages', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_text', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(max_length=100)),
                ('user_mail', models.EmailField(max_length=200, primary_key=True, serialize=False)),
                ('contact_number', models.IntegerField(default=0, unique=True)),
                ('roll_no', models.CharField(max_length=200)),
                ('user_image', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('transaction_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('transaction_amount', models.FloatField()),
                ('book', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='apis.book')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='apis.user')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_text', models.CharField(max_length=30)),
                ('category_image', models.ImageField(upload_to='media/')),
                ('branch_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.branch')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='book_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apis.category'),
        ),
        migrations.AddField(
            model_name='book',
            name='bought_by',
            field=models.ManyToManyField(blank=True, related_name='bought_by', to='apis.User'),
        ),
        migrations.AddField(
            model_name='book',
            name='sold_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sold_by', to='apis.user'),
        ),
    ]