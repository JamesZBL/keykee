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
import style from './common.css'

class Monitor extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      total: 0,
      most_key: 'N/A',
      most_count: 0,
      today: 0
    }
  }

  componentDidMount() {
    ax.get('/till/now')
      .then(r => {
        r = r.data;
        let total = r.total;
        let most_key = r.most.name;
        let most_count = r.most.count;
        let today = r.today;
        this.setState({
          total: total,
          most_key: most_key,
          most_count: most_count,
          today: today
        })
      })
  }

  render() {
    return (
      <div>
        <Row gutter={0}>
          <Col span={8} className={style["col-div"]}>
            <span className={style.label}>一共按了</span>
            <span className={style["label-count"]}>{this.state.total}</span>
            <span className={style["label-line"]}>次</span>
          </Col>
          <Col span={8} className={style["col-div"]}>
            <span className={style.label}>今天按了</span>
            <span className={style["label-count"]}>{this.state.today}</span>
            <span className={style["label-line"]}>次</span>
          </Col>
          <Col span={8}>
            <span className={style.label}>按的最多的键是</span>
            <span className={style["label-key"]}>{this.state.most_key}</span>
          </Col>
        </Row>
      </div>
    );
  }
}

export default Monitor
