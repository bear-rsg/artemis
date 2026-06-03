$(document).ready(function(){

    // Move inlines to more appropriate place in the page
    $('#survey_unit_materials_counted_and_collecteds-group').detach().insertBefore('fieldset:nth-of-type(4)');
    $('#photograph_survey_record-group').detach().insertBefore('fieldset:nth-of-type(2)');
    $('#photograph_survey_unit_material_bags_collecteds-group').detach().insertBefore('fieldset:nth-of-type(6)');

});