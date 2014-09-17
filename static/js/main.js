function colorLinks(container) {
  var darkColorOptions = [
    "#178766",
    "#C05402",
    "#4E4A8C",
    "#C51671",
    "#4B7916",
    "#B18202",
    "#A5311D",
    "#751DA5",
    "#004D99"
  ]
  var lightColorOptions = [
    "rgba(179,226,205,0.3)",
    "rgba(253,205,172,0.3)",
    "rgba(203,213,232,0.3)",
    "rgba(244,202,228,0.3)",
    "rgba(230,245,201,0.3)",
    "rgba(255,242,174,0.3)",
    "rgba(227,114,95,0.3)",
    "rgba(191,116,231,0.3)",
    "rgba(77,166,255,0.3)",
  ]

  $(container).find("a:not(.marky-linkToCode)").filter( function() {
    return $(this).children("img").length==0;
  })
    .each( function(i) {
      var randomIndex = Math.floor(Math.random()*lightColorOptions.length);
      $(this).css("color", darkColorOptions[randomIndex]);
      if (!$(this).hasClass("noBackgroundColor")) {
        $(this).css("background-color", lightColorOptions[randomIndex]);
      }
      $(this).html($(this).html().trim());
  });
}


$(document).on("ready", function() {
  colorLinks("#contentContainer, .post-body");
});
