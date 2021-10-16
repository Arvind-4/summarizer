document.getElementById('content').focus()
var content = document.getElementById('content').value
const copy = document.getElementById("copy-button")
const text = document.getElementById("result")
content.defaultValue = ''

function copy_all() {
    text.select()
    document.execCommand('copy')
    copy.innerHTML = 'Copied! <i class="fas fa-check-circle"></i>'
    window.getSelection().removeAllRanges()
}

function clear_all() {
    text.value = ''
}

function closeAlert(event) {
    let element = event.target;
    while (element.nodeName !== "BUTTON") {
        element = element.parentNode;
    }
    element.parentNode.parentNode.removeChild(element.parentNode);
}