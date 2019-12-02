
$(document).ready( function() {

    console.log($("#id_categorymedium"));

    // inline 그룹을 hide..
    if ($("#id_categorymedium option:selected").text() == "주점"){
        $("#tmpadd_set-group").show();
    }else {
        $("#tmpadd_set-group").hide();
    }

    // 콤보박스의 변화가 생기면 선택된 텍스트를 판별하여 이벤트 발생..
    $( "#id_categorymedium" ).change(function() {
        if ($("#id_categorymedium option:selected").text() == "주점"){
            $("#tmpadd_set-group").show();
        }else {
            $("#tmpadd_set-group").hide();
        }
        alert($("#id_categorymedium option:selected").text());
        // console.log($("#id_categorymedium option:selected").val());
    });

    $("input").click( function(event) {
        alert("You clicked the button using JQuery!");
    });
});
