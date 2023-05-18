function nextPage(pageNum, maxPage) {
    if (pageNum + 1 > maxPage)
        return

    var postData = encodeURIComponent('pageNum') + '=' + encodeURIComponent(pageNum + 1);

    const url = "http://localhost:8000/cgi-bin/main_page.py"
    let xhr = new XMLHttpRequest()

    xhr.open('POST', url, true)
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded; charset=UTF-8')
    xhr.send(postData);

    xhr.onload = function () {
        if(this.readyState == 4 && this.status == 200)
            document.body.innerHTML = this.response
    }
}

function prevPage(pageNum) {
    if (pageNum - 1 < 1)
        return

    var postData = encodeURIComponent('pageNum') + '=' + encodeURIComponent(pageNum - 1);

    const url = "http://localhost:8000/cgi-bin/main_page.py"
    let xhr = new XMLHttpRequest()

    xhr.open('POST', url, true)
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded; charset=UTF-8')
    xhr.send(postData);

    xhr.onload = function () {
        if(this.readyState == 4 && this.status == 200)
            document.body.innerHTML = this.response
    }


}


