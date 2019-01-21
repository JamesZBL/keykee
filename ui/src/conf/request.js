/*
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
import axios from "axios";

let server_port = process.env.SERVER_PORT;
const ax = axios.create({
  baseURL: 'http://127.0.0.1:' + server_port + "/",
  timeout: 10000,
  headers: {'X-Custom-Header': 'foobar'}
});

export default ax
