import os # hst5dmha 23an 2l path bta3 2l imgs
from werkzeug.utils import secure_filename # hst5dmha 34an 2 secure 2l name bta3 2lsoora
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session # session 34an btb2a 48ala 3la kolo 2l pages ft7afez 3la  user bta3y

bp = Blueprint('pages', __name__, template_folder="board/template")

UPLOAD_FOLDER = os.path.join('board\static', 'uploads')  # 2l path bta3 2l folder
if not os.path.exists(UPLOAD_FOLDER): # law m4 mawgood 23mly wa7ed tany
    os.makedirs(UPLOAD_FOLDER)

#our users list contains  user data and if the user is admin or not by default there is only one admin
users_db = [
    {"id": 1, "name": "mohamed", "email": "42310@gmail.com", "password": "as", "is_admin": True, "cart": []},
]
#our products data it's a dictionry of dictionry of list
products = {
    "Clothing": {
        "name": "Clothing",
        "img": "clothes_category.jpg",
        "items": [
            {"id": 1, "name": "Eye glasses", "description": "Eye glasses are not only functional but also a style statement.", "img": "eyeglasses.jpg", "price": 25.99},
            {"id": 2, "name": "T-shirt", "description": "A comfortable and versatile piece of clothing suitable for casual wear.", "img": "t-shirt.jpg", "price": 15.49},
            {"id": 3, "name": "Jeans", "description": "A classic denim pant that is a staple in many wardrobes.", "img": "jeans.jpg", "price": 45.99},
            {"id": 4, "name": "Sweater", "description": "Warm and cozy sweater perfect for colder days.", "img": "sweater.jpg", "price": 39.99},
            {"id": 5, "name": "Jacket", "description": "Stylish jacket that adds a layer of warmth and fashion.", "img": "jacket.jpg", "price": 89.99}
        ]
    },
    "Electronics": {
        "name": "Electronics",
        "img": "electronics_category.jpg",
        "items": [
            {"id": 100, "name": "Laptop", "description": "Powerful laptop for work and entertainment.", "img": "laptop.jpg", "price": 899.99},
            {"id": 101, "name": "Smartphone", "description": "Latest smartphone with advanced features.", "img": "smartphone.jpg", "price": 699.99},
            {"id": 102, "name": "Headphones", "description": "High-quality headphones for music and calls.", "img": "headphones.jpg", "price": 199.99},
            {"id": 103, "name": "Smartwatch", "description": "Stylish smartwatch with fitness tracking features.", "img": "smartwatch.jpg", "price": 199.99},
            {"id": 104, "name": "Tablet", "description": "Versatile tablet for work and play.", "img": "tablet.jpg", "price": 299.99}
        ]
    },
    "Books": {
        "name": "Books",
        "img": "books_category.jpg",
        "items": [
            {"id": 200, "name": "The Lord of the Rings", "description": "Epic fantasy novel by J.R.R. Tolkien.", "img": "lord_of_the_rings.jpg", "price": 29.99},
            {"id": 201, "name": "To Kill a Mockingbird", "description": "Classic novel by Harper Lee.", "img": "to_kill_a_mockingbird.jpg", "price": 18.99},
            {"id": 202, "name": "The Alchemist", "description": "Inspirational novel by Paulo Coelho.", "img": "the_alchemist.jpg", "price": 14.99},
            {"id": 203, "name": "Vampire diaries", "description": "created by American author L. J. Smith.", "img": "the_vampire_diaries.jpg", "price": 19.99},
            {"id": 204, "name": "Pride and Prejudice", "description": "Classic novel by Jane Austen.", "img": "pride_and_prejudice.jpg", "price": 16.99}
        ]
    },
    "Beauty": {
        "name": "Beauty",
        "img": "beauty_category.jpg",
        "items": [
            {"id": 300, "name": "Lipstick", "description": "A vibrant red lipstick for an elegant look.", "img": "lipstick.jpg", "price": 12.99},
            {"id": 301, "name": "Foundation", "description": "Smooth foundation for a flawless finish.", "img": "foundation.jpg", "price": 29.99},
            {"id": 302, "name": "Mascara", "description": "Enhance your lashes with this waterproof mascara.", "img": "mascara.jpg", "price": 15.49},
            {"id": 303, "name": "Perfume", "description": "A floral scent that is fresh and long-lasting.", "img": "perfume.jpg", "price": 49.99},
            {"id": 304, "name": "Nail Polish", "description": "Vibrant nail polish available in various colors.", "img": "nail_polish.jpg", "price": 8.99}
        ]
    },
    "Bags": {
        "name": "Bags",
        "img": "bags_category.jpg",
        "items": [
            {"id": 400, "name": "Backpack", "description": "Durable and stylish backpack for daily use.", "img": "backpack.jpg", "price": 49.99},
            {"id": 401, "name": "Handbag", "description": "Elegant handbag for every occasion.", "img": "handbag.jpg", "price": 89.99},
            {"id": 402, "name": "Travel Bag", "description": "Spacious travel bag for your journeys.", "img": "travel_bag.jpg", "price": 79.99},
            {"id": 403, "name": "Laptop Bag", "description": "Protective and stylish bag for your laptop.", "img": "laptop_bag.jpg", "price": 59.99},
            {"id": 404, "name": "Tote Bag", "description": "Versatile tote bag for shopping or the beach.", "img": "tote_bag.jpg", "price": 29.99}
        ]
    }
}

# morsi,fox
# the first page sign in page   get is for displaying the page  post is to check if the user can sign in or not

@bp.route("/", methods=["GET", "POST"])
def sign():
    if request.method == "POST":#if the request type is pst :)
        data = request.form # get the data from the sign in form (we sent it through js)
        email = data.get("email")# the data from te form :)
        password = data.get("password")

        for user in users_db: # a for loop to iterat through the users database to check if the user is among them or not
            if user["email"] == email and user["password"] == password:# if the user can log in 
                session['is_admin'] = user["is_admin"]#save his id and admin statue in the session 
                session['user_id'] = user["id"]
                return render_template("pages/home.html", products=products, isadmin=session.get('is_admin', False))# go to the home page  with the products and admin statue to display the admin list or not
        else:
            print("invalid user")# error handling if user isn't among them
            return jsonify({"success": False, "message": "Invalid "}), 400

    return render_template("pages/signin.html") # the get method to display  the sign in page

#morsi,fox
# the sign up form has 2 methods get for displaying the page and post to add the new user data to the database
@bp.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":#if method is post
        data = request.form# get the data from the html page ( through the js request)
        email = data.get("email")# place the data into vr :)
        password = data.get("password")
        name = data.get("name")

        for user in users_db: #check if the user already exist or not 
            if user["email"] == email:
                return jsonify({'success': False, 'message': 'User already exists'})

        new_user = {# make a new dictionry for the new user
            'id': len(users_db) + 1,
            'name': name,
            'email': email,
            'is_admin': False,
            'password': password,  
            'cart': []  
        }
        users_db.append(new_user)# add the new user to our users database

        return jsonify({'success': True, 'message': 'User registered successfully'})#success response wkda :)

    return render_template("pages/signup.html") #the get method to display the page :)

#shahd
@bp.route("/home")# the home end point it doesnt have a post as it just display the products so no need for a post method 
def home():
    is_admin = session.get('is_admin', False)# it gets the user admin statue from the session
    return render_template("pages/home.html", products=products, isadmin=is_admin)# and then return it to  home page  with the products (this api is used if iam already logged in )

#mohamed
@bp.route("/add", methods=["GET", "POST"])# the add page contains both get and post methods one to display the page and the post for adding a new item to the products 
def add():
    if request.method == "POST":# if the request type is method ya mohamed
        data = request.form # hat 2l data mn 2l html 
        type = data.get("type") # no3
        name = data.get("name")
        desc = data.get("description")
        price = data.get("price")
        img = request.files.get("img")
        if not img: # h4of 2l image gat wlla l2 
            return jsonify({"success": False, "message": "Image is required"}), 400
        imgname = secure_filename(img.filename) # mn 2l25r bt5ly 2lfile  2mn  23an 2l2sm mydrb4
        img_path = os.path.join(UPLOAD_FOLDER, imgname) # b7dd mkan 2lfile
        img.save(img_path)# 27fz b2a 2lsora bta3ty ffile 2l uploads
        if type in products: #for loop 2 iterat beeha  34an 2geeb type 2l product 2l h7to
            new_id = len(products[type]["items"]) + 1 #id gdeed
            new_product = {
                "id": new_id,
                "name": name,
                "description": desc,
                "img": imgname,
                "price": price
            }
            products[type]["items"].append(new_product)# h5zno gwa 2l items fe 2lproducts 2ll type bta3ha kza

            return jsonify({"success": True, "message": "Product added successfully", "product": new_product}), 201
        return jsonify({"success": False, "message": "Invalid product category"}), 400

    return render_template("pages/add.html", products=products)

#mariam
@bp.route("/delete", methods=["GET", "POST"])# delete page 2 methods get to display post to  delete the product from products
def delete():
    if request.method == "POST": # b4of 2l request bta3ty post wla l2 34an h3ml delete kda
        data = request.form # hageeb 2l data mn 2lpage (5dnaha mn js request)
        product_type = data.get("type")  # 5dt 2ldata 5las
        product_id = int(data.get("id"))  

        if product_type in products:# ha4of 2l type mawgood wlaa l2 
            
            product = next((prod for prod in products[product_type]["items"] if prod["id"] == product_id), None)
            # law mawgood ha4oof b2a 2l id mawgood wla l2 
            # # next function  btgeeb 2lnext item 7aga 4bh for loop kda bs 2shl 
            #  fe 2l7ala dh  htst5dm 2l genrator expresion 2llhwa prod for prod in products   law l2t prod [id] zay 2l id 2l 2na d5lto  
            # hay7to fe product law ml2aho4 hay5zn none 

            if product: #law l2a product
                # h2ol 2l products btsawy products bardo ma3da 2l product  2l 2na m4 3ayzo
                # hanheh mn 2l25r ya3ny
                # bngeebo 2zay bardo bnfs 2l taree2a 2ll hya genrator expresion
                products[product_type]["items"] = [prod for prod in products[product_type]["items"] if prod["id"] != product_id]
                return jsonify({"success": True, "message": f"Product '{product['name']}' deleted successfully"}), 200
                # harf 2l f dh bydol  3la 2ny hzawed variable fel 2l string bta3y
        return jsonify({"success": False, "message": "Product not found or invalid category"}), 404# error  response law ml2ahoo4

    
    return render_template("pages/delete.html", products=products) # dh 34an 2l get 2ft7 2lsaf7a mn 2l2wl 5ales 2sln :) 

#menna
@bp.route("/products") #products page there is  a seprate post api the next one :) 
def productspage():
    product_type = request.args.get("type")  # ha5ed 2ltype mn 2l2rguments 2llb3tha ma3 2l js

    return render_template("pages/products.html", products=products[product_type])# hroo7 2la 2l page b2a

#menna
@bp.route("/products", methods=["POST"])# post method to add a product to the cart from the products page
def product():
    user_id = session.get('user_id') # ha5od 2l user id mn 2l session 24an 23rf meen 2l user 
    print("Session User ID:", user_id)  # ta2keed 3ady
    if not user_id: # law 7asl 2kan guest h2lo mafee4 user
        return jsonify({"success": False, "message": "Invalid user session"}), 400
    data = request.form # ha5od 2l data mn 2l js 2ll b3tha 
    type = data.get("type")
    pid = data.get("id")
    if not type or not pid: # law 7asel bardo 2mkan4 feeh data  yb2a response b fail
        return jsonify({"success": False, "message": "Invalid product data"}), 400
    
    #bt2kd 2n 2lproduct fady
    product = None
    if type in products: # law no3o mawgood
        product = next((prod for prod in products[type]["items"] if prod["id"] == int(pid)), None)
        # nextfunction 4bh 2l foor loop  bt3dy 3la klo  law l2t 2l id dh  ht7t 2lproduct  law ml2to4 ht7t none
        #prod for prod dh 7aga 2smha genrator expresion ya3ny h5zn 2l prod dh f product law la2eeto wkda

    # kda m3aya 2lproduct 2geeb 2luser b2a
    user = next((user for user in users_db if user["id"] == user_id), None) # nafs 2lklam fe 2l next function w genrator expression
    if user is None:
        return jsonify({"success": False, "message": "User not found"}), 404

    
     # hazwod 2l product fe 2l cart bta3et 2l user
    user["cart"].append(product)

    print(user["cart"])  
    return jsonify({"success": True, "message": "Product added successfully to cart", "product": product}), 201

#weam
@bp.route("/cart")# cart page the get method and post method are seprated into 2 apis 
def carts():
    user_id = session.get('user_id') # haggeb 2l user mn 2l session 
    user = next((user for user in users_db if user["id"] == user_id), None)
     # nextfunction 4bh 2l foor loop  bt3dy 3la klo  law l2t 2l id dh  ht7t 2l user  law ml2to4 ht7t none
        #user for user dh 7aga 2smha genrator expresion ya3ny h5zn 2l user dh f user law la2eeto wkda

    if not user:
        return jsonify({"success": False, "message": "User not found"}), 404

    
    print(f"User {user_id}'s cart: {user['cart']}")  # batb3 2ldata fe 2l terminal zyadet ta2kked bs
    
    cart_items = user.get("cart", []) #b5zn 2l items bta3et 2l user gwa  list 34an 23rf 2b3tha  

    

    return render_template("pages/cart.html", items=cart_items) #bb3t 2l items b2a llpage 

#weam
@bp.route("/cart", methods=["POST"])# post method 34an 23rf 2 delete item mn 2l cart bta3ty
def delete_from_cart():
    user_id = session.get('user_id') # bageeb 2l user bardo
    if not user_id:
        return jsonify({"success": False, "message": "User not logged in"}), 404

    data = request.json# bageeb 2l item mn 2l request bta3ty (2l js )
    product_id = data.get("product_id")
    
    if not product_id:
        return jsonify({"success": False, "message": "Product ID not provided"}), 400
# bageeb 2l user  zat nafso b2a klo
    user = next((user for user in users_db if user["id"] == user_id), None)
    
    
     # ba2ool 2n 2l cart bta3et 2l user  nafs 2l cart ma3da 2l product 2ll 3mltlo delete
    user["cart"] = [item for item in user["cart"] if item['id'] != product_id]
    
    return jsonify({"success": True, "message": "Product removed from cart"})

@bp.route("/checkout", methods=["GET"]) #checkout to get me to the thank u page  and delete whole cart
def checkout():
    user_id = session.get('user_id')
    user = next((user for user in users_db if user["id"] == user_id), None)
    if not user:
        return jsonify({"success": False, "message": "User not found"}), 404
    user["cart"] = []
    session['cart'] = []
    return render_template("pages/checkout.html")
@bp.route('/aboutus') # the about us page contains our ids ,names and out amazing TAs names 
def aboutus():
    return render_template('pages/aboutus.html')
