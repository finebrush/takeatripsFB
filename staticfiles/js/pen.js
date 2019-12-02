$(function () {
  var width = 80,
  height = 44 * 4,
  speed = 300,
  button = $('#menu-button'),
  overlay = $('#overlay'),
  menu = $('#hamburger-menu');

  button.on('click', function (e) {
    if (overlay.hasClass('open')) {
      animate_menu('close');
    } else {
      animate_menu('open');
    }
  });

  overlay.on('click', function (e) {
    if (overlay.hasClass('open')) {
      animate_menu('close');
    }
  });

  $('a[href="#"]').on('click', function (e) {
    e.preventDefault();
  });

  function animate_menu(menu_toggle) {
    if (menu_toggle == 'open') {
      overlay.addClass('open');
      button.addClass('on');
      overlay.animate({ opacity: 1 }, speed);
      menu.animate({ width: width, height: height }, speed);
    }

    if (menu_toggle == 'close') {
      button.removeClass('on');
      overlay.animate({ opacity: 0 }, speed);
      overlay.removeClass('open');
      menu.animate({ width: "0", height: 0 }, speed);
    }
  }

  //POI 말풍선안의 버튼 클릭시
  $('#openstreet-map').on('click', '.dialog__trigger', function() {
    // alert('Hello from seoul!!');

    //위치값 받아와서 다이얼로그 작성 후 같이 저장 되어야 함.

    $("#dialog").dialog({
      width: 900,
    });

  });

  $('#tiregister').on('click', function(){

    //다이얼로그 작성 한 후 저장 할때 위치값을 공백으로 넣고 이후 리스트에서 배치 할 때 위치값 저장 해야 함.
    
    $("#dialog").dialog({
      width: 900,
    });
  });

});
