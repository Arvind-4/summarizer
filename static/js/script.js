document.getElementById('content').focus()
var content = document.getElementById('content').value
content.defaultValue = ''
var final_content = content.replaceAll(' ', '')
content.innerHTML = final_content

const copy = document.getElementById("copy-button");
const selection = window.getSelection();
const range = document.createRange();
const text = document.getElementById("result")
var clear = document.getElementById('clear-button')


function disable_button() {
    if (text.value.length === 0) {
        clear.disabled = true
        copy.disabled = true
    } else {
        copy.onclick = function () {
            text.select()
            document.execCommand('copy')
            copy.innerText = 'copied!'
            window.getSelection().removeAllRanges()
        }
        clear.onclick = function () {
            console.log('Clear')
            text.value = ''
        }
    }
}

//
// document.getElementById('submit-button').addEventListener('click', function () {
//     document.onreadystatechange = function () {
//         if (document.readyState !== "complete") {
//             document.querySelector("body").style.visibility = "none";
//             document.querySelector("#loader").style.visibility = "none";
//         } else {
//             document.querySelector("#loader").style.display = "none";
//             document.querySelector("body").style.visibility = "none";
//         }
//     };
// })