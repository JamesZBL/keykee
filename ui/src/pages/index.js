import styles from './index.css';
import {Card, Col, Row} from 'antd';
import React from "react";
import KeysTable from '../components/keys_table'
import TopChart from "../components/top_chart";


export default function () {
  return (
    <div className={styles.normal}>
      <Row gutter={0}>
        <Col span={12}>
          <div className={styles.cards}>
            <Card title={'按键排行榜'}>
              <KeysTable/>
            </Card>
          </div>
        </Col>
        <Col span={12}>
          <div className={styles.cards}>
            <Card title={'TOP 10'}>
              <TopChart/>
            </Card>
          </div>
        </Col>
      </Row>
    </div>
  );
}
