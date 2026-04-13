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
    for order, name in enumerate(['pottery', 'tile', 'lithic', 'other']):
        models.MaterialType.objects.create(name=name, order=order)

    # GridSize
    for order, name in enumerate(['5m x 5m', '10m x 10m', '20m x 20m', '40m x 40m']):
        models.GridSize.objects.create(name=name, order=order)

    # BulkMaterialSourceType
    for order, name in enumerate(['not started', 'in progress', 'completed']):
        models.BulkMaterialSourceType.objects.create(name=name, order=order)

    # BulkMaterialProcessingStatus
    for name in ['survey unit', 'feature', 'grid square']:
        models.BulkMaterialProcessingStatus.objects.create(name=name)

    # PotteryMaterial
    for name in ['clay', 'tile', 'other']:
        models.PotteryMaterial.objects.create(name=name)

    # Function
    for name in [
        'transport',
        'storage',
        'easting',
        'drinking',
        'serving',
        'cooking',
        'processing',
        'agricultural',
        'rooking',
        'architectural',
        'ritual',
        'toilet',
        'other household'
    ]:
        models.Function.objects.create(name=name)

    # Part
    for name in [
        'rim',
        'body',
        'base',
        'handle',
        'combined rim/handle',
        'combine rim/handle/body',
        'spout',
        'stem',
        'other'
    ]:
        models.Part.objects.create(name=name)

    # TimePeriod
    for order, name in enumerate([
        'Early Neolithic',
        'Mid Neolithic',
        'Late Neolithic',
        'Early Bronze Age,Mid Bronze Age,Late Helladic (Mycenaean)',
        'ProtoGeometric',
        'Middle Geometric',
        'Late Geometric',
        'Early Archaic',
        'Mid Archaic',
        'Late Archaic Early Classical',
        'Mid Classica',
        'Late Classical',
        'Hellenistic',
        'Early Roman',
        'Mid Roman',
        'Late Roman',
        'Early Christian',
        'Byzantine',
        'Venetian',
        'Ottoman',
        'Early/Modern'
    ]):
        models.TimePeriod.objects.create(name=name, order=order)

    # FlaggedItemStatus
    for name in ['pending study', 'under study', 'completed', 'returned']:
        models.FlaggedItemStatus.objects.create(name=name)

    # Texture
    for name in ['coarse', 'cooking', 'semi-coarse', 'fine', 'medium']:
        models.Texture.objects.create(name=name)

    # PotteryManufactureTechnique
    for name in ['handmade', 'wheelmade', 'mouldmade']:
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
