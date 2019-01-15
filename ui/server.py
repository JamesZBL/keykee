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
from flask import Flask, render_template

from data.buffered_repo import buffered_repo as repo

webapp = Flask(__name__, static_folder='static', static_url_path='/static')
app = webapp


@app.route("/")
def index():
	keys = repo.find_keys()
	size = len(keys)
	lines_per_column = int(size / 3)
	columns = []
	last = 0
	for i in range(0, size):
		if i % lines_per_column == 0 and i != 0 or i == size - 1:
			columns.append(keys[last: i])
			last = i
	return render_template('index.html', columns=columns)
