document.getElementById("addform").onsubmit = function (e) {
    e.preventDefault();

    const type = document.getElementById("type").value;
    const name = document.getElementById("name").value;  
    const desc = document.getElementById("desc").value;  
    const price = document.getElementById("price").value;
    const imgFile = document.getElementById("img").files[0];

    

    if (!type || !name || !price || !desc || !imgFile) {
        alert("Please fill in all fields.");
        return;
    }

    const formData = new FormData();
    formData.append("type", type);
    formData.append("name", name);
    formData.append("price", price);
    formData.append("description", desc);
    formData.append("img", imgFile);

    fetch("/add", {
        method: "POST",
        body: formData,
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            alert("an error ocured");
        }
    })
    .then(data => {
        alert("Product added successfully!");
        console.log(data);  
    })
    
};
