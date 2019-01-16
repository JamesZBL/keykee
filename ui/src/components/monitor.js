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
import React from "react";
import ax from "../conf/request";
import {Col, Row} from "antd";

class Monitor extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      total: 0,
      most_key: '',
      most_count: 0
    }
  }

  componentDidMount() {
    ax.get('/till/now')
      .then(r => {
        r = r.data;
        let total = r.total;
        let most_key = r.most.name;
        let most_count = r.most.count;
        this.setState({
          total: total,
          most_key: most_key,
          most_count: most_count
        })
      })
  }

  render() {
    return (
      <div>
        <Row>
          <Col span={8}>
            总共按了 {this.state.total} 次
          </Col>
          <Col span={8}>
            按的最多的是 {this.state.most_key} 键
            <br/>按了 {this.state.most_count} 次
          </Col>
          <Col span={8}>

          </Col>
        </Row>
      </div>
    );
  }
}

export default Monitor
