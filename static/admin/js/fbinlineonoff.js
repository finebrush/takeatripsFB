
$(document).ready( function() {
    
    // $("#id_categorysmall option").filter(function() {
    //     // console.log($(this).attr('value'));
    //     if($(this).attr('selected')){
    //         console.log("ok!");
    //     }
    //     // return $(this).attr('value') == '107';
    // })//.attr('selected', true);

    // console.log($("#id_part"));
    // console.log($("#id_categorysmall")[0].attributes[5]);
    // console.log($("#id_categorysmall")[0].options);
    // console.log($("#id_categorysmall")[0].options[$("#id_categorysmall")[0].options.selectedIndex].text);
    // console.log($("#id_categorysmall")[0].selectedOptions);
    
    // $("#id_categorysmall option").filter(function(){
    //     if($(this).attr('selected')){
    //         console.log($(this).attr('value'));
    //         return $(this).attr('value');
    //     }
    // }).attr('selected', true);

    if (document.getElementById("id_part")){

        var sel = document.getElementById("id_part");

        // inline 그룹을 hide..
        switch (sel.value) {
            case "Eat":
                $("#eatdrinkpart-group").show();
                $("#funpart-group").hide();
                $("#seepart-group").hide();
                $("#sleeppart-group").hide();
                $("#buypart-group").hide();
                break;
            case "Drink":
                $("#eatdrinkpart-group").show();
                $("#funpart-group").hide();
                $("#seepart-group").hide();
                $("#sleeppart-group").hide();
                $("#buypart-group").hide();
                break;
            case "Fun":
                $("#eatdrinkpart-group").hide();
                $("#funpart-group").show();
                $("#seepart-group").hide();
                $("#sleeppart-group").hide();
                $("#buypart-group").hide();
                break;
            case "See":
                $("#eatdrinkpart-group").hide();
                $("#funpart-group").hide();
                $("#seepart-group").show();
                $("#sleeppart-group").hide();
                $("#buypart-group").hide();
                break;
            case "Sleep":
                $("#eatdrinkpart-group").hide();
                $("#funpart-group").hide();
                $("#seepart-group").hide();
                $("#sleeppart-group").show();
                $("#buypart-group").hide();
                break;
            case "Buy":
                $("#eatdrinkpart-group").hide();
                $("#funpart-group").hide();
                $("#seepart-group").hide();
                $("#sleeppart-group").hide();
                $("#buypart-group").show();
                break;
            default:
                $("#eatdrinkpart-group").hide();
                $("#funpart-group").hide();
                $("#seepart-group").hide();
                $("#sleeppart-group").hide();
                $("#buypart-group").hide();
                break;
        }
        
        // 콤보박스의 변화가 생기면 선택된 텍스트를 판별하여 이벤트 발생..
        $( "#id_part" ).change(function() {
            // console.log(sel.value);
            switch (sel.value) {
                case "Eat":
                    $("#eatdrinkpart-group").show();
                    $("#funpart-group").hide();
                    $("#seepart-group").hide();
                    $("#sleeppart-group").hide();
                    $("#buypart-group").hide();
                    break;
                case "Drink":
                    $("#eatdrinkpart-group").show();
                    $("#funpart-group").hide();
                    $("#seepart-group").hide();
                    $("#sleeppart-group").hide();
                    $("#buypart-group").hide();
                    break;
                case "Fun":
                    $("#eatdrinkpart-group").hide();
                    $("#funpart-group").show();
                    $("#seepart-group").hide();
                    $("#sleeppart-group").hide();
                    $("#buypart-group").hide();
                    break;
                case "See":
                    $("#eatdrinkpart-group").hide();
                    $("#funpart-group").hide();
                    $("#seepart-group").show();
                    $("#sleeppart-group").hide();
                    $("#buypart-group").hide();
                    break;
                case "Sleep":
                    $("#eatdrinkpart-group").hide();
                    $("#funpart-group").hide();
                    $("#seepart-group").hide();
                    $("#sleeppart-group").show();
                    $("#buypart-group").hide();
                    break;
                case "Buy":
                    $("#eatdrinkpart-group").hide();
                    $("#funpart-group").hide();
                    $("#seepart-group").hide();
                    $("#sleeppart-group").hide();
                    $("#buypart-group").show();
                    break;
                default:
                    $("#eatdrinkpart-group").hide();
                    $("#funpart-group").hide();
                    $("#seepart-group").hide();
                    $("#sleeppart-group").hide();
                    $("#buypart-group").hide();
                    break;
            }
            // if ($("#id_part option:selected").text() == "먹다/마시다"){
            //     $("#eatdrinkpart-group").show();
            // }else {
            //     $("#eatdrinkpart-group").hide();
            // }
            // alert($("#id_part option:selected").text());
            // console.log($("#id_part option:selected").val());
        });

        // $("input").click( function(event) {
        //     alert("You clicked the button using JQuery!");
        // });
    }
});
