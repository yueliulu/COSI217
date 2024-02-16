"""Simple Web interface to spaCy entity recognition

To see the pages point your browser at http://127.0.0.1:5000.

"""


from flask import Flask, request, render_template

import ner_dep

app = Flask(__name__)


# For the website we use the regular Flask functionality and serve up HTML pages.

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html', input=open('input.txt').read())
    else:
        text = request.form['text']
        doc = ner_dep.SpacyDocument(text)
        markup = doc.get_entities_with_markup()
        markup_paragraphed = ''
        for line in markup.split('\n'):
            if line.strip() == '':
                markup_paragraphed += '<p/>\n'
            else:
                markup_paragraphed += line
        dependencies = doc.get_dependency()
        dependency_table = ''
        for d in dependencies:
            dependency_table = '<p>' + dependency_table + d[0] + "\t\t" + d[1] + "\t\t\t" + d[2] + '</p>\n'

        return render_template('result.html', markup=markup_paragraphed, parsed=dependency_table)


if __name__ == '__main__':

    app.run(debug=True)
