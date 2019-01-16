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
import {Table} from "antd";

class KeysTable extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      rows: [],
      columns: [{
        title: '排名',
        dataIndex: 'order',
        align: 'center',
        width: 80
      }, {
        title: '按键',
        dataIndex: 'name',
        align: 'center',
        width: 150
      }, {
        title: '次数',
        dataIndex: 'count',
        align: 'center',
        width: 150
      }]
    };
  }

  componentDidMount() {
    const _this = this;
    ax.get('/keys')
      .then(r => _this.setState({
        rows: r.data.rows
      }));
  }

  render() {
    return (
      <Table scroll={{y: 865}} bordered={true} dataSource={this.state.rows}
             columns={this.state.columns} pagination={false}/>
    );
  }
}

export default KeysTable
