$(document).ready(function(){

    //
    // Offline warning
    //

    // Add an offline alert message
    $('.submit-row').append('<div id="offlinealert">⚠️ You are offline. Please wait for an active internet connection before saving the form</div>')

    const $offlineAlert = $('#offlinealert');
    const $saveButtons = $('input[name="_save"], input[name="_addanother"], input[name="_continue"], .deletelink');

    function updateNetworkStatus() {
        if (navigator.onLine) {
            // We have internet: Hide alert, enable buttons
            $offlineAlert.hide();
            $saveButtons.show();
        } else {
            // We are offline: Show alert, disable buttons
            $offlineAlert.show();
            $saveButtons.hide();
        }
    }

    // 1. Check the status immediately when the page loads
    updateNetworkStatus();
    // 2. Listen for the browser's native network events
    $(window).on('online offline', function() {
        updateNetworkStatus();
    });


    //
    // Image compression
    //

    // Compression Settings
    const IMG_MAX_WIDTH_PX = 1920;
    const IMG_QUALITY = 0.8;

    // Listen for file selections on ANY file input in the admin
    $(document).on('change', 'input[type="file"]', function(e){
        const inputElement = e.target;
        const file = inputElement.files[0];

        // Ignore if no file is selected or if it's not an image (e.g., PDFs)
        if (!file || !file.type.startsWith('image/')) return;

        const reader = new FileReader();

        reader.onload = function(event){
            const img = new Image();

            img.onload = function(){
                const canvas = document.createElement('canvas');
                let width = img.width;
                let height = img.height;

                // Resize keeping aspect ratio
                if (width > IMG_MAX_WIDTH_PX){
                    height = Math.round((height * IMG_MAX_WIDTH_PX) / width);
                    width = IMG_MAX_WIDTH_PX;
                }

                canvas.width = width;
                canvas.height = height;

                // Draw image to canvas
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, width, height);

                // Convert to compressed JPEG blob
                canvas.toBlob(function(blob){
                    // Force .jpeg extension for backend consistency
                    const newFileName = file.name.replace(/\.[^/.]+$/, "") + ".jpg";
                    // Create a new File object
                    const compressedFile = new File([blob], newFileName, {
                        type: 'image/jpeg',
                        lastModified: Date.now()
                    });
                    // Swap the files in the input field using DataTransfer
                    const dataTransfer = new DataTransfer();
                    dataTransfer.items.add(compressedFile);
                    inputElement.files = dataTransfer.files;
                }, 'image/jpeg', IMG_QUALITY);
            };

            img.src = event.target.result;
        };

        reader.readAsDataURL(file);
    });

});