// Ajax를 사용해 rest api 호출 시 csrftoken을 얻기 위해 사용한다.
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function() {
    // 네비게이션바에서 해당 메뉴를 활성화한다.
    $(".nav-link").eq(0).addClass("active");

    // 검색창에 키워드가 없으면 검색창 위치를 중간으로 변경한다.
    if ($("#input-keyword").val() == '') {
        $("#search-box").addClass("d-flex align-items-center h-50");
        $("#search-box").children().addClass("w-100");
    }

    // 화면 오픈 시 검색창에 커서를 이동시킨다.
    // 커서를 검색어 마지막에 위치시킨다.
    _keyword = $("#input-keyword").val();
    $("#input-keyword").focus();
    $("#input-keyword").val('').val(_keyword);

    // 검색버튼을 선택하면 검색을 수행한다.
    $("#search-img").click(function() {
        $("#frm-search").submit();
    });

    // 키워드 리스트 모달에서 키워드를 선택하면
    // 키워드를 검색창에 입력하고 키워드 리스트 모달을 닫는다.
    $(".btn-select-keyword").click(function() {
        $("#input-keyword").val($(this).data("keyword"));
        $("#keywordListModal").modal('hide');
    });

    // 언론사 관리하기 모달 언론사 정보를 입력한다.
    $("#siteEditModal").on('show.bs.modal', function(event) {
        var siteuri = $(event.relatedTarget).data('siteuri');
        var sitename = $(event.relatedTarget).data('sitename');
        var actionurl = $(event.relatedTarget).data('action-url');
        var actiontype = $(event.relatedTarget).data('action-type');

        $("#modal-siteuri").val(siteuri);
        $("#modal-sitedesc").val(sitename);
        $("#frmSiteEditModeal").attr("action", actionurl);

        // 언론사 정보가 존재하지 않을 경우 method를 POST로 설정하고
        // 언론사 정보가 존재할 경우 method를 PUT으로 설정한다.
        if (actiontype === 'create') {
            $("#frmSiteEditModeal").attr("method", "POST");
        } else if (actiontype === 'update') {
            $("#frmSiteEditModeal").attr("method", "PUT");
        }
    });

    // 언론사 관리하기 모달이 보여진 후 언론사명 입력란에 포커스를 옮긴다.
    $("#siteEditModal").on('shown.bs.modal', function(event) {
        $("#modal-sitedesc").focus();
    });

    // 언론사 관리하기 모달에서 저장 버튼 클릭 시 REST API를 호출한다.
    $("#btnSaveSiteEditModal").click(function() {
        const csrftoken = getCookie('csrftoken');

        let url = $("#frmSiteEditModeal").attr("action");
        let method = $("#frmSiteEditModeal").attr("method");

        let headers = {
            'X-CSRFToken': csrftoken
        }

        let data = {
            address: $("#modal-siteuri").val(),
            description: $("#modal-sitedesc").val()
        }

        $.ajax({
                method: method,
                url: url,
                headers: headers,
                data: data,
                dataType: "json"
            })
            .done(function() {
                $("#siteEditModal").modal('hide');
                $("#frm-search").submit();
            })
            .fail(function() {
                console.log("fail!")
            });
    });
});