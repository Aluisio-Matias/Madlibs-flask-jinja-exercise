from flask import Flask, request, render_template
from stories import stories
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# app.config['SECRET_KEY'] = "mablibs"
# debug = DebugToolbarExtension(app)

@app.route('/')
def select_story():
    '''Show list of story templates'''
    return render_template('select-story.html', stories=stories.values())

@app.route('/words')
def ask_words():
    '''Show page with form to ask for words to create the story'''
    story_id = request.args['story_id']
    story = stories[story_id]
    
    prompts = story.prompts

    return render_template('words.html', story_id=story_id, title=story.title, prompts=prompts)

@app.route('/story')
def create_story():
    '''Creates the story and displays it'''
    story_id = request.args['story_id']
    story = stories[story_id]

    text = story.generate(request.args)

    return render_template('story.html', title=story.title, text=text)

