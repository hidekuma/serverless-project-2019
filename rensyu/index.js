$(document).ready(function(){
    function dialog_init(){
        var dialog = document.querySelector('dialog');
        if (! dialog.showModal) {
            dialogPolyfill.registerDialog(dialog);
        }
        $(document).on('click', '.show-modal', function(e){
            e.preventDefault();
            dialog.showModal();
        })
        dialog.querySelector('.close').addEventListener('click', function() {
            dialog.close();
        });
        dialog.querySelector('.print').addEventListener('click', function() {
            print();
        });
    }

    function load_data(){

    }

    function submit_data(){
        $('#submitBtn').on('click',function(){
            alert('submit');
        })
    }

    dialog_init();
    load_data();
    submit_data();
})
