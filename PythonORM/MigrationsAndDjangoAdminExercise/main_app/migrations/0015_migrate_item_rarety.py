from django.db import migrations


def set_rarity(apps, schema_editor):
    ItemModel = apps.get_model('main_app', 'Item')
    for i in ItemModel.objects.all():
        if i.price <= 10:
            i.rarity = 'Rare'
        elif i.price <= 20:
            i.rarity = 'Very Rare'
        elif i.price <= 30:
              i.rarity = 'Extremely Rare'
        else:
            i.rarity = 'Mega Rare'
        i.save()

def reverse_set_rarity(apps, schema_editor):
    ItemModel = apps.get_model('main_app', 'Item')
    for i in ItemModel.objects.all():
        i.rarity = ItemModel._meta.get_field('rarity').default
        i.save()

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_migrate_person_age_group'),
    ]

    operations = [
        migrations.RunPython(set_rarity, reverse_set_rarity),
    ]