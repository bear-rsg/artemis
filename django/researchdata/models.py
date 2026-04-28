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
        return self.image.name

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


class FeatureType(SimpleModelAbstract):
    """ Types of Features, e.g. wall, terrace, pit, quarry, etc """


class FeatureCondition(SimpleModelAbstract):
    """ The condition of a feature, e.g. good, moderate, poor, ruined """


class MaterialType(CustomOrderSimpleModelAbstract):
    """ Types of material, e.g. pottery, tile, lithic, other """


class GridSize(CustomOrderSimpleModelAbstract):
    """ Sizes of grids used in GriddedCollection """


class BulkMaterialSourceType(CustomOrderSimpleModelAbstract):
    """ Types of sources within BulkMaterial """


class BulkMaterialProcessingStatus(SimpleModelAbstract):
    """ Statuses of process of BulkMaterial """


class PotteryMaterial(SimpleModelAbstract):
    """ Materials used in pottery """


class Function(SimpleModelAbstract):
    """ The function/purpose of a BulkMaterialBatch, e.g. transport, storage, easting, drinking """


class Part(SimpleModelAbstract):
    """ The part a BulkMaterialBatch, e.g. rim, body, base """


class TimePeriod(CustomOrderSimpleModelAbstract):
    """ A period of time, e.g. Early Neolithic, Mid Neolithic, Late Neolithic, etc. """


class FlaggedItemStatus(SimpleModelAbstract):
    """ Status of a FlaggedItem """

    class Meta:
        ordering = [Upper('name'), 'id']
        verbose_name_plural = 'flagged item statuses'


class Texture(SimpleModelAbstract):
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
    class Meta:
        verbose_name_plural = 'Survey Unit Photographs'


class PhotographSurveyUnitMaterialBagsCollected(PhotographModelAbstract):
    """ Photographs of SurveyRecord > survey unit materials bags collected """

    related_name = 'photograph_survey_unit_material_bags_collecteds'

    relates_to = models.ForeignKey('SurveyRecord', related_name=related_name, on_delete=models.RESTRICT)
    material = models.ForeignKey('MaterialType', related_name=related_name, on_delete=models.RESTRICT)

    class Meta:
        verbose_name_plural = 'Survey Unit Materials Bags Collected Photographs'


class PhotographFeature(PhotographModelAbstract):
    """ Photographs of Feature """

    relates_to = models.ForeignKey(
        'Feature',
        related_name='photograph_features',
        on_delete=models.RESTRICT
    )


class PhotographFeatureMaterialCollected(PhotographModelAbstract):
    """ Photographs of Feature > material_collected_pottery_bags """

    related_name = 'photograph_feature_material_collecteds'

    relates_to = models.ForeignKey(
        'Feature',
        related_name='photograph_feature_material_collected_pottery',
        on_delete=models.RESTRICT
    )
    material = models.ForeignKey('MaterialType', related_name=related_name, on_delete=models.RESTRICT)

    class Meta:
        verbose_name_plural = 'Material Collected Around Feature Photographs'


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
    survey_unit_id = models.CharField(max_length=1000, db_index=True, unique=True)
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
    # A. Cultivated
    cultivated = models.BooleanField(default=False)
    cultivated_grain = models.BooleanField(default=False, verbose_name='grain/cereals')
    cultivated_fruits = models.BooleanField(default=False, verbose_name='fruits')
    cultivated_vegetables = models.BooleanField(default=False, verbose_name='vegetables')
    cultivated_olive = models.BooleanField(default=False, verbose_name='olive')
    cultivated_vine = models.BooleanField(default=False, verbose_name='vine')
    cultivated_notes = models.TextField(blank=True, null=True)
    # B. Uncultivated
    uncultivated = models.BooleanField(default=False)
    uncultivated_fallowland = models.BooleanField(default=False, verbose_name='fallow land')
    uncultivated_wetland = models.BooleanField(default=False, verbose_name='wetland/marsh')
    uncultivated_scrubland = models.BooleanField(default=False, verbose_name='scrubland/maquis/garrigue')
    uncultivated_forest = models.BooleanField(default=False, verbose_name='forest/woodland')
    uncultivated_pasture = models.BooleanField(default=False, verbose_name='natural pasture/grazing land')
    uncultivated_rocky = models.BooleanField(default=False, verbose_name='rocky/barren ground')
    uncultivated_abandoned = models.BooleanField(default=False, verbose_name='abandoned agricultural land')
    uncultivated_notes = models.TextField(blank=True, null=True)

    # 3. Survey Unit Materials
    # A. Materials Counted and Collected
    # (see reverse FK model SurveyUnitMaterialsCountedAndCollected)
    # B. Bags Collected
    survey_material_bags_collected_pottery = models.IntegerField(blank=True, null=True, verbose_name='No. of pottery bags')
    survey_material_bags_collected_tile = models.IntegerField(blank=True, null=True, verbose_name='No. of tile bags')
    survey_material_bags_collected_lithic = models.IntegerField(blank=True, null=True, verbose_name='No. of lithic bags')
    survey_material_bags_collected_other = models.IntegerField(blank=True, null=True, verbose_name='No. of other bags')
    # (see reverse FK model, e.g. PhotographSurveyMaterialBagsCollected)
    # C. Materials Observations
    survey_unit_materials_observations = models.TextField(blank=True, null=True)

    # 4. Photographs - see PhotographSurveyRecord model

    def __str__(self):
        return self.survey_unit_id

    class Meta:
        ordering = ['-id',]
        verbose_name_plural = '1. Survey Record'


class SurveyUnitMaterialsCountedAndCollected(models.Model):
    """
    A subform of Survey Record, for recording materials counted by each walker
    """

    related_name = 'survey_unit_materials_counted_and_collecteds'

    survey_record = models.ForeignKey(SurveyRecord, related_name=related_name, on_delete=models.RESTRICT)
    walker = models.ForeignKey(TeamMember, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)

    pottery_counted = models.IntegerField(blank=True, null=True)
    pottery_collected = models.IntegerField(blank=True, null=True)

    tile_counted = models.IntegerField(blank=True, null=True)
    tile_collected = models.IntegerField(blank=True, null=True)

    lithic_counted = models.IntegerField(blank=True, null=True)
    lithic_collected = models.IntegerField(blank=True, null=True)

    other_counted = models.IntegerField(blank=True, null=True)
    other_collected = models.IntegerField(blank=True, null=True)

    @property
    def total_counted(self):
        return sum(c or 0 for c in [self.pottery_counted, self.tile_counted, self.lithic_counted, self.other_counted])

    @property
    def total_collected(self):
        return sum(c or 0 for c in [self.pottery_collected, self.tile_collected, self.lithic_collected, self.other_collected])

    def __str__(self):
        return f'{self.survey_record}: {self.walker}'

    class Meta:
        ordering = ['-id',]
        verbose_name_plural = "Survey Unit Materials Counted And Collected"


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
    location_description = models.TextField(blank=True, null=True)
    dimensions_length_cm = models.IntegerField(blank=True, null=True, verbose_name='length (cm)')
    dimensions_width_cm = models.IntegerField(blank=True, null=True, verbose_name='width (cm)')
    dimensions_height_cm = models.IntegerField(blank=True, null=True, verbose_name='height (cm)')
    feature_condition = models.ForeignKey(FeatureCondition, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    sketch = models.ImageField(upload_to='researchdata-photographs', blank=True, null=True)
    feature_metadata_notes = models.TextField(blank=True, null=True)

    # 2. Photographs - see PhotographFeature model

    # 3. Material Collected Around Feature

    # Pottery
    material_collected_pottery_quantity = models.IntegerField(blank=True, null=True, verbose_name='No. of pottery collected')
    material_collected_pottery_bags = models.IntegerField(blank=True, null=True, verbose_name='No. of pottery bags')

    # Tile
    material_collected_tile_quantity = models.IntegerField(blank=True, null=True, verbose_name='No. of tile collected')
    material_collected_tile_bags = models.IntegerField(blank=True, null=True, verbose_name='No. of tile bags')

    # Lithic
    material_collected_lithic_quantity = models.IntegerField(blank=True, null=True, verbose_name='No. of lithic collected')
    material_collected_lithic_bags = models.IntegerField(blank=True, null=True, verbose_name='No. of lithic bags')

    # Other
    material_collected_other_quantity = models.IntegerField(blank=True, null=True, verbose_name='No. of other collected')
    material_collected_other_bags = models.IntegerField(blank=True, null=True, verbose_name='No. of other bags')

    # 4. Photographs of Materials - see PhotographFeatureMaterialCollected model

    def __str__(self):
        return self.feature_id

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
    soil = models.ForeignKey(Soil, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    grid_metadata_notes = models.TextField(blank=True, null=True)

    # 2. Land Use
    land_use = models.ForeignKey(LandUse, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    # A. Cultivated
    cultivated_grain = models.BooleanField(default=False, verbose_name='grain/cereals')
    cultivated_fruits = models.BooleanField(default=False, verbose_name='fruits')
    cultivated_vegetables = models.BooleanField(default=False, verbose_name='vegetables')
    cultivated_olive = models.BooleanField(default=False, verbose_name='olive')
    cultivated_vine = models.BooleanField(default=False, verbose_name='vine')
    # B. Uncultivated
    uncultivated_fallowland = models.BooleanField(default=False, verbose_name='fallow land')
    uncultivated_wetland = models.BooleanField(default=False, verbose_name='wetland/marsh')
    uncultivated_scrubland = models.BooleanField(default=False, verbose_name='scrubland/maquis/garrigue')
    uncultivated_forest = models.BooleanField(default=False, verbose_name='forest/woodland')
    uncultivated_pasture = models.BooleanField(default=False, verbose_name='natural pasture/grazing land')
    uncultivated_rocky = models.BooleanField(default=False, verbose_name='rocky/barren ground')
    uncultivated_abandoned = models.BooleanField(default=False, verbose_name='abandoned agricultural land')

    # 3. Grid Squares - see GridSquare model

    # 4. Photographs - see PhotographGriddedCollection model

    def __str__(self):
        return self.grid_id

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
        return self.square_id

    class Meta:
        ordering = ['-id',]


class BulkMaterial(models.Model):
    """
    Bulk Material main form
    """

    related_name = 'bulk_materials'

    # 1. Bulk Material Observations
    bulk_material_id = models.CharField(max_length=1000, unique=True, db_index=True)
    source_type = models.ForeignKey(BulkMaterialSourceType, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    source_id = models.CharField(max_length=1000, blank=True, null=True)
    date_batch_created = models.DateField(blank=True, null=True)
    date_of_collection = models.DateField(blank=True, null=True)
    processed_by = models.ForeignKey(TeamMember, related_name=f'{related_name}_processed_by', on_delete=models.RESTRICT, blank=True, null=True)
    checked_by = models.ForeignKey(TeamMember, related_name=f'{related_name}_checked_by', on_delete=models.RESTRICT, blank=True, null=True)
    checked_by = models.ForeignKey(BulkMaterialProcessingStatus, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    storage_location = models.TextField(blank=True, null=True)
    total_sherd_count = models.IntegerField(blank=True, null=True)
    material_type = models.ForeignKey(MaterialType, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    weight = models.TextField(blank=True, null=True, verbose_name='weight (g)')
    bulk_photograph = models.ImageField(upload_to='researchdata-photographs', blank=True, null=True)
    bulk_observations = models.TextField(blank=True, null=True)

    # 2. Batches - see BulkMaterialBatch model

    # 3. Flagged Items - see FlaggedItem model

    def __str__(self):
        return self.bulk_material_id

    class Meta:
        ordering = ['-id',]
        verbose_name_plural = '4. Bulk Material'


class BulkMaterialBatch(models.Model):
    """
    Batch subform of Bulk Material main form
    """

    related_name = 'bulk_material_batches'

    bulk_material = models.ForeignKey(BulkMaterial, related_name=related_name, on_delete=models.RESTRICT)
    lot_number = models.CharField(max_length=1000, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    material = models.ForeignKey(PotteryMaterial, related_name=related_name, on_delete=models.SET_NULL, blank=True, null=True)
    technique = models.ForeignKey(PotteryManufactureTechnique, related_name=related_name, on_delete=models.SET_NULL, blank=True, null=True)
    texture = models.ForeignKey(Texture, related_name=related_name, on_delete=models.SET_NULL, blank=True, null=True)
    fabric = models.CharField(max_length=1000, blank=True, null=True)
    function = models.ForeignKey(Function, related_name=related_name, on_delete=models.SET_NULL, blank=True, null=True)
    part = models.ForeignKey(Part, related_name=related_name, on_delete=models.SET_NULL, blank=True, null=True)
    shape = models.CharField(max_length=1000, blank=True, null=True)
    start_period = models.ForeignKey(TimePeriod, related_name=f'{related_name}_start_period', on_delete=models.SET_NULL, blank=True, null=True)
    end_period = models.ForeignKey(TimePeriod, related_name=f'{related_name}_end_period', on_delete=models.SET_NULL, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    catalogue = models.BooleanField(default=False)

    def __str__(self):
        return f'bulk material batch #{self.id}'

    class Meta:
        ordering = ['-id',]
        verbose_name_plural = 'bulk material batches'


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
        return self.flagged_item_id

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
    lot_number = models.ForeignKey(FlaggedItem, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    material_type = models.ForeignKey(MaterialType, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    storage_location = models.CharField(max_length=1000, blank=True, null=True)

    # 2. Item Attributes

    # 2a. Pottery
    pottery_part = models.ForeignKey(Part, related_name=related_name, on_delete=models.SET_NULL, blank=True, null=True)
    pottery_material = models.ForeignKey(PotteryMaterial, related_name=related_name, on_delete=models.SET_NULL, blank=True, null=True)
    pottery_texture = models.ForeignKey(Texture, related_name=f'{related_name}_pottery_texture', on_delete=models.SET_NULL, blank=True, null=True)
    function = models.ForeignKey(Function, related_name=related_name, on_delete=models.SET_NULL, blank=True, null=True)
    pottery_decoration_technique = models.CharField(max_length=1000, blank=True, null=True)
    pottery_manufacture_technique = models.ForeignKey(PotteryManufactureTechnique, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    pottery_shape = models.CharField(max_length=1000, blank=True, null=True)
    pottery_fabric_description = models.CharField(max_length=1000, blank=True, null=True)
    pottery_flag_for_drawing = models.BooleanField(default=False)
    pottery_flag_for_photography = models.BooleanField(default=False)
    pottery_flag_for_sampling = models.BooleanField(default=False)
    pottery_rim_diameter = models.CharField(max_length=1000, blank=True, null=True)
    pottery_base_diameter = models.CharField(max_length=1000, blank=True, null=True)
    pottery_general_dimensions = models.CharField(max_length=1000, blank=True, null=True)
    pottery_weight_grams = models.IntegerField(blank=True, null=True)
    pottery_start_period = models.ForeignKey(TimePeriod, related_name=f'{related_name}_start_period', on_delete=models.SET_NULL, blank=True, null=True)
    pottery_end_period = models.ForeignKey(TimePeriod, related_name=f'{related_name}_end_period', on_delete=models.SET_NULL, blank=True, null=True)
    pottery_chronological_certainty = models.ForeignKey(ChronologicalCertainty, related_name=f'{related_name}_pottery', on_delete=models.RESTRICT, blank=True, null=True)
    pottery_comparanda = models.CharField(max_length=1000, blank=True, null=True)
    pottery_for_publication = models.BooleanField(default=False)
    pottery_notes = models.TextField(blank=True, null=True)
    pottery_item_returned_to_bulk = models.BooleanField(default=False)

    # 2b. Tile
    tile_object_type = models.CharField(max_length=1000, blank=True, null=True)
    tile_fabric = models.ForeignKey(Texture, related_name=f'{related_name}_tile_frabic', on_delete=models.RESTRICT, blank=True, null=True)
    tile_type = models.ForeignKey(TileType, related_name=related_name, on_delete=models.RESTRICT, blank=True, null=True)
    tile_part = models.CharField(max_length=1000, blank=True, null=True)
    tile_general_dimensions = models.CharField(max_length=1000, blank=True, null=True)
    tile_weight = models.CharField(max_length=1000, blank=True, null=True)
    tile_flag_for_drawing = models.BooleanField(default=False)
    tile_flag_for_photography = models.BooleanField(default=False)
    tile_flag_for_sampling = models.BooleanField(default=False)
    tile_start_period = models.CharField(max_length=1000, blank=True, null=True)
    tile_end_period = models.CharField(max_length=1000, blank=True, null=True)
    tile_chronological_certainty = models.ForeignKey(ChronologicalCertainty, related_name=f'{related_name}_tile', on_delete=models.RESTRICT, blank=True, null=True)
    tile_comparanda = models.CharField(max_length=1000, blank=True, null=True)
    tile_for_publication = models.BooleanField(default=False)
    tile_notes = models.TextField(blank=True, null=True)
    tile_item_returned_to_bulk = models.BooleanField(default=False)

    # 2c. Lithics
    lithics_object_type = models.CharField(max_length=1000, blank=True, null=True)
    lithics_material = models.CharField(max_length=1000, blank=True, null=True)
    lithics_classification = models.CharField(max_length=1000, blank=True, null=True)
    lithics_general_dimensions = models.CharField(max_length=1000, blank=True, null=True)
    lithics_weight = models.CharField(max_length=1000, blank=True, null=True)
    lithics_flag_for_drawing = models.BooleanField(default=False)
    lithics_flag_for_photography = models.BooleanField(default=False)
    lithics_flag_for_sampling = models.BooleanField(default=False)
    lithics_start_period = models.CharField(max_length=1000, blank=True, null=True)
    lithics_end_period = models.CharField(max_length=1000, blank=True, null=True)
    lithics_chronological_certainty = models.ForeignKey(ChronologicalCertainty, related_name=f'{related_name}_lithics', on_delete=models.RESTRICT, blank=True, null=True)
    lithics_comparanda = models.CharField(max_length=1000, blank=True, null=True)
    lithics_for_publication = models.BooleanField(default=False)
    lithics_notes = models.TextField(blank=True, null=True)
    lithics_item_returned_to_bulk = models.BooleanField(default=False)

    # 2d. Other
    other_object_type = models.CharField(max_length=1000, blank=True, null=True)
    other_material_or_fabric = models.CharField(max_length=1000, blank=True, null=True)
    other_material_or_fabric_description = models.CharField(max_length=1000, blank=True, null=True)
    other_general_dimensions = models.CharField(max_length=1000, blank=True, null=True)
    other_weight = models.CharField(max_length=1000, blank=True, null=True)
    other_flag_for_drawing = models.BooleanField(default=False)
    other_flag_for_photography = models.BooleanField(default=False)
    other_flag_for_sampling = models.BooleanField(default=False)
    other_decoration = models.BooleanField(default=False)
    other_descoration_description = models.CharField(max_length=1000, blank=True, null=True)
    other_manufacture = models.CharField(max_length=1000, blank=True, null=True)
    other_start_period = models.CharField(max_length=1000, blank=True, null=True)
    other_end_period = models.CharField(max_length=1000, blank=True, null=True)
    other_chronological_certainty = models.ForeignKey(ChronologicalCertainty, related_name=f'{related_name}_other', on_delete=models.RESTRICT, blank=True, null=True)
    other_comparanda = models.CharField(max_length=1000, blank=True, null=True)
    other_for_publication = models.BooleanField(default=False)
    other_notes = models.TextField(blank=True, null=True)
    other_item_returned_to_bulk = models.BooleanField(default=False)

    def __str__(self):
        return self.study_id

    class Meta:
        ordering = ['-id',]
        verbose_name_plural = '5. Specialist Study'
