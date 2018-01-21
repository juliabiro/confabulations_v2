# Generated by Django 2.0.1 on 2018-01-21 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('confabulation', '0007_auto_20170425_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysispoint',
            name='analysis_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='confabulation.AnalysisType'),
        ),
        migrations.AlterField(
            model_name='chain',
            name='connection_range',
            field=models.CharField(choices=[('Interconnection', 'interconnection'), ('Intraconnection', 'intraconnection')], max_length=30),
        ),
        migrations.AlterField(
            model_name='participant',
            name='gender',
            field=models.CharField(choices=[('female', 'female'), ('male', 'male'), ('other', 'other')], max_length=20),
        ),
        migrations.AlterField(
            model_name='participant',
            name='participation_group',
            field=models.CharField(choices=[('non-photgrapher', 'non_photographer'), ('photographer', 'photographer'), ('student', 'student')], max_length=50),
        ),
        migrations.AlterField(
            model_name='recording',
            name='participant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='confabulation.Participant'),
        ),
        migrations.AlterField(
            model_name='story',
            name='participant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='confabulation.Participant'),
        ),
        migrations.AlterField(
            model_name='storyintheme',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='confabulation.Story'),
        ),
        migrations.AlterField(
            model_name='storyintheme',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='confabulation.Theme'),
        ),
        migrations.AlterField(
            model_name='storytostoryconnection',
            name='connection_range',
            field=models.CharField(choices=[('Interconnection', 'interconnection'), ('Intraconnection', 'intraconnection')], max_length=30),
        ),
        migrations.AlterField(
            model_name='storytostoryconnection',
            name='story1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='story1', to='confabulation.Story'),
        ),
        migrations.AlterField(
            model_name='storytostoryconnection',
            name='story2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='story2', to='confabulation.Story'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='connection_range',
            field=models.CharField(choices=[('Interconnection', 'interconnection'), ('Intraconnection', 'intraconnection')], max_length=30),
        ),
        migrations.AlterField(
            model_name='themeinchain',
            name='chain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='confabulation.Chain'),
        ),
        migrations.AlterField(
            model_name='themeinchain',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='confabulation.Theme'),
        ),
        migrations.AlterField(
            model_name='transscription',
            name='recording',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='confabulation.Recording'),
        ),
        migrations.AlterField(
            model_name='transscription',
            name='story',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='confabulation.Story'),
        ),
    ]
