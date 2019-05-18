# Generated by Django 2.1.7 on 2019-04-04 12:09

from django.db import migrations
from django.utils import translation


def populate_new_systematics(apps, schema_editor):
    translation.activate('de')

    TreeNode = apps.get_model("stein", "TreeNode")
    MineralType = apps.get_model("stein", "MineralType")

    MINERAL_CATEGORIES = dict(MineralType._meta.get_field("systematics").choices)
    SPLIT_CHOICES = dict(MineralType._meta.get_field("split_systematics").choices)
    SUB_CHOICES = dict(MineralType._meta.get_field("sub_systematics").choices)

    for mineral in MineralType.objects.all():
        if mineral.sub_systematics:

            mineral.new_systematics = TreeNode.objects.get(node_name=translation.gettext(SUB_CHOICES.get(mineral.sub_systematics)))
        elif mineral.split_systematics:
            mineral.new_systematics = TreeNode.objects.get(node_name=translation.gettext(SPLIT_CHOICES.get(mineral.split_systematics)))
        else:
            mineral.new_systematics = TreeNode.objects.get(node_name=translation.gettext(MINERAL_CATEGORIES.get(mineral.systematics)))
        mineral.save()


def revert(apps, schema_editor):
    translation.activate('de')

    TreeNode = apps.get_model("stein", "TreeNode")
    MineralType = apps.get_model("stein", "MineralType")

    for node in TreeNode.objects.all():

        node.mineraltypes.clear()


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0063_create_intermediate_new_systematics'),
    ]

    operations = [
        migrations.RunPython(populate_new_systematics, revert),
    ]
