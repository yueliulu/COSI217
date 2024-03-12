"""Simple Web interface to spaCy entity recognition

To see the pages point your browser at http://127.0.0.1:5000.

"""
from collections import Counter

from flask import Flask, request, render_template

import ner_dep

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fc3bb2a43ff1103895a4ee315ee27740'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_entity_dependency.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity = db.Column(db.String(80), unique=True)
    count = db.Column(db.Integer, default=0)
    dep = db.relationship('Dependency', backref='entity', lazy=True)

    def pp(self):
        dependency = '<p>\n    '.join([str(d) for d in self.dep])
        return dependency


class Dependency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    head = db.Column(db.String(100), nullable=False)
    dep = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(100), nullable=False)
    count = db.Column(db.Integer, default=1)
    entity_id = db.Column(db.Integer, db.ForeignKey('entity.id'), nullable=False)

    def __repr__(self):
        return f"{self.head} {self.dep} {self.text} {self.count}"
        #return [self.head, self.dep, self.text, self.count]


def add_dependency(entity, dep):
    d = Dependency.query.filter_by(head=dep[1], dep=dep[0], text=dep[2], entity_id=entity.id).first()
    if d:
        d.count += 1
    else:
        dependency = Dependency(head=dep[1], dep=dep[0], text=dep[2], entity_id=entity.id)
        db.session.add(dependency)
    db.session.commit()



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

        entities = doc.get_entities()
        entities_dependency = doc.get_entities_dependency()
        for e in entities:
            print(e[3])
            entity = Entity.query.filter_by(entity=e[3]).first()
            if entity:
                entity.count+=1
                for dep in entities_dependency[e[3]]:
                    add_dependency(entity, dep)
            else:
                new_entity = Entity(entity=e[3], count=0)
                new_entity.count += 1
                db.session.add(new_entity)
                db.session.commit()
                for dep in entities_dependency[e[3]]:
                    add_dependency(new_entity, dep)

        return render_template('result_page.html', markup=markup_paragraphed, parsed=dependency_table)


@app.route('/database')
def database():
    database = Entity.query.all()
    return render_template('database.html', data=database)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
