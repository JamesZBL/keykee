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
	for k in range(0, len(total)):
		key = total[k]
		count = key['count']
		if k < top:
			tops.append(key)
			tops_count += count
		total_count += count
	other_count = total_count - tops_count
	return jsonify({'total': total_count, 'tops': tops, 'other': other_count})


@app.route("/recent")
def recent():
	recent_times = repo.find_recent(count=999)
	recent_times.reverse()
	return jsonify({'times': recent_times})


@app.route("/till/now")
def till_now():
	total_count = repo.find_total_count()
	total = repo.find_keys()
	most_frequency_key = total[0] if len(total) > 0 else None
	today_count = repo.find_today_count()
	return jsonify({'total': total_count, 'most': most_frequency_key, 'today': today_count})


@app.route('/whole/day')
def whole_day():
	whole_day_count = repo.find_whole_day()
	for i in whole_day_count:
		hour_from = i['hour']
		hour_to = hour_from + 1
		i['hour'] = '{0}-{1} 时'.format(hour_from, hour_to)
	return jsonify({'count': whole_day_count})
