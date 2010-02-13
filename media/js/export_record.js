$(document).ready(function() {
    $("tr:odd").css("background-color", "#EDF3FE");

    $("a#display-columns").click(function(e) {
        $("div#select-columns").toggle("slow");
        $("th").toggle();
        $("td").toggle();
        e.preventDefault();
    });

    $(".column-display").click(function(e) {
        var name = "." + $(this).attr("name");
        $("th" + name).toggle();
        $("td" + name).toggle();
    });
});
