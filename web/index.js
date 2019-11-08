$(document).ready(function(){
    var ENDPOINT = 'https://epn2pajpf4.execute-api.ap-northeast-2.amazonaws.com/dev/conference'
    var CF = 'https://d21wnzpstszop8.cloudfront.net'
    var dialog = document.querySelector('dialog');
    var showModalButton = $('.show-modal');
    if (! dialog.showModal) {
        dialogPolyfill.registerDialog(dialog);
    }
    $(document).on('click', '.show-modal', function(e) {
        e.preventDefault();
        var user = $(this).data('user');
        var type = $(this).data('type');
        $('#showImg').html('<img style="width:100%" src="'+CF+'/qrcodes/'+user+'/'+type+'/qrcode.jpg"/>');
        dialog.showModal();
    });
    dialog.querySelector('.close').addEventListener('click', function() {
        dialog.close();
    });
    dialog.querySelector('.print').addEventListener('click', function() {
        print();
    });
    function load_data(){
        $.ajax({
            url: ENDPOINT +'?user_id=*',
            method: 'get',
            success: function(r){
                var html = '';
                html += '<ul class="demo-list-three mdl-list mdl-cell mdl-cell--4-col">'
                r['items'].forEach(function(item) {
                    html += '<li class="mdl-list__item mdl-list__item--three-line"> <span class="mdl-list__item-primary-content"> <i class="material-icons mdl-list__item-avatar">person</i> <span>'
                    html += item['user_name']
                    html += '</span> <span class="mdl-list__item-text-body">'
                    html += 'From. ' + item['company_name'] +'<br/> '+item['type']
                    html += '</span> </span> <span class="mdl-list__item-secondary-content"> <a data-user="'+item['user_id']+'" data-type="'+item['type']+'" class="show-modal mdl-list__item-secondary-action" href="#"><i class="material-icons">print</i></a> </span> </li>'
                })
                html += '</ul>'
                $('#history').html(html);
            },
            fail: function(err){
                console.log('failed', err);
            },
            complete: function(r){
                console.log('completed', r);
            }
        });
    }
    $('#submitButton').on('click', function(e){
        var user_id = $('#user_id').val();
        var type = $('#type').val();
        var user_name = $('#user_name').val();
        var user_phone = $('#user_phone').val();
        var company_name = $('#company_name').val();
        $.ajax({
            url: ENDPOINT,
            method: 'post',
            datatype: 'json',
            async: true,
            data:JSON.stringify({
                type: type,
                user_id: user_id,
                user_name: user_name,
                user_phone: user_phone,
                company_name: company_name
            }),
            beforeSend: function(){
                $('#p2').show();
            },
            success: function(r){
                console.log('success', r);
            },
            fail: function(err){
                console.log('failed', err);
                alert('failed! reloading...')
            },
            complete: function(r){
                console.log('completed', r);
                setTimeout(function() {
                    $('#p2').hide();
                    location.reload();
                }, 1000);
            }
        });
    });
    load_data();
})
