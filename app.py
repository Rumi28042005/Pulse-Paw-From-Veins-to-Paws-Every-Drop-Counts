from flask import Flask, render_template , request , jsonify
from chatbot import get_motivational_message
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app)

# getting internal server error
# @app.route('/', methods=['GET', 'POST'])    
# def home():
#     if request.method == 'POST':
#         # Handle donor registration logic here
#         pass
#     return render_template('homepage.html')


# Define motivation messages
motivation_messages = [
    "❤ One small prick, a lifetime of impact. Be someone's hero today! 🚑",
"💉 You have the power to save lives—your blood is a gift of hope! 🏥", 
"🩸 A few minutes for you, a lifetime for them. Donate blood, save a life! ⏳", 
"🎖 Be proud of being a lifesaver—donate blood, make a difference! 🦸‍♂",
"⚡ Fear is temporary, but the life you save is forever! 💪", 
"🌿 Close your eyes, take a deep breath, and remember—you’re saving a life! 🌬",
"🦸‍♂ You're braver than you think! A tiny pinch can mean the world to someone. ✨",
"✨ Think of it this way: you’re not just donating blood, you’re donating hope! 🤝", 
"🐾 Your pet can be a hero too! Give the gift of life to another furry friend. 🦴",  
"🦴 Just like humans, pets need blood too—your pet can make a difference! 🐶",
"🐕‍🦺 Helping another pet in need is an act of pure love. Let your pet be a lifesaver! ❤",
"🎉 First time donating? You’re about to do something amazing—saving a life! 🚀", 
"🦸‍♀ Heroes don’t always wear capes. Today, you become one by donating blood! 🦸‍♂",
"🚀 Every great journey begins with a single step—this one saves lives! 🔄",
"💪 The first time is always the hardest, but the impact lasts forever! 🔥",
"🔁 Consistency saves lives. Keep being the hero someone is waiting for! ❤‍🔥",
"💖 Every donation matters. Someone out there is grateful for your kindness! 🙏", 
"🌟 Your blood has the power to heal. Keep spreading hope, one drop at a time! 💧"
]
@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html')

@app.route('/donor', methods=['GET', 'POST'])
def donor():
    if request.method == 'POST':
        # Handle donor registration logic here
        pass
    return render_template('donor.html')

@app.route('/get_message', methods=['POST'])
def get_message():
    return jsonify({"message": get_motivational_message()})

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/pet')
def pet():
    return render_template('pet.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/eligibility_checker', methods=['GET', 'POST'])
def eligibility_checker():
    return render_template('eligibility_checker.html')

@app.route('/reciever')
def reciever():
    return render_template('reciever.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        pass
    return render_template('login.html')


@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/appoin')
def appoin():
    return render_template('appoin.html')

@app.route('/request_blood', methods=['GET', 'POST'])
def request_blood():
    if request.method == 'POST':
        # Handle blood request logic here
        pass
    return render_template('request_blood.html')


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000, debug = True)