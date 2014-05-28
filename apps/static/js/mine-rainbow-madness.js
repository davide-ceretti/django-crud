function change_colours() {
    $('.rainbow-madness-random-color').each(function(i, obj) {
        var hue = 'rgb('
            + (Math.floor(Math.random() * 256)) + ','
            + (Math.floor(Math.random() * 256)) + ','
            + (Math.floor(Math.random() * 256)) + ')';
         $(this).css("color", hue);
    });
}

$(function() {
    $('.rainbow-madness').each(function(i, obj) {
        letters = $(this).text().split('');
        $(this).text('');
        for(var i = 0; i < letters.length; i++) {
            $(this).append('<span class="rainbow-madness-random-color">' + letters[i] + '</span>');
        }
    });

    change_colours();
    $(document).ready(function() {
        setInterval( "change_colours()", 50 );
    });

});