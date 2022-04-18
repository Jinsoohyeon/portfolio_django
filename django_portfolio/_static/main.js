let nav_h = document.querySelector('nav#nav_bar').clientHeight
let con_h = document.querySelector('div#main_area').clientHeight
let fot_h = document.querySelector('footer').clientHeight
doc_h = nav_h + con_h + fot_h
console.log(nav_h, con_h, fot_h)
console.log(window.innerHeight)

if (doc_h >= window.innerHeight){
    document.querySelector('footer').classList.remove('fixed-bottom')
}

function searchPost(){
    let searchValue = document.getElementById('search-input').value.trim()
    if (searchValue.length > 1){
        location.href="/blog/search/" + searchValue + "/"
    }
    else {
        alert('두 글자 이상 입력해주세요.')
    }
}
document.getElementById('search-input').addEventListener('keyup', function(event){
    if(event.key === 'Enter'){
        searchPost()
    }
})