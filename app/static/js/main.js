let down = "/static/audio/pop-down.mp3"
let check = "/static/audio/pop-up-on.mp3"
let uncheck = "/static/audio/pop-up-off.mp3"

let apiStorage = localStorage.getItem('fav_api')

if (apiStorage) {

    const ul = document.querySelector(".bookmarks");
    let apis = JSON.parse(apiStorage)
    apis.forEach(api => {


        let temp = ` 
            <button class="remove-btn">×</button>
            <a href="${api.Link}" target="_blank"> 
            <img src="${api.ImageURL}" alt="">
            <span>${api.API}</span>
            </a> 
            `
        let newLiElement = document.createElement('li');
        newLiElement.classList.add("bookmark")
        newLiElement.innerHTML = temp
        ul.appendChild(newLiElement)
        newLiElement.querySelector('button').addEventListener("click", (e) => {
            let parent = e.target.parentElement;
            let apiText = parent.querySelector('span').innerText;
            let apis = JSON.parse(apiStorage)
            let index = apis.findIndex(x => x.API === apiText)
            apis.splice(index, 1)
            localStorage.setItem('fav_api', JSON.stringify(apis))
            parent.classList.add('gesture-animation-out');
            parent.addEventListener('animationend', () => {
                let sibling = parent.nextElementSibling;
                let popout = "/static/audio/trash.wav"
                let audio = new Audio(popout);
                audio.play();
                parent.remove();

                if (sibling) {
                    sibling.classList.add('gesture-animation');
                }
            })


        })
    });
}



let checkbox = document.getElementById('checkbox');
const label = document.querySelector('label[for="checkbox"]');

function playSound(soundName) {
    const audio = new Audio(`${soundName}`);
    audio.volume = 0.2;
    audio.play();
}

label.addEventListener('mousedown', () => {
    playSound(down)
});

label.addEventListener('mouseup', () => {
    checkbox.checked ? playSound(uncheck) : playSound(check)

});

document.body.addEventListener('htmx:afterSwap', function(event) {
    var targetElement = event.detail.target;
    if (targetElement.id === 'status-checking') {
        targetElement.classList.remove('anim');
        let parent = document.getElementById('result')
        let r = event.detail.xhr.responseText;
        parent.classList.remove('anim');
        if (r.includes("done")) {
            parent.classList.add('alive');
        } else {
            parent.classList.add('dead');
        }
    }
});