from django.contrib import admin
from django.db.models import ManyToManyField, ForeignKey
from . import models


# Reusable code


inline_extra_default = 1
inline_view_default = 'collapse'


def get_manytomany_fields(model, exclude=[]):
    """
    Returns a list of strings containing the field names of many to many fields of a model
    To ignore certain fields, provide a list of such field names (as strings) using the exclude parameter
    """
    return list(f.name for f in model._meta.get_fields() if type(f) is ManyToManyField and f.name not in exclude)


def get_foreignkey_fields(model, exclude=[]):
    """
    Returns a list of strings containing the field names of foreign key fields of a model
    To ignore certain fields, provide a list of such field names (as strings) using the exclude parameter
    """
    return list(f.name for f in model._meta.get_fields() if type(f) is ForeignKey and f.name not in exclude)


class GenericAdminView(admin.ModelAdmin):
    """
    This is a generic class that can be applied to most models to customise their inclusion in the Django admin.

    This class can either be inherited from to customise, e.g.:
    class [ModelName]AdminView(GenericAdminView):

    Or if you don't need to customise it just register a model, e.g.:
    admin.site.register([model name], GenericAdminView)
    """
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 100
    search_fields = ('name',)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all many to many fields to display the filter_horizontal widget
        self.filter_horizontal = get_manytomany_fields(self.model)
        # Set all foreign key fields to display the autocomplete widget
        self.autocomplete_fields = get_foreignkey_fields(self.model)


class HiddenGenericAdminView(GenericAdminView):
    """
    Same as GenericAdminView, but hides model in sidebar
    """

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index
        """
        return {}


class GenericAdminStackedInline(admin.StackedInline):
    """
    This is a generic base class for StackedInline subforms
    It should be inherited via an inline, e.g. class ManuscriptInline(GenericAdminStackedInline)
    """

    extra = inline_extra_default
    classes = ['collapse']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all many to many fields to display the filter_horizontal widget
        self.filter_horizontal = get_manytomany_fields(self.model)
        # Set all foreign key fields to display the autocomplete widget
        self.autocomplete_fields = get_foreignkey_fields(self.model)


# Simple ModelAdmins


admin.site.register(models.TeamMember, HiddenGenericAdminView)
admin.site.register(models.Spacing, HiddenGenericAdminView)
admin.site.register(models.VisibilityPercentage, HiddenGenericAdminView)
admin.site.register(models.Soil, HiddenGenericAdminView)
admin.site.register(models.LandUse, HiddenGenericAdminView)
admin.site.register(models.FeatureType, HiddenGenericAdminView)
admin.site.register(models.FeatureCondition, HiddenGenericAdminView)
admin.site.register(models.MaterialType, HiddenGenericAdminView)
admin.site.register(models.GridSize, HiddenGenericAdminView)
admin.site.register(models.BulkMaterialSourceType, HiddenGenericAdminView)
admin.site.register(models.BulkMaterialProcessingStatus, HiddenGenericAdminView)
admin.site.register(models.PotteryMaterial, HiddenGenericAdminView)
admin.site.register(models.Function, HiddenGenericAdminView)
admin.site.register(models.Part, HiddenGenericAdminView)
admin.site.register(models.TimePeriod, HiddenGenericAdminView)
admin.site.register(models.FlaggedItemStatus, HiddenGenericAdminView)
admin.site.register(models.Texture, HiddenGenericAdminView)
admin.site.register(models.PotteryManufactureTechnique, HiddenGenericAdminView)
admin.site.register(models.ChronologicalCertainty, HiddenGenericAdminView)
admin.site.register(models.TileType, HiddenGenericAdminView)


# Inlines


class SurveyUnitMaterialsCountedAndCollectedInline(admin.TabularInline):
    """
    A subform/inline form for SurveyUnitMaterialsCountedAndCollected
    """
    model = models.SurveyUnitMaterialsCountedAndCollected
    extra = inline_extra_default
    classes = [inline_view_default]


class PhotographSurveyUnitMaterialBagsCollectedInline(admin.TabularInline):
    """
    A subform/inline form for PhotographSurveyUnitMaterialBagsCollected
    """
    model = models.PhotographSurveyUnitMaterialBagsCollected
    extra = inline_extra_default
    classes = [inline_view_default]
    fields = ('material', 'image', 'caption', 'date', 'photographer')


class PhotographSurveyRecordInline(admin.TabularInline):
    """
    A subform/inline form for PhotographSurveyRecord
    """
    model = models.PhotographSurveyRecord
    extra = inline_extra_default
    classes = [inline_view_default]


class PhotographFeatureInline(admin.TabularInline):
    """
    A subform/inline form for PhotographFeature
    """
    model = models.PhotographFeature
    extra = inline_extra_default
    classes = [inline_view_default]


class PhotographFeatureMaterialCollectedInline(admin.TabularInline):
    """
    A subform/inline form for PhotographFeatureMaterialCollected
    """
    model = models.PhotographFeatureMaterialCollected
    extra = inline_extra_default
    classes = [inline_view_default]
    fields = ('material', 'image', 'caption', 'date', 'photographer')


class GridSquareInline(GenericAdminStackedInline):
    """
    A subform/inline form for GridSquare
    """
    model = models.GridSquare
    extra = inline_extra_default
    classes = [inline_view_default]
    fieldsets = [
        (
            None,
            {
                'fields': [
                    'gridded_collection',
                    'square_id',
                    'coordinates_recorded',
                    'land_use',
                    'visibility_percentage',
                    'soil',
                ],
            },
        ),
        (
            'Counted',
            {
                'fields': [(
                    'pottery_counted',
                    'tile_counted',
                    'lithic_counted',
                    'other_counted',
                )],
            },
        ),
        (
            'Collected',
            {
                'fields': [(
                    'pottery_collected',
                    'tile_collected',
                    'lithic_collected',
                    'other_collected',
                )],
            },
        ),
        (
            'Bags',
            {
                'fields': [(
                    'pottery_bags',
                    'tile_bags',
                    'lithic_bags',
                    'other_bags',
                )],
            },
        ),
    ]


class PhotographGriddedCollectionInline(admin.TabularInline):
    """
    A subform/inline form for PhotographGriddedCollection
    """
    model = models.PhotographGriddedCollection
    extra = inline_extra_default
    classes = [inline_view_default]


class BulkMaterialBatchInline(GenericAdminStackedInline):
    """
    A subform/inline form for FlaggeBulkMaterialBatchdItem
    """
    model = models.BulkMaterialBatch
    extra = inline_extra_default
    classes = [inline_view_default]


class FlaggedItemInline(GenericAdminStackedInline):
    """
    A subform/inline form for FlaggedItem
    """
    model = models.FlaggedItem
    extra = inline_extra_default
    classes = [inline_view_default]


# Custom ModelAdmins


@admin.register(models.SurveyRecord)
class SurveyRecordAdminView(GenericAdminView):
    """ Customise the admin interface for SurveyRecord model """

    list_display = ('id', 'survey_unit_id',)
    list_display_links = ('id', 'survey_unit_id')
    search_fields = ('id', 'survey_unit_id',)
    inlines = (
        SurveyUnitMaterialsCountedAndCollectedInline,
        PhotographSurveyUnitMaterialBagsCollectedInline,
        PhotographSurveyRecordInline
    )
    fieldsets = [
        (
            None,
            {
                'fields': [
                    'survey_unit_id',
                    'scribe',
                    'date',
                    'time',
                    'number_of_walkers',
                    'spacing',
                    'bearing',
                    'visibility_percentage',
                    'soil',
                    'survey_unit_metadata_notes',
                ],
            },
        ),
        (
            'Current Land Use: Cultivated',
            {
                'fields': [
                    'cultivated',
                    ('cultivated_grain',
                    'cultivated_fruits',
                    'cultivated_vegetables',
                    'cultivated_olive',
                    'cultivated_vine'),
                    'cultivated_notes'
                ],
                'classes': ('collapse',),
            },
        ),
        (
            'Current Land Use: Uncultivated',
            {
                'fields': [
                    'uncultivated',
                    ('uncultivated_fallowland',
                    'uncultivated_wetland',
                    'uncultivated_scrubland',
                    'uncultivated_forest',
                    'uncultivated_pasture',
                    'uncultivated_rocky',
                    'uncultivated_abandoned'),
                    'uncultivated_notes'
                ],
                'classes': ('collapse',),
            },
        ),
        (
            'Survey Unit Materials Bags Collected',
            {
                'fields': [(
                    'survey_material_bags_collected_pottery',
                    'survey_material_bags_collected_tile',
                    'survey_material_bags_collected_lithic',
                    'survey_material_bags_collected_other',
                )],
                'classes': ('collapse',),
            },
        ),
        (
            'Survey Unit Materials Observations',
            {
                'fields': [(
                    'survey_unit_materials_observations',
                )],
                'classes': ('collapse',),
            },
        ),
    ]

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/3.7.0/jquery.min.js',
            'js/admin/main.js',
            'js/admin/survey_record.js',
        )


@admin.register(models.Feature)
class FeatureAdminView(GenericAdminView):
    """ Customise the admin interface for Feature model """

    list_display = ('id', 'feature_id',)
    list_display_links = ('id', 'feature_id',)
    search_fields = ('id', 'feature_id',)
    inlines = (
        PhotographFeatureInline,
        PhotographFeatureMaterialCollectedInline,
    )
    fieldsets = [
        (
            None,
            {
                'fields': [
                    'feature_id',
                    'feature_type',
                    'feature_description',
                    'survey_unit',
                    'coordinates_recorded',
                    'location_description',
                    ('dimensions_length_cm', 'dimensions_width_cm', 'dimensions_height_cm'),
                    'feature_condition',
                    'sketch',
                    'feature_metadata_notes',
                ],
            },
        ),
        (
            'Material Collected Around Feature',
            {
                'fields': [(
                    'material_collected_pottery_quantity',
                    'material_collected_pottery_bags',
                ),
                (
                    'material_collected_tile_quantity',
                    'material_collected_tile_bags',
                ),
                (
                    'material_collected_lithic_quantity',
                    'material_collected_lithic_bags',
                ),
                (
                    'material_collected_other_quantity',
                    'material_collected_other_bags',
                )],
                'classes': ('collapse',),
            }
        )
    ]

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/3.7.0/jquery.min.js',
            'js/admin/main.js',
            'js/admin/feature.js',
        )


@admin.register(models.GriddedCollection)
class GriddedCollectionAdminView(GenericAdminView):
    """ Customise the admin interface for GriddedCollection model """

    list_display = ('id', 'grid_id',)
    list_display_links = ('id', 'grid_id',)
    search_fields = ('id', 'grid_id',)
    inlines = (
        GridSquareInline,
        PhotographGriddedCollectionInline
    )
    fieldsets = [
        (
            None,
            {
                'fields': [
                    'grid_id',
                    'grid_size',
                    'soil',
                    'grid_metadata_notes',
                ],
            },
        ),
        (
            'Current Land Use',
            {
                'fields': [
                    'land_use',
                ],
                'classes': ('collapse',),
            },
        ),
        (
            'Current Land Use: Cultivated',
            {
                'fields': [(
                    'cultivated_grain',
                    'cultivated_fruits',
                    'cultivated_vegetables',
                    'cultivated_olive',
                    'cultivated_vine',
                )],
                'classes': ('collapse',),
            },
        ),
        (
            'Current Land Use: Uncultivated',
            {
                'fields': [(
                    'uncultivated_fallowland',
                    'uncultivated_wetland',
                    'uncultivated_scrubland',
                    'uncultivated_forest',
                    'uncultivated_pasture',
                    'uncultivated_rocky',
                    'uncultivated_abandoned',
                )],
                'classes': ('collapse',),
            },
        ),
    ]


@admin.register(models.BulkMaterial)
class BulkMaterialAdminView(GenericAdminView):
    """ Customise the admin interface for BulkMaterial model """

    list_display = ('id', 'bulk_material_id',)
    list_display_links = ('id', 'bulk_material_id',)
    search_fields = ('id', 'bulk_material_id',)
    inlines = (BulkMaterialBatchInline, FlaggedItemInline,)


@admin.register(models.FlaggedItem)
class FlaggedItemAdminView(GenericAdminView):
    """ Customise the admin interface for FlaggedItem model """

    list_display = ('id', 'flagged_item_id',)
    list_display_links = ('id', 'flagged_item_id',)
    search_fields = ('id', 'flagged_item_id',)

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index
        """
        return {}


@admin.register(models.SpecialistStudy)
class SpecialistStudyAdminView(GenericAdminView):
    """ Customise the admin interface for SpecialistStudy model """

    list_display = ('id', 'study_id',)
    list_display_links = ('id', 'study_id',)
    search_fields = ('id', 'study_id',)

    fieldsets = [
        (
            None,
            {
                'fields': [
                    'study_id',
                    'specialist',
                    'date',
                    'bulk_material',
                    'lot_number',
                    'material_type',
                    'storage_location',
                ],
            },
        ),
        (
            'Item Attributes: Pottery',
            {
                'fields': [
                    'pottery_part',
                    'pottery_material',
                    'pottery_texture',
                    'pottery_fabric',
                    'pottery_decoration_technique',
                    'pottery_manufacture_technique',
                    'pottery_shape',
                    'pottery_fabric_description',
                    'pottery_flag_for_drawing',
                    'pottery_flag_for_photography',
                    'pottery_flag_for_sampling',
                    'pottery_rim_diameter',
                    'pottery_base_diameter',
                    'pottery_general_dimensions',
                    'pottery_weight_grams',
                    'pottery_start_period',
                    'pottery_end_period',
                    'pottery_chronological_certainty',
                    'pottery_comparanda',
                    'pottery_for_publication',
                    'pottery_notes',
                    'pottery_item_returned_to_bulk',
                ],
                'classes': ('collapse',),
            },
        ),
        (
            'Item Attributes: Tile',
            {
                'fields': [
                    'tile_object_type',
                    'tile_fabric',
                    'tile_type',
                    'tile_part',
                    'tile_general_dimensions',
                    'tile_weight',
                    'tile_flag_for_drawing',
                    'tile_flag_for_photography',
                    'tile_flag_for_sampling',
                    'tile_start_period',
                    'tile_end_period',
                    'tile_chronological_certainty',
                    'tile_comparanda',
                    'tile_for_publication',
                    'tile_notes',
                    'tile_item_returned_to_bulk',
                ],
                'classes': ('collapse',),
            },
        ),
        (
            'Item Attributes: Lithic',
            {
                'fields': [
                    'lithics_object_type',
                    'lithics_material',
                    'lithics_classification',
                    'lithics_general_dimensions',
                    'lithics_weight',
                    'lithics_flag_for_drawing',
                    'lithics_flag_for_photography',
                    'lithics_flag_for_sampling',
                    'lithics_start_period',
                    'lithics_end_period',
                    'lithics_chronological_certainty',
                    'lithics_comparanda',
                    'lithics_for_publication',
                    'lithics_notes',
                    'lithics_item_returned_to_bulk',
                ],
                'classes': ('collapse',),
            },
        ),
        (
            'Item Attributes: Other',
            {
                'fields': [
                    'other_object_type',
                    'other_material_or_fabric',
                    'other_material_or_fabric_description',
                    'other_general_dimensions',
                    'other_weight',
                    'other_flag_for_drawing',
                    'other_flag_for_photography',
                    'other_flag_for_sampling',
                    'other_decoration',
                    'other_descoration_description',
                    'other_manufacture',
                    'other_start_period',
                    'other_end_period',
                    'other_chronological_certainty',
                    'other_comparanda',
                    'other_for_publication',
                    'other_notes',
                    'other_item_returned_to_bulk',
                ],
                'classes': ('collapse',),
            },
        ),
    ]
