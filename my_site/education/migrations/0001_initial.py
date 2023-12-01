# Generated by Django 3.2.23 on 2023-12-01 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('instructions', models.TextField()),
                ('max_score', models.IntegerField()),
                ('is_published', models.BooleanField()),
                ('files', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('category', models.CharField(max_length=255)),
                ('is_published', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('order', models.IntegerField()),
                ('instructions', models.TextField()),
                ('materials', models.TextField()),
                ('due_date', models.DateField()),
                ('is_completed', models.BooleanField()),
                ('files', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_date', models.DateTimeField()),
                ('files', models.FileField(upload_to='')),
                ('feedback', models.TextField()),
                ('score', models.IntegerField()),
                ('thisAssignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.assignment')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('duration', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('category', models.CharField(max_length=255)),
                ('is_published', models.BooleanField()),
                ('order', models.IntegerField()),
                ('notes', models.TextField()),
                ('files', models.FileField(upload_to='')),
                ('labs', models.ManyToManyField(to='education.Lab')),
                ('thisCourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.course')),
            ],
        ),
        migrations.AddField(
            model_name='lab',
            name='thisModule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.module'),
        ),
        migrations.AddField(
            model_name='course',
            name='modules',
            field=models.ManyToManyField(to='education.Module'),
        ),
        migrations.AddField(
            model_name='course',
            name='prerequisites',
            field=models.ManyToManyField(related_name='_education_course_prerequisites_+', to='education.Course'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.course'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='submissions',
            field=models.ManyToManyField(to='education.Submission'),
        ),
    ]
