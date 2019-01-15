# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from flask import Flask, render_template, jsonify
from flask_cors import CORS

from data.buffered_repo import buffered_repo as repo

webapp = Flask(__name__, static_folder='templates', static_url_path='')
app = webapp
CORS(app)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/keys")
def keys():
	find = repo.find_keys()
	return jsonify({'rows': find})


@app.route("/top/<int:top>")
def top10(top):
	total = repo.find_keys()
	total_count = 0
	tops = []
	tops_count = 0
	i = 0
	for k in total:
		if i < top:
			tops.append(k)
			tops_count += k['count']
		count = k['count']
		total_count += count
		i += 1
	tops_proportion = 0
	for k in tops:
		count = k['count']
		proportion = round(count / total_count, ndigits=4)
		k['proportion'] = proportion
		tops_proportion += proportion
	other_count = total_count - tops_proportion
	return jsonify({'total': total_count, 'tops': tops, 'other': other_count})


@app.route("/recent")
def recent():
	recent_times = repo.find_recent()
	return jsonify(recent_times)
