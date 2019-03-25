from flask import Flask, request, render_template_string
import requests

app = Flask(__name__, static_url_path='/static')
ids =	{
  "f5ddb063e92808b472c31d82c887d791"
  }

@app.route("/",methods=['GET'])
def hello():
	auth = request.args.get('auth')
	if auth:
		if auth in ids:
			message = "auth recognized!"
			return render_template_string("""
<h1>ULTRA SECRET DINO DNA SERVICE</h1>
<h3>only host this service api on localhost to make sure we dont expose our proprietary dino DNA to external competitors</h3>
			
{{message}}
			
            
SSNs: 
519-33-7051
541-02-7240
402-35-3149
349-82-2699
657-32-6831
359-70-0916
			""",message=message)
		else:
			message = "DinoID not recognized!"
			return """
<h1>ULTRA SECRET SERVICE</h1>
<h3>only host this service api on localhost to make sure we dont expose our proprietary data to external competitors</h3>

<p>auth not recognized!</p>
			
			"""
	else:
		return """
<h1>ULTRA SECRET SERVICE</h1>
<h3>only host this service api on localhost to make sure we dont expose our proprietary data to external competitors</h3>
<p>to use this API, pass the auth as a GET param.</p>
		"""


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=False, port=1337)