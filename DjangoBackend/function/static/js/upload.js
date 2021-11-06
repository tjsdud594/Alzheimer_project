function readURL(input) {
  if (input.files && input.files[0]) {
     // 인풋 태그에 파일이 있는 경우
    var reader = new FileReader();

    reader.onload = function(e) {
      $('.image-upload-wrap').hide();
      $('.file-upload-image').attr('src', e.target.result);//기본적으로 이미지에 대한 경로를 미리 세팅 이거 그대로 모델링 할거니 경로를 결과값으로 (base64)
      $('.file-upload-content').show();
    };

    reader.readAsDataURL(input.files[0]);

  } else {
    removeUpload();
  }
}

$('.image-upload-wrap').bind('dragover', function () {
  $('.image-upload-wrap').addClass('image-dropping');
});
$('.image-upload-wrap').bind('dragleave', function () {
  $('.image-upload-wrap').removeClass('image-dropping');
});

function removeUpload() {
  $('.file-upload-input').replaceWith($('.file-upload-input').clone());
  $('.file-upload-content').hide();
  $('.image-upload-wrap').show();
}
