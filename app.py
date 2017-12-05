from flask import Flask, render_template, request, flash, redirect, url_for, session
from forms import *
from modules import cert, register, invite, send_mail

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/speaker', methods = ['GET', 'POST'])
def speaker():
   form = NewSpeakerForm()

   if request.method == 'POST':
       if form.validate() == False:
           flash('All fields are required.')
           return render_template('speaker.html', form = form)
       else:
           register.newspeaker(form.name.data, form.org.data, form.email.data)
           submission_successful = True
           form = NewSpeakerForm(formdata=None)
           return render_template('speaker.html', form=form, submission_successful=submission_successful)
   elif request.method == 'GET':
       return render_template('speaker.html', form = form)

@app.route('/certificate', methods = ['GET', 'POST'])
def certificate():
   form = CertForm()
   id, name = cert.showspeaker()

   if request.method == 'POST':
       if not request.form.getlist('speakers'):
           flash('All fields are required.')
           selected = False
           return render_template('certificate.html', form = form, data=zip(id, name), selected = selected)
       else:
           selected = True
           n, fn = cert.generate(request.form.getlist('speakers'))
           return render_template('download.html', data=zip(n, fn))
   elif request.method == 'GET':
       selected = True
       return render_template('certificate.html', form = form, data=zip(id,name), selected = selected)

@app.route('/invitation', methods = ['GET', 'POST'])
def invitation():
   form = InviteForm()
   id, name = invite.showspeaker()

   if request.method == 'POST':
       if not request.form.getlist('speakers'):
           flash('All fields are required.')
           selected = False
           return render_template('invitation.html', form = form, data=zip(id, name), selected = selected)
       else:
           speakers = request.form.getlist('speakers')
           list = ','.join(speakers)
           session['speakers'] = list
           return redirect(url_for('mail'))
   elif request.method == 'GET':
       selected = True
       return render_template('invitation.html', form = form, data=zip(id,name), selected = selected)

@app.route('/mail', methods = ['GET', 'POST'])
def mail():
   speakers = session['speakers'].split(',')
   form = SendForm()

   if request.method == 'POST':
       n, fn = invite.generate(speakers)
       if not request.form.getlist('file_name'):
           flash('All fields are required.')
           selected = False
           return render_template('send.html', form = form, data=zip(n, fn), selected = selected)
       else:
           selected = True
           emailsent = True
           send_mail.sende(request.form.getlist('file_name'))
           return render_template('send.html', data=zip(n, fn), emailsent=emailsent, form=form, selected = selected)
   elif request.method == 'GET':
       selected = True
       n, fn = invite.generate(speakers)
       return render_template('send.html', data=zip(n,fn), form=form, selected = selected)


if __name__ == '__main__':
   app.run(host='0.0.0.0', port='80')
