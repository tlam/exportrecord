$(document).ready(function() {
    $("tr:odd").css("background-color", "#EDF3FE");

    $("a#advanced-search").click(function(e) {
        $("div#select-columns").toggle("slow");
        e.preventDefault();
    });
});
