$(document).ready(function(){

    // Warn users when they're leaving the page if there are any unsaved changes to the data
    var formHasSubmitted = false;
    function warnUsersLeavingActiveForm(){
        var form = $('#content-main form').first();
        var origForm = form.serialize();
        var formHasChanged = false;
        // If the form has changed, update the var to True (or if form has not changed reset to False)
        $('#content-main form :input').on('change input', function() { formHasChanged = form.serialize() !== origForm; });
        // Show an alert to stay on/leave the page if the form has changed
        $(window).on('beforeunload', function(){ if (formHasChanged && !formHasSubmitted) return "Leaving the page will lose unsaved changes"; });
    }
    // Execute above function on page load
    warnUsersLeavingActiveForm();
    // If certain actions taken then cancel the beforeunload event of warning users
    // If the main form is submitted
    $('#content-main form').first().on('submit', function(){ formHasSubmitted = true; });
    // If the user tries to delete the object
    $('.deletelink').on('click', function(){ formHasSubmitted = true; });

});