from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def contact():
   return render_template('contact.html')

@app.route('/confirmation.html', methods=['POST'])
def submit():
   if request.method=='POST':
      email = request.form['email']
      phone = request.form['phone']
      message = request.form['message']
      subject = request.form['subject']
      other_subject = request.form.get('other_subject', '')
      contact_methods = request.form.getlist('contact_method')
      agreement = 'Yes' if request.form.get('agreement') else 'No'
      final_subject = other_subject if subject == 'Other' else subject
      return render_template('confirmation.html', name=name, email=email, phone=phone, message=message, subject=final_subject, contact_methods=contact_methods, agreement=agreement)

if __name__ == '__main__':
   app.run(debug=True)
