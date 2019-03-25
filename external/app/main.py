from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
	if request.method == 'POST':
		try:
			URL = request.form.get('url')
			headers = {'X_SECRET_AUTH_KEY': 'f5ddb063e92808b472c31d82c887d791'}
			r = requests.get(url = URL,headers=headers)
			body = r.text
			header = r.headers
		except:
			URL = "Failed"
			body = ""
			header = ""
		return render_template_string("""
		<h1>Website Tester</h1>
		<p>This page can be used to test your website to make sure it works right.</p>
        <p>Enter a URL below and the system will fetch it show the headers and body of the response.</p>

		</br></br></br>
		<form action="/" method="post">
			URL:  <input type="text" name="url" value="{{URL}}" size="70">
			<input type="submit" value="Submit">
		</form> 

		<h3>Attempting to fetch: {{URL}}</h3>
		<h3>headers</h3>
		<pre>{{header}}</pre></br>
		<h3>body</h3>
		<pre>{{body}}</pre>
		""",body=body,URL=URL,header=header)
	else:
		return """
		<h1>Website Tester</h1>
		<p>This page can be used to test your website to make sure it works right.</p>
        <p>Enter a URL below and the system will fetch it show the headers and body of the response.</p>

		</br></br></br>
		<form action="/" method="post">
			URL:  <input type="text" name="url" value="https://trustfoundry.net/" size="70">
			<input type="submit" value="Submit">
		</form> 
		"""


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=False, port=80)