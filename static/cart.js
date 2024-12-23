document.addEventListener("DOMContentLoaded", function() {
    const deleteButtons = document.querySelectorAll('.delete-item');// hselect kl 2l buttons 2l id bta3ha delet
    
    deleteButtons.forEach(button => { // h3ml function lkl button mwa7da ya3ny leehm
        button.addEventListener('click', function() {
            const productId = this.getAttribute('data-product-id');// ha5ed 2l attribute 2l 2smo id mno 
            const button = this; // 2l button bysawy 2lldost 3aleh
            
            
            button.disabled = true; //h3mlo myanf34 ytdas 3leeh 34an law 5d w2t 2no y3ml delete my3rf4 ydos tany
            

            fetch('/cart', {// hst5dm function 2l delete bta3t 2l cart
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json' // hb3t request no3ha json
                },
                body: JSON.stringify({ product_id: productId })// hb3t 2l id 3la 4kl json
            })
            .then(response => response.json())
            .then(data => {// law 3mlt fetch  ha4eel b2a 2l item mn 2odamy
                button.disabled = false;
                button.textContent = "Delete";  
                
                if (data.success) {
                    
                    this.closest('.cart-item').remove();// closest m3naha 22rb   tag lldelete 2llhwa fe 2l 7ala dh 2l container 2ll 4ael 2l product fhms70
                } else {
                    alert(data.message);
                }
            })
           
        });
    });
});
document.getElementById("checkout").onclick = function() {// function t3mly checkout  wtms7 2l cart kolha
    fetch("/checkout", { method: "GET" })
        .then(response => response.text())  
        .then(data => {
            
            document.body.innerHTML = data; // y5ly 2l current page btsawy 2l page 2ll3ayez 23rdha fe 2l 7ala dh hya 2l checkout page
        });
        
};
