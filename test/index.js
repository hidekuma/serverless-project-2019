$(document).ready(function(){
    //$('#fixed-tab-2').on('click', function(){
        $.ajax({
            url: 'https://epn2pajpf4.execute-api.ap-northeast-2.amazonaws.com/dev/conference?user_id=*',
            method: 'get',
            success: function(r){
                var html = '';
                r['items'].forEach(function(item) {
                    html += '<div  class="mdl-cell mdl-cell--4-col">'
                    html += '<div class="history-card-wide mdl-card mdl-shadow--2dp">'
                    html += '<div class="mdl-card__title" style="background: url(\'http://d21wnzpstszop8.cloudfront.net/qrcodes/'+item['user_id']+'/qrcode.jpg\') center / cover;">'
                    //html += '<div>'
                    //html += 'Serverless Web project'
                    html += '<h2 class="mdl-card__title-text">'+item['user_name']+'</h2>'
                    html += '</div>'
                    html += '<div class="mdl-card__supporting-text">'
                    html += item['company_name']
                    html += '소속 / '
                    html += item['user_name']
                    html += '님 : '
                    html += item['user_phone']
                    html += '</div>'
                    html += '<div class="mdl-card__menu">'
                    html += '<button class="mdl-button mdl-button--icon mdl-js-button mdl-js-ripple-effect">'
                    html += '<i class="material-icons">share</i>'
                    html += '</button>'
                    html += '</div>'
                    html += '</div>'
                    html += '</div>'
                })

                 $('#history').html(html);
            },
            fail: function(err){
                console.log('failed', err);
            },
            complete: function(r){
                console.log('completed', r);
            }
        //});
    });
    $('#submitButton').on('click', function(e){
        var user_id = $('#user_id').val();
        var user_name = $('#user_name').val();
        var user_phone = $('#user_phone').val();
        var company_name = $('#company_name').val();
        $.ajax({
            url: 'https://epn2pajpf4.execute-api.ap-northeast-2.amazonaws.com/dev/conference',
            method: 'post',
            datatype: 'json',
            async: true,
            data:JSON.stringify({
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
})
