from django.contrib import admin
from django.db.models import ManyToManyField, ForeignKey
from . import models


# Reusable code


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


# Simple ModelAdmins


admin.site.register(models.TeamMember, HiddenGenericAdminView)
admin.site.register(models.Spacing, HiddenGenericAdminView)
admin.site.register(models.VisibilityPercentage, HiddenGenericAdminView)
admin.site.register(models.Soil, HiddenGenericAdminView)
admin.site.register(models.LandUse, HiddenGenericAdminView)
admin.site.register(models.LandUseCultivation, HiddenGenericAdminView)
admin.site.register(models.LandUseUncultivated, HiddenGenericAdminView)
admin.site.register(models.FeatureType, HiddenGenericAdminView)
admin.site.register(models.FeatureCondition, HiddenGenericAdminView)
admin.site.register(models.MaterialType, HiddenGenericAdminView)
admin.site.register(models.GridSize, HiddenGenericAdminView)
admin.site.register(models.BulkMaterialSourceType, HiddenGenericAdminView)
admin.site.register(models.FlaggedItemStatus, HiddenGenericAdminView)
admin.site.register(models.Fabric, HiddenGenericAdminView)
admin.site.register(models.PotteryManufactureTechnique, HiddenGenericAdminView)
admin.site.register(models.ChronologicalCertainty, HiddenGenericAdminView)
admin.site.register(models.TileType, HiddenGenericAdminView)


# Inlines


inline_extra_default = 1
inline_view_default = 'collapse'


class SurveyMaterialCountedInline(admin.TabularInline):
    """
    A subform/inline form for SurveyMaterialCounted
    """
    model = models.SurveyMaterialCounted
    extra = inline_extra_default
    classes = [inline_view_default]


class SurveyMaterialCollectedInline(admin.TabularInline):
    """
    A subform/inline form for SurveyMaterialCollected
    """
    model = models.SurveyMaterialCollected
    extra = inline_extra_default
    classes = [inline_view_default]


class PhotographSurveyMaterialBagsCollectedPotteryInline(admin.TabularInline):
    """
    A subform/inline form for PhotographSurveyMaterialBagsCollectedPottery
    """
    model = models.PhotographSurveyMaterialBagsCollectedPottery
    extra = inline_extra_default
    classes = [inline_view_default]


class PhotographSurveyMaterialBagsCollectedTileInline(admin.TabularInline):
    """
    A subform/inline form for PhotographSurveyMaterialBagsCollectedTile
    """
    model = models.PhotographSurveyMaterialBagsCollectedTile
    extra = inline_extra_default
    classes = [inline_view_default]


class PhotographSurveyMaterialBagsCollectedLithicInline(admin.TabularInline):
    """
    A subform/inline form for PhotographSurveyMaterialBagsCollectedLithic
    """
    model = models.PhotographSurveyMaterialBagsCollectedLithic
    extra = inline_extra_default
    classes = [inline_view_default]


class PhotographSurveyMaterialBagsCollectedOtherInline(admin.TabularInline):
    """
    A subform/inline form for PhotographSurveyMaterialBagsCollectedOther
    """
    model = models.PhotographSurveyMaterialBagsCollectedOther
    extra = inline_extra_default
    classes = [inline_view_default]


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


class PhotographFeatureMaterialCollectedPotteryInline(admin.TabularInline):
    """
    A subform/inline form for PhotographFeatureMaterialCollectedPottery
    """
    model = models.PhotographFeatureMaterialCollectedPottery
    extra = inline_extra_default
    classes = [inline_view_default]


class PhotographFeatureMaterialCollectedTileInline(admin.TabularInline):
    """
    A subform/inline form for PhotographFeatureMaterialCollectedTile
    """
    model = models.PhotographFeatureMaterialCollectedTile
    extra = inline_extra_default
    classes = [inline_view_default]


class PhotographFeatureMaterialCollectedLithicInline(admin.TabularInline):
    """
    A subform/inline form for PhotographFeatureMaterialCollectedLithic
    """
    model = models.PhotographFeatureMaterialCollectedLithic
    extra = inline_extra_default
    classes = [inline_view_default]


class PhotographFeatureMaterialCollectedOtherInline(admin.TabularInline):
    """
    A subform/inline form for PhotographFeatureMaterialCollectedOther
    """
    model = models.PhotographFeatureMaterialCollectedOther
    extra = inline_extra_default
    classes = [inline_view_default]


class GridSquareInline(admin.StackedInline):
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


class FlaggedItemInline(admin.StackedInline):
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

    list_display = ('id', 'survey_unit',)
    list_display_links = ('id',)
    search_fields = ('survey_unit',)
    inlines = (
        SurveyMaterialCountedInline,
        SurveyMaterialCollectedInline,
        PhotographSurveyMaterialBagsCollectedPotteryInline,
        PhotographSurveyMaterialBagsCollectedTileInline,PhotographSurveyMaterialBagsCollectedLithicInline,
        PhotographSurveyMaterialBagsCollectedOtherInline,
        PhotographSurveyRecordInline
    )


@admin.register(models.Feature)
class FeatureAdminView(GenericAdminView):
    """ Customise the admin interface for Feature model """

    list_display = ('id', 'feature_id',)
    list_display_links = ('id',)
    search_fields = ('feature_id',)
    inlines = (
        PhotographFeatureInline,
        PhotographFeatureMaterialCollectedPotteryInline,
        PhotographFeatureMaterialCollectedTileInline,
        PhotographFeatureMaterialCollectedLithicInline,
        PhotographFeatureMaterialCollectedOtherInline,
    )


@admin.register(models.GriddedCollection)
class GriddedCollectionAdminView(GenericAdminView):
    """ Customise the admin interface for GriddedCollection model """

    list_display = ('id', 'grid_id',)
    list_display_links = ('id',)
    search_fields = ('grid_id',)
    inlines = (
        GridSquareInline,
        PhotographGriddedCollectionInline
    )


@admin.register(models.BulkMaterial)
class BulkMaterialAdminView(GenericAdminView):
    """ Customise the admin interface for BulkMaterial model """

    list_display = ('id', 'bulk_material_id',)
    list_display_links = ('id',)
    search_fields = ('bulk_material_id',)
    inlines = (FlaggedItemInline,)


@admin.register(models.FlaggedItem)
class FlaggedItemAdminView(GenericAdminView):
    """ Customise the admin interface for FlaggedItem model """

    list_display = ('id', 'flagged_item_id',)
    list_display_links = ('id',)
    search_fields = ('flagged_item_id',)

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index
        """
        return {}


@admin.register(models.SpecialistStudy)
class SpecialistStudyAdminView(GenericAdminView):
    """ Customise the admin interface for SpecialistStudy model """

    list_display = ('id', 'study_id',)
    list_display_links = ('id',)
    search_fields = ('study_id',)
