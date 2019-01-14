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
from key.handler import KeyEventHandler
from key.listener import KeyListener
from ui.Server import webapp


class App:
	def run(self):
		self.run_server()
		self.run_client()

	def run_client(self):
		handler = KeyEventHandler()
		listener = KeyListener(handler)
		listener.listen()

	def run_server(self):
		webapp.run(host='0.0.0.0', port=9999, debug=True)


if __name__ == '__main__':
	app = App()
	app.run()
