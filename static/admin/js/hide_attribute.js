hide_page=false;
django.jQuery(document).ready(function(){
    if (django.jQuery('#id_has_submenu').is(':checked')) {
        django.jQuery(".tmptest").hide();
        hide_page=true;
    } else {
        django.jQuery(".tmptest").show();
        hide_page=false;
    }
    django.jQuery("#id_has_submenu").click(function(){
        hide_page=!hide_page;
        if (hide_page) {
            django.jQuery(".tmptest").hide();
        } else {
            django.jQuery(".tmptest").show();
        }
    })
})
