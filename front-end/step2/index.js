$(document).ready(function(){
    var dialog = document.querySelector('dialog');
    dialogPolyfill.registerDialog(dialog);
    $(document).on('click', '.show-modal', function(e){
        e.preventDefault();
        var data = $(this).data();
        var user = data['user'];
        var type = data['type'];
        $('#showBox').html('<img style="width:100%" src="'+'{cloudfront:endpoint}'+'/qrcodes/'+user+'/'+type+'/qrcode.jpg"/>');
        dialog.showModal();
    });
    dialog.querySelector('.close').addEventListener('click', function() {
        dialog.close();
    });
    dialog.querySelector('.print').addEventListener('click', function() {
        print();
    });

    $('#submitBtn').on('click', function(){
        submit();
    })
    function submit(){
        var user_name = $('#user_name').val();
        var phone_number = $('#phone_number').val();
        var company_name = $('#company_name').val();
        var user_id = $('#user_id').val();
        var type = $('#type').val();

        $.ajax({
            url: '{api-gateway:endpoint}',
            method: 'post',
            datatype: 'json',
            data:JSON.stringify({
                type: type,
                user_id: user_id,
                user_name: user_name,
                phone_number: phone_number,
                company_name: company_name
            }),
            success: function(r){
                console.log(r);
            },
            complete: function(r){
                console.log(r);
                location.reload();

            }
        })

    }

    function load_data(){
        $.ajax({
            url: '{ap-gateway:endpoint}',
            method: 'get',
            success: function(r){
                var html = '';
                r['items'].forEach(function(item) {
                    console.log(item)
                    html += '<li class="mdl-list__item mdl-list__item--three-line"> <span class="mdl-list__item-primary-content"> <i class="material-icons mdl-list__item-avatar">person</i> <span>'
                    html += item['user_name']
                    html += '</span> <span class="mdl-list__item-text-body">'
                    html += 'From. ' + item['company_name'] +'<br/> '+item['type']
                    html += '</span> </span> <span class="mdl-list__item-secondary-content"> <a data-user="'+item['user_id']+'" data-type="'+item['type']+'" class="show-modal mdl-list__item-secondary-action" href="#"><i class="material-icons">print</i></a> </span> </li>'
                })
                $('#history').html(html);
            },
            complete: function(r){
                //console.log(r)
            }
        })
    }
    load_data();
});
