from django.db import migrations
from researchdata import models


def insert_data(apps, schema_editor):
    """ Inserts default data """

    # Soil
    for name in ['sandy', 'clay', 'loam', 'silt', 'rocky']:
        models.Soil.objects.create(name=name)

    # Spacing
    for order, name in enumerate(['5', '10', '15']):
        models.Spacing.objects.create(name=name, order=order)

    # VisibilityPercentage
    for order, name in enumerate([
        '0%', '5%', '10%', '15%', '20%', '25%', '30%', '35%', '40%', '45%',
        '50%', '55%', '60%', '65%', '70%', '75%', '80%', '85%', '90%', '95%', '100%'
    ]):
        models.VisibilityPercentage.objects.create(name=name, order=order)

    # LandUse
    for name in ['cultivated', 'uncultivated']:
        models.LandUse.objects.create(name=name)

    # LandUseCultivation
    for name in [
        'grain/cereals',
        'fruits',
        'vegetables',
        'olive',
        'vine'
    ]:
        models.LandUseCultivation.objects.create(name=name)

    # LandUseUncultivated
    for name in [
        'fallow land',
        'wetland/marsh',
        'scrubland/maquis/garrigue',
        'forest/woodland',
        'natural pasture/grazing land',
        'rocky/barren ground',
        'abandoned agricultural land',
    ]:
        models.LandUseUncultivated.objects.create(name=name)

    # FeatureType
    for name in [
        'wall',
        'terrace',
        'pit',
        'quarry',
        'rock cut feature',
        'well',
        'structure',
        'artefact scatter',
        'basin',
        'burial',
        'cistern',
        'structural complex',
        'inscription',
        'agricultural installation',
        'road',
    ]:
        models.FeatureType.objects.create(name=name)

    # FeatureCondition
    for name in ['good', 'moderate', 'poor', 'ruined']:
        models.FeatureCondition.objects.create(name=name)

    # MaterialType
    for name in ['pottery', 'tile', 'lithic', 'other']:
        models.MaterialType.objects.create(name=name)

    # GridSize
    for order, name in enumerate(['5m x 5m', '10m x 10m', '20m x 20m', '40m x 40m']):
        models.GridSize.objects.create(name=name, order=order)

    # BulkMaterialSourceType
    for name in ['survey unit', 'feature', 'grid square']:
        models.BulkMaterialSourceType.objects.create(name=name)

    # FlaggedItemStatus
    for name in ['pending study', 'under study', 'completed', 'returned']:
        models.FlaggedItemStatus.objects.create(name=name)

    # Fabric
    for name in ['coarse', 'cooking', 'semi-coarse', 'fine']:
        models.Fabric.objects.create(name=name)

    # PotteryManufactureTechnique
    for name in ['hand-made', 'wheel-made', 'mould-made']:
        models.PotteryManufactureTechnique.objects.create(name=name)

    # ChronologicalCertainty
    for name in ['low', 'medium', 'high']:
        models.ChronologicalCertainty.objects.create(name=name)

    # TileType
    for name in ['lakonian', 'corinthian']:
        models.TileType.objects.create(name=name)


class Migration(migrations.Migration):

    dependencies = [('researchdata', '0001_initial'),]
    operations = [migrations.RunPython(insert_data),]
