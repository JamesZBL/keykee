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
import styles from './index.css';
import {Card, Col, Row} from 'antd';
import React from "react";
import KeysTable from '../components/keys_table'
import TopChart from "../components/top_chart";
import RecentChart from '../components/recent_chart'


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
            <Card title={'频率最高的10个键'}>
              <TopChart/>
            </Card>
          </div>
          <div className={styles.cards}>
            <Card title={'每日按键统计'}>
              <RecentChart/>
            </Card>
          </div>
        </Col>
      </Row>
    </div>
  );
}
