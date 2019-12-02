function imgupload(){
    //event.preventDefault();
    //var post_url = $(this).attr("action");
    //var form = $('#FILE_FORM')[0]; //form 의 입력 되는 데이터 가져옴
    var form_data = new FormData(); //가져온 데이터를 FormData로 만들어줌

    form_data.append("image",$("#bs_theimg")[0].files[0]);
    form_data.append("title",$("#bs_thename")[0].value);
    form_data.append("description",$("#bs_title")[0].value);

    console.log(form_data);
    console.log($("#bs_thename")[0].value);
    console.log($("#bs_theimg")[0].files[0]); // C:\fakepath\bg.jpg
    // console.log($("#bs_theimg")[0].value); // C:\fakepath\bg.jpg
    console.log($("#bs_title")[0].value);
    // console.log($("#bs_writer")[0].value);

    var settings = {
          "async": true,
          "crossDomain": true,
          "url": "http://13.125.244.56:8000/api/upload/",
          "method": "POST",
          "headers": {
            "cache-control": "no-cache",
            "postman-token": "fd08c0b2-db76-8ec4-9447-8e49f0cce2c5"
          },
          "contentType": "multipart/form-data",
          "dataType": 'json',
          "processData": false,
          "data": form_data
          //"data": JSON.stringify({'bs_thename':$('#bs_thename').val(),'bs_theimg':$('#bs_theimg').val(),'bs_title':$('#bs_title').val(),'bs_writer':$('#bs_writer').val()})
      }

    $.ajax(settings).done(function (response) {
      console.log("들어옴!");
      console.log(response);
      //alert('메모 저장 완료');
    });
}

function sendinfo() {
  var request = new XMLHttpRequest();
  var formData = new FormData();

  // POST to httpbin which returns the POST data as JSON
  request.open('POST', 'http://13.125.244.56:8000/api/images/', /* async = */ false);
  request.setRequestHeader("X-CSRF-TOKEN", "${_csrf.token}");

  formData.append("bs_thename",$("#bs_thename")[0].value);
  formData.append("bs_theimg",$("#bs_theimg")[0].files[0]);
  formData.append("bs_title",$("#bs_title")[0].value);
  formData.append("bs_writer",$("#bs_writer")[0].value);
  //sub_imagesA~F 로 하는 이유는 서버에서 각기 저장을 하기 위해
  formData.append("sub_imagesA",$("#bs_image1")[0].files[0]);
  formData.append("sub_imagesB",$("#bs_image2")[0].files[0]);
  formData.append("sub_imagesC",$("#bs_image3")[0].files[0]);
  formData.append("sub_imagesD",$("#bs_image4")[0].files[0]);
  formData.append("sub_imagesE",$("#bs_image5")[0].files[0]);
  formData.append("sub_imagesF",$("#bs_image6")[0].files[0]);

  console.log(formData);
  console.log(formData.getAll('sub_images'));
  request.onload = function() {
    if (request.status === 200 || request.status === 201) {
      console.log(request.responseText);
    } else {
      console.error(request.responseText);
    }
  };
  request.send(formData);

  //필드 초기화
  $("#fileName")[0].value = "파일선택";
  $("#bs_thename")[0].value = "";
  $("#bs_title")[0].value = "";
  $("#bs_writer")[0].value = "";

  for(var i = 1; i <= 6 ; i++){
    var $label = $("#bs_image"+i).next('label'),
        $labelText = $label.find('span');
        //labelDefault = $labelText.text();
    $label.removeClass('file-ok');
    $label.removeAttr('style');
    $labelText.text('Select Image One');
  }

  alert(" 업로드 완료 ");
};

function sendaxios() {
  var formData = new FormData();

  formData.append("bs_thename",$("#bs_thename")[0].value);
  formData.append("bs_theimg",$("#bs_theimg")[0].files[0]);
  formData.append("bs_title",$("#bs_title")[0].value);
  formData.append("bs_writer",$("#bs_writer")[0].value);
  //sub_imagesA~F 로 하는 이유는 서버에서 각기 저장을 하기 위해
  formData.append("sub_imagesA",$("#bs_image1")[0].files[0]);
  formData.append("sub_imagesB",$("#bs_image2")[0].files[0]);
  formData.append("sub_imagesC",$("#bs_image3")[0].files[0]);
  formData.append("sub_imagesD",$("#bs_image4")[0].files[0]);
  formData.append("sub_imagesE",$("#bs_image5")[0].files[0]);
  formData.append("sub_imagesF",$("#bs_image6")[0].files[0]);

  console.log(formData);
  console.log(formData.getAll('sub_images'));

  //axios post
  axios.post('http://13.125.244.56:8000/api/images/', formData)
      .then(function (res) {
          console.log("axios post..", res);
      })
      .catch(function (err) {
          console.log("POST ERR", err)
      });

  //필드 초기화
  $("#fileName")[0].value = "파일선택";
  $("#bs_thename")[0].value = "";
  $("#bs_title")[0].value = "";
  $("#bs_writer")[0].value = "";

  for(var i = 1; i <= 6 ; i++){
    var $label = $("#bs_image"+i).next('label'),
        $labelText = $label.find('span');
        //labelDefault = $labelText.text();
    $label.removeClass('file-ok');
    $label.removeAttr('style');
    $labelText.text('Select Image One');
  }

  alert(" 업로드 완료 ");
}

function readURL(input) {
    //console.log("버튼클릭함1");
    if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function (e) {
            //$('#cover').attr('src', e.target.result);        //cover src로 붙여지고
            $('#fileName').val(input.files[0].name);    //파일선택 form으로 파일명이 들어온다
        }
      reader.readAsDataURL(input.files[0]);
    }
}

$("#bs_theimg").change(function(){
    readURL(this);
    //console.log("이미지 바뀜?");
});

$("#bs_preimg").click(function(){
  console.log("미리보기 눌림!");
});


$(document).ready(function(){
  function readURL(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function(e) {
   			$(input).parent().next().attr("src",e.target.result);
      }
      reader.readAsDataURL(input.files[0]);
    }
  }

  	$(".dosyasec").change(function() {
  		readURL(this);
  	});
});
