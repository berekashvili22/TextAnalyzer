from flask import render_template, url_for, flash, redirect, request
from textanalyzer import app
from textanalyzer.forms import TextForm
# from textanalyzer.models import User, Account

# alphabet
script = " აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ" #with whitespace

script_clean = "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ" #without whitespace

script_symbols = "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

# functions

def words_count(text):
    words = ('')
    for i in text:
        if i in script:
            words += i
    words = words.split()
    words_new = []
    for i in words:
        if len(i) >= 2:
            words_new.append(i)
        else:
            pass
    di = dict()
    for w in words_new:
        # set w value in dict to 0 if it doesnot exist , if it exists add 1 to its value
        di[w] = di.get(w,0) + 1
    return di

def most_used(text):
    di = words_count(text)
    largest = -1
    theword = None
    k = "-"
    v = "-"
    for k,v in di.items():
        if v > largest:
            largest = v
            theword = k
    new_di = {theword: largest}
    return new_di
    

def words_all(text):
    words = ('')
    for i in text:
        if i in script:
            words += i
    words = words.split()
    words_new = []
    for i in words:
        if len(i) >= 2:
            words_new.append(i)
        else:
            pass
    all_words_count = str(len(words_new))
    return all_words_count


def character_without_white(text):
    count = 0
    for i in text:
        if i in script_symbols:
            count += 1
        else:
            pass
    return count

def character_without_symbols(text):
    count = 0
    for i in text:
        if i in script_clean:
            count += 1
        else:
            pass
    return count


@app.route('/')
@app.route('/home', methods=['POST', 'GET'])
def home():
    form = TextForm()
    
    data = form.text.data

    # txt = len(str(data))

    #character count
    chars_total = len(str(data))
    # character count without white space
    chars_without_space = character_without_white(str(data))
    # character count without symbols
    chars_without_symbols = character_without_symbols(str(data))
    # words_count = 5
    unique_words = words_count(str(data))
    #all words
    all_words = words_all(str(data))
    #most_used
    used_most = most_used(str(data))
    #unique word count
    #sentecise count
    #all words
    #all unique words

    return render_template('home.html', form=form,
                            total=chars_total, without_white=chars_without_space, without_symbols=chars_without_symbols,
                            words_count=unique_words, words=all_words, most_used=used_most)


@app.route('/about')
def about():
    return 'about_page'

















# @app.route('/register', methods=['POST', 'GET'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(
#             f'გილოცავ {form.first_name.data}! თქვენ წარმატებით გაიარეთ რეგისტრაცია', 'flash_success')
#         return redirect(url_for('home'))

#     return render_template('register.html', form=form)


# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'test@gmail.com' and form.password.data == 'test':
#             flash(f'გილოცავთ ავტორიზაცია წარმატებით განხორციელდა', 'flash_success')
#             return redirect(url_for('home'))
#         else:
#             flash('unsuccsesful', 'flash_fail')

#     return render_template('login.html', form=form)
