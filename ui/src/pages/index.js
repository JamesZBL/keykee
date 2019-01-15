import styles from './index.css';
import {Card, Col, Row} from 'antd';
import React from "react";
import KeysTable from '../components/keys_table'


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
