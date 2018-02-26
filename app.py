from flask import Flask, render_template, request
import pokemongo

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    userinput = ''
    if len(request.args) > 0:
        userinput = request.args['input']
    results = {}
    try:
        int(userinput)
        results = pokemongo.find_id(userinput)
    except:
        namesearch = pokemongo.find_name(userinput)
        typesearch = pokemongo.find_type(userinput)
        if len(namesearch) > len(typesearch):
            results = namesearch
        else:
            results = typesearch
    return render_template('form.html',results=results)

    

if __name__ == ('__main__'):
    app.debug = True
    app.run()
        
