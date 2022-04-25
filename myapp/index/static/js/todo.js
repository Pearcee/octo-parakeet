const requestUrl = "http://127.0.0.1:8000/api/todo";



// fetch(requestUrl)
//     .then(response => response.json())
//     // .then(y => document.getElementById("demo").innerHTML = y)
//     .then(data => console.log(data));

async function getUsers() {
    let url = requestUrl;
    try {
        let res = await fetch(url);
        return await res.json();
    } catch (error) {
        console.log(error);
    }
}

async function renderUsers() {
    let users = await getUsers();
    let html = '';
    users.forEach(user => {
        let htmlSegment = `<div class="user">
                            <h2>${user.title} </h2>
                        </div>`;

        html += htmlSegment;
    });

    let container = document.querySelector('.container');
    container.innerHTML = html;
}

renderUsers();    