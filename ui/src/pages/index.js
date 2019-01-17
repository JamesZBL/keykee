import styles from './index.css';
import {Card, Col, Row} from 'antd';
import React from "react";
import KeysTable from '../components/keys_table'
import Monitor from '../components/monitor'
import {WholeDay, Recent, Top} from "../components/lazy_chart";


export default function () {
  return (
    <div className={styles.normal}>
      <Row gutter={0}>
        <Col offset={2} span={8}>
          <div className={styles.cards}>
            <Card title={'按键排行榜'}>
              <KeysTable/>
            </Card>
          </div>
        </Col>
        <Col span={12}>
          <div className={styles.cards}>
            <Card>
              <Monitor/>
            </Card>
          </div>
          <div className={styles.cards}>
            <Card title={'按的最多的 10 个键'}>
              <Top/>
            </Card>
          </div>
        </Col>
      </Row>
      <Row gutter={0}>
        <Col offset={2} span={20}>
          <div className={styles.cards}>
            <Card title={'按键频率历史趋势'}>
              <Recent/>
            </Card>
          </div>
        </Col>
      </Row>
      <Row gutter={0}>
        <Col offset={2} span={20}>
          <div className={styles.cards}>
            <Card title={'按键历史上的 24 小时'}>
              <WholeDay/>
            </Card>
          </div>
        </Col>
      </Row>
    </div>
  );
}
