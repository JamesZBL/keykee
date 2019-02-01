/*

Copyright JamesZBL 2019

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
import style from "./common.css";
import echarts from "echarts";
import macaron from '../themes/macaron'
import ax from "../conf/request";

class RecentChart extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      names: [],
      values: []
    }
  }

  componentDidMount() {
    const _this = this;
    ax.get('/recent').then(data => {
      let times = data.data.times;
      for (let i = 0; i < times.length; i++) {
        let t = times[i];
        let date = t.date;
        let value = t.count;
        _this.state.names.push(date);
        _this.state.values.push(value)
      }
      this.initChart();
    });
  }

  initChart() {
    const recent_chart = echarts.init(document.getElementById('recent_chart'), macaron);
    recent_chart.setOption({
      tooltip: {
        trigger: 'axis',
        formatter: "<b>{b}</b><br/>按了 {c} 次"
      },
      calculable: true,
      xAxis: [
        {
          type: 'category',
          boundaryGap: false,
          data: this.state.names,
          scale: true
        }
      ],
      yAxis: [
        {
          type: 'value',
          axisLabel: {
            formatter: '{value}'
          }
        }
      ],
      series: [
        {
          name: '按键次数',
          type: 'line',
          data: this.state.values,
          markPoint: {
            data: [
              {type: 'max', name: '按的最多的一天'},
              {type: 'min', name: '按的最少的一天'}
            ]
          },
          markLine: {
            data: [
              {type: 'average', name: '平均每天'}
            ]
          }
        }
      ],
      dataZoom: {
        show: true,
        realtime: true,
        start: 0,
        end: 100
      }
    });
  }

  render() {
    return (
      <div id="recent_chart" style={{width: 1000, height: 400}} className={style.chart}/>
    );
  }
}

export default RecentChart
