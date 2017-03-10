$(document).ready(function(){

  document.getElementById("search").addEventListener("click", function(event) {
    event.preventDefault();
    // console.log("remarks", "preventDefault");
    var date = $('#date').val();
    var url = "http://api.fixer.io/" + date;
    //alert(url);
    /*$.getJSON(url, function(data) {
      var items = [];
      $.each(data.rates, function(key, val) {
        items.push( "<tr><td>" + key + "</td><td>" + val + "</td></tr>" );
      });
      //$("<table/>"), {html: items.join("")}).appendTo("body");
      $('#currencies').html(items);
    });*/
    $.ajax({
     url: url,
     dataType: "jsonp",
     jsonpCallback: "data",
     success: function(data) {
       var items = [];
       $.each(data.rates, function(key, val) {
         items.push( "<tr><td>" + key + "</td><td>" + val + "</td></tr>" );
       });
       $('#currencies').html(items);
     },
     error: function(){ alert('fail'); }
   });
  });

});
