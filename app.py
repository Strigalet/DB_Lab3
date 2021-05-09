from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qhulhbgkzcllgx:107c4e01b6c6425eeb28be5f147b6c73c9e3dee1987ec8c4253766a8af6e7a1a@ec2-52-19-96-181.eu-west-1.compute.amazonaws.com:5432/d5adtng2ucjs4l'
db = SQLAlchemy(app)

class Channel(db.Model):
	__tablename__ = 'channel'
	name = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
	subscribers = db.Column(db.Integer, nullable=False)
	channel = db.relationship('Video', cascade='delete')

class Video(db.Model):
	link = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
	name = db.Column(db.String(255), nullable=False)
	channel = db.Column(db.String(255), db.ForeignKey('channel.name'))
	rating = db.Column(db.Float, nullable=False)
	views = db.Column(db.Integer, nullable=False)



db.create_all()
db.session.commit()



@app.route("/")
def render():
	video = Video.query.all()
	channel = Channel.query.all()
	return render_template('index.html', vid=video, chl=channel, video_name='Video', channel_name='Channel')



@app.route('/<table>/Create', methods=['post'])
def add(table):
	if table == 'Video':
		link = request.form.get('link')
		name = request.form.get('name')
		channel = request.form.get('channel')
		rating = request.form.get('rating')
		views = request.form.get('views')
		outcome = Video(link=link, name=name, channel=channel, rating=rating, views=views)
	elif table == 'Channel':
		name = request.form.get('name')
		subscribers = request.form.get('subscribers')
		outcome = Channel(name=name, subscribers=subscribers)
	try:
		db.session.add(outcome)
		db.session.commit()
	except Exception:
		return redirect(url_for('render'))
	return redirect(url_for('render'))



@app.route('/<table>/Update', methods=['post'])
def update(table):
	if table == 'Video':
		link = request.form.get('link')
		name = request.form.get('name')
		channel = request.form.get('channel')
		rating = request.form.get('rating')
		views = request.form.get('views')
		video = db.session.query(Video).get(link)
		video.name = name
		video.channel = channel
		video.rating = rating
		video.views = views
	elif table == 'Channel':
		name = request.form.get('channel')
		subscribers = request.form.get('subscribers')
		channel = db.session.query(Channel).get(name)
		channel.subscribers = subscribers
	try:
		db.session.commit()
	except Exception:
		return redirect(url_for('render'))
	return redirect(url_for('render'))




@app.route('/<table>/Delete/<name>')
def delete(table,name):
	if table == 'Video':
		require = Video.query.all()
	elif table == 'Channel':
		require = Channel.query.all()
	for i in require:
		if i.name == name:
			db.session.delete(i)
			db.session.commit()
	return redirect(url_for('render'))


if __name__ == "__main__":
	app.run()