(function(){
  var xmlhttp;
  function loadXMLDoc(url,post){
      xmlhttp=null;
      if (window.XMLHttpRequest)
      {// code for Firefox, Mozilla, IE7, etc.
          xmlhttp=new XMLHttpRequest();
      }
      else if (window.ActiveXObject)
      {// code for IE6, IE5
          xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
      }
      if (xmlhttp!=null)
      {
          xmlhttp.onreadystatechange=state_Change;
          xmlhttp.open("POST",url,true);
          xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
          xmlhttp.send(post);
      }
      else
      {
          alert("Your browser does not support XMLHTTP.");
      }
  }

  function state_Change()
  {

    if (xmlhttp.readyState==4)
    {// 4 = "loaded"
        if (xmlhttp.status==200)
        {// 200 = "OK"
            document.getElementById('hotelList').innerHTML=xmlhttp.responseText;
            window.onload();
        }
        else
        {
            document.body.innerHTML = " " + xmlhttp.responseText;
        }
    }
  }

  var starHandle = document.getElementById("star");
  if(starHandle) {

    starHandle.onclick = function(){
        var url = "sortHotels/star";
        var post =  "city="+document.getElementById("city").value + "&checkin=" + document.getElementById("checkin").value + "&checkout="+ document.getElementById("checkout").value;
        loadXMLDoc(url,post);

    }
  }
  var nameHandle = document.getElementById("name");
  if(nameHandle) {
    nameHandle.onclick = function(){
        var url = "sortHotels/name";
        var post =  "city="+document.getElementById("city").value + "&checkin=" + document.getElementById("checkin").value + "&checkout="+ document.getElementById("checkout").value;
        loadXMLDoc(url,post);
    }
  }
})();