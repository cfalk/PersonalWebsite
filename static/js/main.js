
function formatCodeSection(container) {
  var language = "javascript"; //TODO:Abstract this to parse contents and estimate.
  var dirtyContent = $(container).text().split("\n");
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

$(document).on("ready", function() {
//# # # # # # # # # # # # # # # # # #

$(".codeSection").each(function(index){
  formatCodeSection($(this));
});

//# # # # # # # # # # # # # # # # # #
});
