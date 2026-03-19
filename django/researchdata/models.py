from django.db import models
from django.db.models.functions import Upper


# 1. Reusable code
# 2. Select List Models
# 3. Photograph Models
# 4. Primary Models


class SimpleModelAbstract(models.Model):
    """
    An abstract model for simple models that only include a name field
    See: https://docs.djangoproject.com/en/4.0/topics/db/models/#abstract-base-classes
    """

    name = models.CharField(max_length=1000, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = [Upper('name'), 'id']


class CustomOrderSimpleModelAbstract(SimpleModelAbstract):
    """
    An abstract model for simple models that need custom ordering
    See: https://docs.djangoproject.com/en/4.0/topics/db/models/#abstract-base-classes
    """
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ['order', Upper('name'), 'id']


class PhotographModelAbstract(models.Model):
    """
    An abstract model for models that record photograph data
    Models that inherit from this abstract will need to add FK field to main data model
    See: https://docs.djangoproject.com/en/4.0/topics/db/models/#abstract-base-classes
    """

    image = models.ImageField(upload_to='researchdata-photographs', blank=True, null=True)
    caption = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    photographer = models.ForeignKey('TeamMember', on_delete=models.RESTRICT, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['-id']


# 2. Select List Models


class TeamMember(SimpleModelAbstract):
    """ Member of the ARTEMIS project team """


class Spacing(CustomOrderSimpleModelAbstract):
    """ Spacing in 5 increments from 5 to 15, e.g. 5, 10, 15 """


class VisibilityPercentage(CustomOrderSimpleModelAbstract):
    """ Percentage of visibility in 5% increments from 0 to 100, e.g. 0%, 5%, 10%, etc. """


class Soil(SimpleModelAbstract):
    """ Types of soil, e.g. sandy, clay, loam, silt, rocky """


class LandUse(SimpleModelAbstract):
    """ The use of the land, e.g. cultivated or uncultivated """


class LandUseCultivation(SimpleModelAbstract):
    """ Cultivation options, e.g. grain/cereals, fruits, vegetables, olive, vine """


class LandUseUncultivated(SimpleModelAbstract):
    """ Uncultivated options, e.g. fallow land, wetland/marsh, etc """


class FeatureType(SimpleModelAbstract):
    """ Types of Features, e.g. wall, terrace, pit, quarry, etc """


class FeatureCondition(SimpleModelAbstract):
    """ The condition of a feature, e.g. good, moderate, poor, ruined """


class MaterialType(SimpleModelAbstract):
    """ Types of material, e.g. pottery, tile, lithic, other """


class GridSize(CustomOrderSimpleModelAbstract):
    """ Sizes of grids used in GriddedCollection """


class BulkMaterialSourceType(SimpleModelAbstract):
    """ Types of sources within BulkMaterial """


class FlaggedItemStatus(SimpleModelAbstract):
    """ Status of a FlaggedItem """

    class Meta:
        ordering = [Upper('name'), 'id']
        verbose_name_plural = 'flagged item statuses'


class Fabric(SimpleModelAbstract):
    """ A type of fabric, e.g. cooking, coarse, semi-coarse, fine """


class PotteryManufactureTechnique(SimpleModelAbstract):
    """ Techniques for manufacturing pottery, e.g. hand-made, wheel-made, mould-made """


class ChronologicalCertainty(SimpleModelAbstract):
    """ Certainty levels, e.g. low, medium, high """

    class Meta:
        ordering = [Upper('name'), 'id']
        verbose_name_plural = 'chronological certainties'


class TileType(SimpleModelAbstract):
    """ Types of tiles, e.g. lakonian, corinthian """


# 3. Photograph models


class PhotographSurveyRecord(PhotographModelAbstract):
    """ Photographs of SurveyRecord """

    relates_to = models.ForeignKey(
        'SurveyRecord',
        related_name='photograph_survey_record',
        on_delete=models.RESTRICT
    )


class PhotographSurveyMaterialBagsCollectedPottery(PhotographModelAbstract):
    """ Photographs of SurveyRecord > survey_material_bags_collected_pottery """

    relates_to = models.ForeignKey(
        'SurveyRecord',
        related_name='photograph_survey_material_bags_collected_potterys',
        on_delete=models.RESTRICT
    )


class PhotographSurveyMaterialBagsCollectedTile(PhotographModelAbstract):
    """ Photographs of SurveyRecord > survey_material_bags_collected_tile """

    relates_to = models.ForeignKey(
        'SurveyRecord',
        related_name='photograph_survey_material_bags_collected_tiles',
        on_delete=models.RESTRICT
    )


class PhotographSurveyMaterialBagsCollectedLithic(PhotographModelAbstract):
    """ Photographs of SurveyRecord > survey_material_bags_collected_lithic """

    relates_to = models.ForeignKey(
        'SurveyRecord',
        related_name='photograph_survey_material_bags_collected_lithics',
        on_delete=models.RESTRICT
    )


class PhotographSurveyMaterialBagsCollectedOther(PhotographModelAbstract):
    """ Photographs of SurveyRecord > survey_material_bags_collected_other """

    relates_to = models.ForeignKey(
        'SurveyRecord',
        related_name='photograph_survey_material_bags_collected_others',
        on_delete=models.RESTRICT
    )


class PhotographFeature(PhotographModelAbstract):
    """ Photographs of Feature """

    relates_to = models.ForeignKey(
        'Feature',
        related_name='photograph_features',
        on_delete=models.RESTRICT
    )


class PhotographFeatureMaterialCollectedPottery(PhotographModelAbstract):
    """ Photographs of Feature > material_collected_pottery_bags """

    relates_to = models.ForeignKey(
        'Feature',
        related_name='photograph_feature_material_collected_pottery',
        on_delete=models.RESTRICT
    )


class PhotographFeatureMaterialCollectedTile(PhotographModelAbstract):
    """ Photographs of Feature > material_collected_tile_bags """

    relates_to = models.ForeignKey(
        'Feature',
        related_name='photograph_feature_material_collected_tile',
        on_delete=models.RESTRICT
    )


class PhotographFeatureMaterialCollectedLithic(PhotographModelAbstract):
    """ Photographs of Feature > material_collected_lithic_bags """

    relates_to = models.ForeignKey(
        'Feature',
        related_name='photograph_feature_material_collected_lithic',
        on_delete=models.RESTRICT
    )


class PhotographFeatureMaterialCollectedOther(PhotographModelAbstract):
    """ Photographs of Feature > material_collected_other_bags """

    relates_to = models.ForeignKey(
        'Feature',
        related_name='photograph_feature_material_collected_other',
        on_delete=models.RESTRICT
    )


class PhotographGriddedCollection(PhotographModelAbstract):
    """ Photographs of GriddedCollection """

    relates_to = models.ForeignKey(
        'GriddedCollection',
        related_name='photograph_gridded_collections',
        on_delete=models.RESTRICT
    )


# 4. Primary Models


class SurveyRecord(models.Model):
    """
    Survey Record main form
    """

    related_name = 'survey_records'

    # 1. Survey Unit Metadata
    survey_unit = models.CharField(max_length=1000, db_index=True, blank=True, null=True)
    scribe = models.ForeignKey(TeamMember, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    number_of_walkers = models.IntegerField(blank=True, null=True)
    spacing = models.ForeignKey(Spacing, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    bearing = models.IntegerField(blank=True, null=True)
    visibility_percentage = models.ForeignKey(VisibilityPercentage, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    soil = models.ForeignKey(Soil, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    survey_unit_metadata_notes = models.TextField(blank=True, null=True)

    # 2. Current Land Use
    land_use = models.ForeignKey(LandUse, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    land_use_notes = models.TextField(blank=True, null=True)
    cultivation = models.ManyToManyField(LandUseCultivation, blank=True, related_name=related_name)
    uncultivated = models.ManyToManyField(LandUseUncultivated, blank=True, related_name=related_name)

    # 3. Survey Materials
    # A. Materials Counted
    # (see reverse FK model SurveyMaterialCounted)
    survey_material_counted_notes = models.TextField(blank=True, null=True)
    # B. Materials Collected
    # (see reverse FK model SurveyMaterialCollected)
    survey_material_collected_notes = models.TextField(blank=True, null=True)
    # C. Bags Collected
    # (each has photographs, e.g. PhotographSurveyMaterialBagsCollectedPottery)
    survey_material_bags_collected_pottery = models.IntegerField(blank=True, null=True)
    survey_material_bags_collected_tile = models.IntegerField(blank=True, null=True)
    survey_material_bags_collected_lithic = models.IntegerField(blank=True, null=True)
    survey_material_bags_collected_other = models.IntegerField(blank=True, null=True)
    survey_material_bags_collected_notes = models.TextField(blank=True, null=True)

    # 4. Photographs - see PhotographSurveyRecord model

    def __str__(self):
        return f'Survey Record #{self.id}'

    class Meta:
        ordering = ['-id',]
        verbose_name_plural = '1. Survey Record'


class SurveyMaterialCounted(models.Model):
    """
    A subform of Survey Record, for recording materials counted by each walker
    """

    related_name = 'survey_material_counteds'

    survey_record = models.ForeignKey(SurveyRecord, related_name=related_name, on_delete=models.RESTRICT)
    walker = models.ForeignKey(TeamMember, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    pottery_counted = models.IntegerField(blank=True, null=True)
    tile_counted = models.IntegerField(blank=True, null=True)
    lithic_counted = models.IntegerField(blank=True, null=True)
    other_counted = models.IntegerField(blank=True, null=True)

    @property
    def total_counted(self):
        return sum(c or 0 for c in [self.pottery_counted, self.tile_counted, self.lithic_counted, self.other_counted])

    def __str__(self):
        return f'{self.survey_record}: {self.walker}'

    class Meta:
        ordering = ['-id',]


class SurveyMaterialCollected(models.Model):
    """
    A subform of Survey Record, for recording materials collected by each walker
    """

    related_name = 'survey_material_collecteds'

    survey_record = models.ForeignKey(SurveyRecord, related_name=related_name, on_delete=models.RESTRICT)
    walker = models.ForeignKey(TeamMember, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    pottery_collected = models.IntegerField(blank=True, null=True)
    tile_collected = models.IntegerField(blank=True, null=True)
    lithic_collected = models.IntegerField(blank=True, null=True)
    other_collected = models.IntegerField(blank=True, null=True)

    @property
    def total_collected(self):
        return sum(c or 0 for c in [self.pottery_collected, self.tile_collected, self.lithic_collected, self.other_collected])

    def __str__(self):
        return f'{self.survey_record}: {self.walker}'

    class Meta:
        ordering = ['-id',]


class Feature(models.Model):
    """
    Feature main form
    """

    related_name = 'features'

    # 1. Features Metadata
    feature_id = models.CharField(max_length=1000, unique=True, db_index=True)
    feature_type = models.ForeignKey(FeatureType, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    feature_description = models.TextField(blank=True, null=True)
    survey_unit = models.ForeignKey(SurveyRecord, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    coordinates_recorded = models.BooleanField(default=False)
    orientation = models.TextField(blank=True, null=True)
    dimensions_length_cm = models.IntegerField(blank=True, null=True)
    dimensions_width_cm = models.IntegerField(blank=True, null=True)
    dimensions_height_cm = models.IntegerField(blank=True, null=True)
    feature_condition = models.ForeignKey(FeatureCondition, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    sketch = models.TextField(blank=True, null=True)
    feature_metadata_notes = models.TextField(blank=True, null=True)

    # 2. Photographs - see PhotographFeature model

    # 3. Material Collected Around Feature

    # Pottery
    material_collected_pottery_quantity = models.IntegerField(blank=True, null=True)
    material_collected_pottery_bags = models.IntegerField(blank=True, null=True)
    # Photographs - see PhotographFeatureMaterialCollectedPottery

    # Tile
    material_collected_tile_quantity = models.IntegerField(blank=True, null=True)
    material_collected_tile_bags = models.IntegerField(blank=True, null=True)
    # Photographs - see PhotographFeatureMaterialCollectedTile

    # Lithic
    material_collected_lithic_quantity = models.IntegerField(blank=True, null=True)
    material_collected_lithic_bags = models.IntegerField(blank=True, null=True)
    # Photographs - see PhotographFeatureMaterialCollectedLithic

    # Other
    material_collected_other_quantity = models.IntegerField(blank=True, null=True)
    material_collected_other_bags = models.IntegerField(blank=True, null=True)
    # Photographs - see PhotographFeatureMaterialCollectedOther

    def __str__(self):
        return f'Feature #{self.id}'

    class Meta:
        ordering = ['-id',]
        verbose_name_plural = '2. Feature'


class GriddedCollection(models.Model):
    """
    Gridded Collection main form
    """

    related_name = 'gridded_collections'

    # 1. Grid Metadata
    grid_id = models.CharField(max_length=1000, unique=True, db_index=True)
    grid_size = models.ForeignKey(GridSize, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    land_use = models.ForeignKey(LandUse, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    cultivation = models.ManyToManyField(LandUseCultivation, blank=True, related_name=related_name)
    uncultivated = models.ManyToManyField(LandUseUncultivated, blank=True, related_name=related_name)
    soil = models.ForeignKey(Soil, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    grid_metadata_notes = models.TextField(blank=True, null=True)

    # 2. Grid Squares - see GridSquare model

    # 3. Photographs - see PhotographGriddedCollection model

    def __str__(self):
        return f'Gridded Collection #{self.id}'

    class Meta:
        ordering = ['-id',]
        verbose_name_plural = '3. Gridded Collection'


class GridSquare(models.Model):
    """
    Grid Square subform of Gridded Collection main form
    """

    related_name = 'grid_squares'

    gridded_collection = models.ForeignKey(GriddedCollection, related_name=related_name, on_delete=models.RESTRICT)
    square_id = models.CharField(max_length=1000, unique=True, db_index=True)
    coordinates_recorded = models.BooleanField(default=False)
    land_use = models.ForeignKey(LandUse, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    visibility_percentage = models.ForeignKey(VisibilityPercentage, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    soil = models.ForeignKey(Soil, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)

    pottery_counted = models.IntegerField(blank=True, null=True)
    tile_counted = models.IntegerField(blank=True, null=True)
    lithic_counted = models.IntegerField(blank=True, null=True)
    other_counted = models.IntegerField(blank=True, null=True)

    pottery_collected = models.IntegerField(blank=True, null=True)
    tile_collected = models.IntegerField(blank=True, null=True)
    lithic_collected = models.IntegerField(blank=True, null=True)
    other_collected = models.IntegerField(blank=True, null=True)

    pottery_bags = models.IntegerField(blank=True, null=True)
    tile_bags = models.IntegerField(blank=True, null=True)
    lithic_bags = models.IntegerField(blank=True, null=True)
    other_bags = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'Grid Square #{self.id}'

    class Meta:
        ordering = ['-id',]


class BulkMaterial(models.Model):
    """
    Bulk Material main form
    """

    related_name = 'bulk_materials'

    # 1. Bulk Material Metadata
    bulk_material_id = models.CharField(max_length=1000, unique=True, db_index=True)
    source_type = models.ForeignKey(BulkMaterialSourceType, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    source_id = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    processed_by = models.ForeignKey(TeamMember, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    storage_location = models.TextField(blank=True, null=True)
    material_type = models.ForeignKey(MaterialType, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    weight = models.TextField(blank=True, null=True)
    bulk_photograph = models.ImageField(upload_to='researchdata-photographs', blank=True, null=True)
    bulk_observations = models.TextField(blank=True, null=True)
    flagged_for_study = models.BooleanField(default=False)
    flagged_for_study_reason = models.TextField(blank=True, null=True)

    # 2. Flagged Items - see FlaggedItem model

    def __str__(self):
        return f'Bulk Material #{self.id}'

    class Meta:
        ordering = ['-id',]
        verbose_name_plural = '4. Bulk Material'


class FlaggedItem(models.Model):
    """
    Flagged Item subform of Bulk Material main form
    """

    related_name = 'flagged_items'

    bulk_material = models.ForeignKey(BulkMaterial, related_name=related_name, on_delete=models.RESTRICT)
    flagged_item_id = models.CharField(max_length=1000, unique=True, db_index=True)
    material_type = models.ForeignKey(MaterialType, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    reason_for_flagging = models.TextField(blank=True, null=True)
    flagged_item_photograph = models.ImageField(upload_to='researchdata-photographs', blank=True, null=True)
    status = models.ForeignKey(FlaggedItemStatus, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)

    def __str__(self):
        return f'Flagged Item #{self.id}'

    class Meta:
        ordering = ['-id',]


class SpecialistStudy(models.Model):
    """
    Specialist Study main form
    """

    related_name = 'specialist_studies'

    # 1. Study Metadata
    study_id = models.CharField(max_length=1000, unique=True, db_index=True)
    specialist = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    bulk_material = models.ForeignKey(BulkMaterial, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    flagged_item = models.ForeignKey(FlaggedItem, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    material_type = models.ForeignKey(MaterialType, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    storage_location = models.TextField(blank=True, null=True)

    # 2. Item Attributes

    # 2a. Pottery
    pottery_object_type = models.TextField(blank=True, null=True)
    pottery_fabric = models.ForeignKey(Fabric, related_name=f'{related_name}_pottery', on_delete=models.RESTRICT, blank=True, null=True)
    pottery_decoration_technique = models.TextField(blank=True, null=True)
    pottery_manufacture_technique = models.ForeignKey(PotteryManufactureTechnique, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    pottery_shape = models.TextField(blank=True, null=True)
    pottery_fabric_description = models.TextField(blank=True, null=True)
    pottery_flag_for_drawing = models.BooleanField(default=False)
    pottery_flag_for_photography = models.BooleanField(default=False)
    pottery_flag_for_sampling = models.BooleanField(default=False)
    pottery_rim_diameter = models.TextField(blank=True, null=True)
    pottery_base_diameter = models.TextField(blank=True, null=True)
    pottery_general_dimensions = models.TextField(blank=True, null=True)
    pottery_weight = models.TextField(blank=True, null=True)
    pottery_start_period = models.TextField(blank=True, null=True)
    pottery_end_period = models.TextField(blank=True, null=True)
    pottery_chronological_certainty = models.ForeignKey(ChronologicalCertainty, related_name=f'{related_name}_pottery', on_delete=models.RESTRICT, blank=True, null=True)
    pottery_comparanda = models.TextField(blank=True, null=True)
    pottery_for_publication = models.BooleanField(default=False)
    pottery_notes = models.TextField(blank=True, null=True)
    pottery_item_returned_to_bulk = models.BooleanField(default=False)

    # 2b. Tile
    tile_object_type = models.TextField(blank=True, null=True)
    tile_fabric = models.ForeignKey(Fabric, related_name=f'{related_name}_tile', on_delete=models.RESTRICT, blank=True, null=True)
    tile_type = models.ForeignKey(TileType, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    tile_part = models.TextField(blank=True, null=True)
    tile_general_dimensions = models.TextField(blank=True, null=True)
    tile_weight = models.TextField(blank=True, null=True)
    tile_flag_for_drawing = models.BooleanField(default=False)
    tile_flag_for_photography = models.BooleanField(default=False)
    tile_flag_for_sampling = models.BooleanField(default=False)
    tile_start_period = models.TextField(blank=True, null=True)
    tile_end_period = models.TextField(blank=True, null=True)
    tile_chronological_certainty = models.ForeignKey(ChronologicalCertainty, related_name=f'{related_name}_tile', on_delete=models.RESTRICT, blank=True, null=True)
    tile_comparanda = models.TextField(blank=True, null=True)
    tile_for_publication = models.BooleanField(default=False)
    tile_notes = models.TextField(blank=True, null=True)
    tile_item_returned_to_bulk = models.BooleanField(default=False)

    # 2c. Lithics
    lithics_object_type = models.TextField(blank=True, null=True)
    lithics_material = models.TextField(blank=True, null=True)
    lithics_classification = models.TextField(blank=True, null=True)
    lithics_general_dimensions = models.TextField(blank=True, null=True)
    lithics_weight = models.TextField(blank=True, null=True)
    lithics_flag_for_drawing = models.BooleanField(default=False)
    lithics_flag_for_photography = models.BooleanField(default=False)
    lithics_flag_for_sampling = models.BooleanField(default=False)
    lithics_start_period = models.TextField(blank=True, null=True)
    lithics_end_period = models.TextField(blank=True, null=True)
    lithics_chronological_certainty = models.ForeignKey(ChronologicalCertainty, related_name=f'{related_name}_lithics', on_delete=models.RESTRICT, blank=True, null=True)
    lithics_comparanda = models.TextField(blank=True, null=True)
    lithics_for_publication = models.BooleanField(default=False)
    lithics_notes = models.TextField(blank=True, null=True)
    lithics_item_returned_to_bulk = models.BooleanField(default=False)

    # 2d. Other
    other_object_type = models.TextField(blank=True, null=True)
    other_material_or_fabric = models.TextField(blank=True, null=True)
    other_material_or_fabric_description = models.TextField(blank=True, null=True)
    other_general_dimensions = models.TextField(blank=True, null=True)
    other_weight = models.TextField(blank=True, null=True)
    other_flag_for_drawing = models.BooleanField(default=False)
    other_flag_for_photography = models.BooleanField(default=False)
    other_flag_for_sampling = models.BooleanField(default=False)
    other_decoration = models.BooleanField(default=False)
    other_descoration_description = models.TextField(blank=True, null=True)
    other_manufacture = models.TextField(blank=True, null=True)
    other_start_period = models.TextField(blank=True, null=True)
    other_end_period = models.TextField(blank=True, null=True)
    other_chronological_certainty = models.ForeignKey(ChronologicalCertainty, related_name=f'{related_name}_other', on_delete=models.RESTRICT, blank=True, null=True)
    other_comparanda = models.TextField(blank=True, null=True)
    other_for_publication = models.BooleanField(default=False)
    other_notes = models.TextField(blank=True, null=True)
    other_item_returned_to_bulk = models.BooleanField(default=False)

    def __str__(self):
        return f'Specialist Study #{self.id}'

    class Meta:
        ordering = ['-id',]
        verbose_name_plural = '5. Specialist Study'
