from selenium.webdriver.common.by import By


class Locators:
    # ----------------------  homepage locators ---------------------
    url = "https://www.demoblaze.com/"
    header = (By.XPATH, "//nav[@id='narvbarx']")
    footer = (By.XPATH, "//div[@id='footc']")
    body = (By.XPATH, "//body")
    brand_name = (By.XPATH, "//a[@id='nava']")
    categories = [(By.XPATH, "//a[contains(text(),'Phones')]"),
           (By.XPATH, "//a[contains(text(),'Laptops')]"),
           (By.XPATH, "//a[contains(text(),'Monitors')]")]
    login_link = (By.XPATH, "//a[@id='login2']")
    username_path = (By.XPATH, "//input[@id='loginusername']")
    password_path = (By.XPATH, "//input[@id='loginpassword']")
    name_of_user = (By.XPATH, "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[7]/a[1]")
    random_product = (By.XPATH, "//a[contains(text(),'Samsung galaxy s6')]")
    random_price = (By.XPATH, "//body[1]/div[5]/div[1]/div[2]/div[1]/div[5]/div[1]/div[1]/h5[1]")
    home_link = (By.XPATH, "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]")
    previous_button = (By.XPATH, "/html[1]/body[1]/div[5]/div[1]/div[2]/form[1]/ul[1]/li[1]/button[1]")
    next_button = (By.XPATH, "/html[1]/body[1]/div[5]/div[1]/div[2]/form[1]/ul[1]/li[2]/button[1]")
    products_on_page = (By.XPATH, "/html[1]/body[1]/div[5]/div[1]/div[2]/div[1]/div")
    phone_link = (By.XPATH, "//a[contains(text(),'Phones')]")
    laptop_link = (By.XPATH, "//a[contains(text(),'Laptops')]")
    monitors_link = (By.XPATH, "//a[contains(text(),'Monitors')]")
    caroucel_right = (By.XPATH, "/html[1]/body[1]/nav[1]/div[2]/div[1]/a[2]/span[1]")

    # ----------------------------cart locators -----------------------
    add_to_cart = (By.XPATH, "//a[contains(text(),'Add to cart')]")
    cart_link = (By.XPATH, "//a[@id='cartur']")
    product_on_cart = (By.XPATH, "//tbody/tr[1]/td[1]/img[1]")
    price_on_cart = (By.ID, "totalp")
    delete = (By.XPATH, "//a[contains(text(),'Delete')]")
    added_product = (By.XPATH, "//tbody/tr[1]/td[1]/img[1]")
    cart_title = (By.XPATH, "//h2[contains(text(),'Products')]")
    place_order_button = (By.XPATH, "//button[contains(text(),'Place Order')]")

    # ------------------------  place order ------------------------------

    name_path = (By.XPATH, "//input[@id='name']")
    country_path = (By.XPATH, "//input[@id='country']")
    city_path = (By.XPATH, "//input[@id='city']")
    card_path = (By.XPATH, "//input[@id='card']")
    month_path = (By.XPATH, "//input[@id='month']")
    year_path = (By.XPATH, "//input[@id='year']")
    purchase_button = (By.XPATH, "//button[contains(text(),'Purchase')]")
    order_successfully = (By.XPATH, "//h2[contains(text(),'Thank you for your purchase!')]")
    record = (By.XPATH, "//body/div[10]/p[1]")
    order_page_title = (By.XPATH, "//h5[@id='orderModalLabel']")
    confirm = (By.XPATH, "//button[contains(text(),'OK')]")
    purchase_close_button = (By.XPATH, "//body/div[@id='orderModal']/div[1]/div[1]/div[3]/button[1]")

    # -------------------------- sign up -------------------------------
    signup_button = (By.XPATH, "//button[contains(text(),'Sign up')]")
    signup_link = (By.XPATH, "//a[@id='signin2']")
    signup_name = (By.XPATH, "//input[@id='sign-username']")
    signup_pass = (By.XPATH, "//input[@id='sign-password']")
    signup_close_button = (By.XPATH, "//body/div[@id='signInModal']/div[1]/div[1]/div[3]/button[1]")
    signup_header = (By.XPATH, "//h5[@id='signInModalLabel']")

    # ------------------------  login -----------------------------
    login_header = (By.XPATH, "//h5[@id='logInModalLabel']")
    login_name = (By.XPATH, "//input[@id='loginusername']")
    login_pass = (By.XPATH, "//input[@id='loginpassword']")
    login_button = (By.XPATH, "//button[contains(text(),'Log in')]")
    login_close_button = (By.XPATH, "//body/div[@id='logInModal']/div[1]/div[1]/div[3]/button[1]")
    logout_link = (By.XPATH, "//a[@id='logout2']")

    # -----------------------  contact us --------------------------------
    contact_link = (By.XPATH, "//a[contains(text(),'Contact')]")
    contact_page_title = (By.XPATH, "//h5[@id='exampleModalLabel']")
    email_path = (By.XPATH, "//input[@id='recipient-email']")
    comment_name = (By.XPATH, "//input[@id='recipient-name']")
    message_path = (By.XPATH, "//textarea[@id='message-text']")
    send_message_button = (By.XPATH, "//button[contains(text(),'Send message')]")
    contact_close_button = (By.XPATH, "//body/div[@id='exampleModal']/div[1]/div[1]/div[3]/button[1]")


class Colors:
    dark_blue = 'rgba(41, 43, 44, 1)'
    white1 = 'rgba(250, 252, 255, 1)'
    white2 = 'rgba(0, 0, 0, 0)'


class Inputs:
    username = "mikee"
    password = 12365478
    invalid_pass = "!@#$%^&*m("
    name = "mikiyas"
    invalid_name = "b54651=-#%@"
    country = "Israel"
    invalid_country = "sdfg5"
    city = "Beer Sheva"
    invalid_city = "6584lkoji"
    card_num = "1234568796"
    invalid_card = "kjb%^*()_+!@"
    month = 2
    invalid_month = "1p"
    year = 2026
    invali_year = "6+11sdf"
    less_pass = "12"
    email = "miko12@gmail.com"
    invalid_email = "dfbgf^&*%$#%"
    comment = "I was satisfied with your service"
    invalid_comment = "%$$####@@)((*&^^^%^%%%$$????||||"


