$('#img').change(function () {
    let input = $(this)[0];
    if (input.files && input.files[0]) {
        if (input.files[0].type.match('image.*')) {
            let reader = new FileReader();
            reader.onload = function (e) {
                $('#img-preview').attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
            $('#img-preview').show();
            $('#up-img').height(318);
            $('#reset-img-preview').show();
            $('.download-btn').hide();
        } else {
            console.log('ошибка, не изображение');
        }
    } else {
        console.log('хьюстон у нас проблема');
    }
});

$('#reset-img-preview').click(function() {
    $('#img').val('');
    $('#up-img').height(135);
    $('#img-preview').hide()
    $('#reset-img-preview').hide()
    $('.download-btn').show();
});
