document.getElementById('content').focus()
var content = document.getElementById('content').value
const copy = document.getElementById("copy-button")
const text = document.getElementById("result")
content.defaultValue = ''

function copy_all() {
    text.select()
    document.execCommand('copy')
    copy.innerText = 'copied!'
    window.getSelection().removeAllRanges()
}

function clear_all() {
    text.value = ''
}