function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function setCookie(cname, cvalue, exminutes) {
    var d = new Date();
    d.setTime(d.getTime() + (exminutes * 60 * 1000));
    var expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

let visited = getCookie("visited");

if (visited) {
    $("#preloader-active").remove();
    $("#main-content").removeClass('blur-backgroud');
    $(".mobile-nav-toggle").removeClass('blur-backgroud');
    console.log("visited");
} else {
    console.log("fist time");
}

$(window).on('load', function () {
    $('#preloader-active').delay(100).fadeOut('slow');
    $("#main-content").delay(100).removeClass('blur-backgroud');
    $(".mobile-nav-toggle").delay(100).removeClass('blur-backgroud');
    $('body').delay(100).css({
        'overflow': 'visible'
    });
    setCookie("visited", true, 5);    
});