function applyMarker(marker, token){
  return "<span class='"+marker+"'>"+token+"</span>";
}


function markJavaScript(text){
  var keywords = ["var", "new", "function", "RegExp", "continue",
                  "undefined", "null"];
  var bools = ["true", "false"];
  var operators = ["+","-","*","/","=","==", "<", ">"];
  var syntax = ["[","]","{","}","(",")",";", ",", "."];

  var formattedText = "";
  var token = "";
  var inString = false;
  var inComment = false;
  var escaped = false;

  for (var i=0 ; i < text.length ; i++){
    var c = text[i];
    var potential = token+c;

    //Escaped Characters.
    if (escaped && c!="\\") {
      escaped = false;
      formattedText += applyMarker("token-escaped", potential);
      token = "";
      continue;
    }
    if (c=="\\" && token[token.length-1]!="\\") escaped = true;

    if (inComment) {
      if (c=="\n"){
        formattedText += applyMarker("token-comment", potential);
        inComment = false;
        continue;
      }
      token += c;
      continue
    }

    if (inString && !escaped && c=="\""){
      formattedText += applyMarker("token-string", potential);
      token="";
      inString=false;
      continue;
    }

    if (!inString && c=="\"") inString=true;

    if (!inString && syntax.indexOf(c)>=0) {
      formattedText += markJavaScript(token);
      formattedText += applyMarker("token-syntax", c);
      token = "";
      continue;
    }

    if (token=="//") inComment = true;


    //Check for Keywords.
    if (keywords.indexOf(potential)<0 && keywords.indexOf(token)>=0){
      formattedText += applyMarker("token-keyword", token);
      token="";
    }

    //Check for Booleans.
    if (bools.indexOf(potential)<0 && bools.indexOf(token)>=0){
      formattedText += applyMarker("token-bool", token);
      token="";
    }

    //Check for Operators.
    if (operators.indexOf(potential)<0 && operators.indexOf(token)>=0){
      formattedText += applyMarker("token-operator", token);
      token="";
    }

    //Check for Identifiers.
    if (token!="" && c==" " && !inString && !inComment){
      formattedText += applyMarker("token-identifier", potential);
      token="";
      continue;
    }

    //Preserve Whitespace.
    if (token=="" && c==" ") {
      formattedText += " ";
      continue
    }

    token += c;
  }

  if (token.length){
    var marker="token-identifier";
    if (inComment) marker = "token-comment";
    if (keywords.indexOf(token)>=0) marker="token-keyword";
    if (operators.indexOf(token)>=0) marker="token-operator";
    if (bools.indexOf(token)>=0) marker="token-bool";
    formattedText += applyMarker(marker, token);
  }

  return formattedText;
}



function markLanguage(language, text){

  switch(language.toLowerCase()){
    case "javascript":
      return markJavaScript(text);

    default:
      throw "Language unknown to markLanguage function!";
  }

}
