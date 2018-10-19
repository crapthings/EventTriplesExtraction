from flask import Flask, request, jsonify
from sentence_parser import LtpParser
from triple_extraction import TripleExtractor

app = Flask(__name__)
ltp = LtpParser()

@app.route('/',methods = ['POST'])
def index():
  extractor = TripleExtractor(ltp)

  if request.is_json:
    phrase = request.json['phrase']
  else:
    phrase = request.form['phrase']

  result = extractor.triples_main(phrase)
  return jsonify(result)

if __name__ == '__main__':
   app.run(debug = False)
