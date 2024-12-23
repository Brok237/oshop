document.getElementById("signupform").onsubmit = function(e) { // lma 23ml submit fe 2l sign up  h48l function 2ab3tlha event object 2llhwa fe 2l hala dh submit
    e.preventDefault(); // Prevent form from submitting normally

    const formData = new FormData(document.getElementById("signupform"));  //h5zn 2ldata mn 2l html mn 2lform kolha ya3ny
    fetch('/signup', {// h48l wl sign up api mn 2lflask
        method: 'POST',
        body: formData // 2ldata 2ll flask hya5odha
    })
    .then(response => {// law 3mlt fetch  yb2a dh hy4t8l
        return response.json();  //(twadeeeny 3la shahd)
    })
    .then(data => { 
        if (data.success) {// 2l data hya 2l response mn 2llfat law 24t8l
            window.location.href = "/";  //wadeeny 3la sign in
        } else {// law l2 23mly alert 2no feeh error
            alert(data.message); 
        }
    })
   
};

function getCookie(name) {
    let cookies = document.cookie.split('; ');
    for (let cookie of cookies) {
        let [key, value] = cookie.split('=');
        if (key === name) {
            return value;
        }
    }
    return null; 
}

window.onload = function () {
    let savedEmail = getCookie("email");
    if (savedEmail) {
        document.getElementById("email").value = savedEmail;
        
    }
};

document.getElementById("sign-in-form").onsubmit = function (e) {//nafs 2lklam 2llfo2 bs hroo7 3la 2l home
    e.preventDefault(); // Prevent default form submission

    const formData = new FormData(document.getElementById("sign-in-form"));
    
    fetch('/', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        return response.json(); 
    })
    .then(data => { 
        if (data.success) {
            return response.json();
        } else {
            alert(data.message); 
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert("Something went wrong. Please try again later.");
    });
};
