
class Login:
    login_url = "https://api.demoblaze.com/login"
    success_message = 'Auth_token: bWlrZWUxNjc2MDQz'
    error_message = {"errorMessage": "User does not exist."}
    valid_data = {"username": "mikee", "password": "MTIzNjU0Nzg="}
    invalid_data = {"username": "tim", "password": "78965412"}
    incorrect_pass = {"username": "mikee", "password": "32145698"}
    wrong_pass_error = {'errorMessage': 'Wrong password.'}
    signup_url = "https://api.demoblaze.com/signup"
    signup_error = {'errorMessage': 'This user already exist.'}
