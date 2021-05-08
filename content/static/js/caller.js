var SERVER_URL = "http://localhpst:8080/"

setInterval(getDoor, 200)

function getDoor() {
    callApi(SERVER_URL + "getDoor");
}

function callApi(url) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url);
    xhr.onload = function () {
        // レスポンスが返ってきた時の処理
      }
    xhr.send();
}