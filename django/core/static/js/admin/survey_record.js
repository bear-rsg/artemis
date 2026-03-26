$(document).ready(function(){

    // Move inlines to more appropriate place in the page
    $('#survey_unit_materials_counted_and_collecteds-group').detach().insertBefore('fieldset:nth-of-type(5)');
    $('#photograph_survey_record-group').detach().insertBefore('fieldset:nth-of-type(2)');
    $('#photograph_survey_unit_material_bags_collecteds-group').detach().insertBefore('fieldset:nth-of-type(6)');

    


    // // Limit options in "Document Subtype" based on value of "Type"
    // $('#id_type').on('change', function(){
    //     let textType = $(this).find('option:selected').text();
    //     let documentSubtype = $('#id_document_subtype');
    //     let documentSubtypeContainer = $('.field-document_subtype');
    //     // If selecting Administrative type
    //     if (textType.startsWith('Administrative')){
    //         documentSubtypeContainer.show();
    //         documentSubtype.find('option').each(function(){
    //             if ($(this).text().startsWith('Administrative')) $(this).show();
    //             else $(this).hide();
    //         });
    //         if (!documentSubtype.find('option:selected').text().startsWith('Administrative')) documentSubtype.val('');
    //     }
    //     // If selecting Legal type
    //     else if (textType.startsWith('Legal')){
    //         documentSubtypeContainer.show();
    //         documentSubtype.find('option').each(function(){
    //             if ($(this).text().startsWith('Legal')) $(this).show();
    //             else $(this).hide();
    //         });
    //         if (!documentSubtype.find('option:selected').text().startsWith('Legal')) documentSubtype.val('');
    //     }
    //     // If selecting none of the above
    //     else {
    //         documentSubtypeContainer.hide();
    //         documentSubtype.val('');
    //     }
    // }).trigger('change');

});