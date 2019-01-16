import styles from './index.css';
import {Card, Col, Row} from 'antd';
import React from "react";
import KeysTable from '../components/keys_table'
import TopChart from "../components/top_chart";
import RecentChart from '../components/recent_chart'
import Monitor from '../components/monitor'
import WholeDayChart from "../components/whole_day";


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
              <TopChart/>
            </Card>
          </div>
        </Col>
      </Row>
      <Row gutter={0}>
        <Col offset={2} span={20}>
          <div className={styles.cards}>
            <Card title={'按键频率历史趋势'}>
              <RecentChart/>
            </Card>
          </div>
        </Col>
      </Row>
      <Row gutter={0}>
        <Col offset={2} span={20}>
          <div className={styles.cards}>
            <Card title={'按键历史上的 24 小时'}>
              <WholeDayChart/>
            </Card>
          </div>
        </Col>
      </Row>
    </div>
  );
}
