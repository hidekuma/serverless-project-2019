$(document).ready(function(){
    var dialog = document.querySelector('dialog');
    dialogPolyfill.registerDialog(dialog);

    $(document).on('click', '.show-modal', function() {
        dialog.showModal();
    });
    dialog.querySelector('.print').addEventListener('click', function() {
        print();
    });
    dialog.querySelector('.close').addEventListener('click', function() {
        dialog.close();
    });
});
