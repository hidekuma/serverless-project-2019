$(document).ready(function(){
    var dialog = document.querySelector('dialog');
    dialogPolyfill.registerDialog(dialog);
    $(document).on('click', '.show-modal', function(e) {
        e.preventDefault();
        dialog.showModal();
    });
    dialog.querySelector('.close').addEventListener('click', function() {
        dialog.close();
    });
    dialog.querySelector('.print').addEventListener('click', function() {
        print();
    });
});
