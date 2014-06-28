
function formatCodeSection(container) {
  var rawText = $(container).text();
  
  //Try to decipher which language is being used.
  var language = interpretLanguage(rawText); 

  var dirtyContent = rawText.split("\n");
  var cleanLines = [];
  var cleanLineNumbers = [];

  var linesUsed = 1;
  for (var i=0 ; i < dirtyContent.length ; i++) {
    var dirtyLineContent = dirtyContent[i].trim();
    var lineClasses = "codeLine";

    var lineNumber = "";
    if (dirtyLineContent[0]==">") {
      lineNumber = "<div class='returnLineNumber unselectable'>&nbsp;</div>";
      lineClasses += " returnLine";
    } else if (dirtyLineContent=="") {
      continue;
    } else {
      lineNumber = "<div class='lineNumber unselectable'>"+linesUsed+"</div>";
      linesUsed++;
    }

    var formattedContent = markLanguage(language, dirtyLineContent)
    var lineContent = "<span class='lineContent'>" +formattedContent+"</span>";


    cleanLineNumbers.push(lineNumber);
    cleanLines.push("<div class='"+lineClasses+"'>"+lineContent+"</div>");
  }

  var formattedContent = "<div class='lineNumberContainer'>"+
                           cleanLineNumbers.join(" ")+
                         "</div>" +
                         "<div class='lineContainer'>"+
                           cleanLines.join(" ")+
                         "</div>";

  $(container).html(formattedContent)
}


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

  $(container).find("a").each( function(i) {
    var randomIndex = Math.floor(Math.random()*lightColorOptions.length);
    $(this).css("color", darkColorOptions[randomIndex]);
    $(this).css("background-color", lightColorOptions[randomIndex]);
    $(this).html($(this).html().trim());
  });
}


$(document).on("ready", function() {
//# # # # # # # # # # # # # # # # # #

$(".codeSection").each(function(index){
  formatCodeSection($(this));
});


colorLinks("#contentContainer, .post-body");


//# # # # # # # # # # # # # # # # # #
});
