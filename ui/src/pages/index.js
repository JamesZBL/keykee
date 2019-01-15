import styles from './index.css';
import {Card, Col, Row, Table} from 'antd';
import React from "react";
import ax from '../conf/request'


class KeysTable extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      rows: [],
      columns: [{
        title: 'order',
        dataIndex: 'order',
        align: 'center'
      }, {
        title: 'key',
        dataIndex: 'name',
        align: 'center'
      }, {
        title: 'count',
        dataIndex: 'count',
        align: 'center'
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
      <Table dataSource={this.state.rows} columns={this.state.columns} pagination={false}/>
    );
  }
}

export default function () {
  return (
    <div className={styles.normal}>
      <Row gutter={0}>
        <Col span={12}>
          <div className={styles.cards}>
            <Card title={'keystroke leaderboard'}>
              <KeysTable/>
            </Card>
          </div>
        </Col>
      </Row>
    </div>
  );
}
