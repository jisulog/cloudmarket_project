// 검색
$(document).ready(function () {
  $(".page-link").on('click', function () {
      $("#page").val($(this).data("page"));
      $("#searchForm").submit();
  });

  $("#btn_search").on('click', function () {
      $("#kw").val($(".kw").val());
      $("#page").val(1);  // 검색버튼을 클릭할 경우 1페이지부터 조회한다.
      $("#searchForm").submit();
  });
});

// 댓글
$(document).ready(function (){ $("[id^=button1]").click(
  function (e){ 
      var target = $(e.target);
      target.parent().parent().toggle();
      target.parent().parent().next().toggle();
      // $("[id^=divToggle2]").toggle(); 
      // $("[id^=divToggle1]").toggle(); 
  }); 
});
$(document).ready(function (){ $("[id^=button2]").click(
  function (e){    
      var target = $(e.target);
      target.parent().parent().parent().toggle();
      target.parent().parent().parent().prev().toggle();
      // $("[id^=divToggle1]").toggle();
      // $("[id^=divToggle2]").toggle(); 
  });
});