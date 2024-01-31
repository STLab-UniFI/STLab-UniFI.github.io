---
layout: page
title: Our publications
---
<div id="load"></div>

<script>
document.onreadystatechange = function () {
  var state = document.readyState
  if (state == 'interactive') {
       document.getElementById('contents').style.visibility="hidden";
  } else if (state == 'complete') {
      setTimeout(function(){
         document.getElementById('interactive');
         document.getElementById('load').style.visibility="hidden";
         document.getElementById('contents').style.visibility="visible";
      },0);
  }
}
</script> 

<script src="https://bibbase.org/show?bib=https%3A%2F%2Fbibbase.org%2Fnetwork%2Ffiles%2FAckLME82Ptjq8qnmm&noBootstrap=1&jsonp=1"></script>
