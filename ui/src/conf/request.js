import axios from "axios";

const ax = axios.create({
  baseURL: 'http://127.0.0.1:7999/',
  timeout: 1000,
  headers: {'X-Custom-Header': 'foobar'}
});

export default ax
