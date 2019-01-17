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
import _thread
import os

from conf.config import Config
from key.handler import KeyEventHandler
from key.listener import KeyListener
from api.server import webapp


def run_client():
	handler = KeyEventHandler()
	listener = KeyListener(handler)
	listener.listen()


def run_server():
	webapp.run(host='0.0.0.0', port=Config.server_port, debug=Config.dev)


def record_pid():
	this_pid = os.getpid()
	home_dir = Config.home_dir
	with open(home_dir + '.pid', 'w') as pid_file:
		pid_file.write(str(this_pid))


if __name__ == '__main__':
	_thread.start_new_thread(run_client, ())
	record_pid()
	run_server()
