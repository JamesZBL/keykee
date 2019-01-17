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
import style from "./common.css";
import echarts from "echarts";
import macaron from "../themes/macaron";
import colorList from "../themes/colors"

class WholeDayChart extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      hours: [],
      counts: []
    }
  }

  componentDidMount() {
    const _this = this;
    ax.get('/whole/day')
      .then(r => {
        r = r.data;
        let hour_counts = r.count;
        for (let i = 0; i < hour_counts.length; i++) {
          let hc = hour_counts[i];
          let hour = hc.hour;
          let count = hc.count;
          _this.state.hours.push(hour);
          _this.state.counts.push(count);
        }
        _this.initChart();
      });
  }

  initChart() {
    const day_chart = echarts.init(document.getElementById('day_chart'), macaron);
    day_chart.setOption({
      tooltip: {
        trigger: 'axis',
        formatter: '<b>{b}</b><br/>过去共按了 {c} 次'
      },
      calculable: true,
      xAxis: [
        {
          type: 'category',
          data: this.state.hours
        }
      ],
      yAxis: [
        {
          type: 'value'
        }
      ],
      series: [
        {
          type: 'bar',
          data: this.state.counts,
          itemStyle: {
            normal: {
              color: function (params) {
                return colorList[params.dataIndex]
              },
              label: {
                show: true,
                position: 'top',
                formatter: '{c}'
              }
            }
          },
        }
      ]
    });
  };

  render() {
    return (
      <div id="day_chart" style={{width: 1000, height: 400}} className={style.chart}/>
    )
  }
}

export default WholeDayChart;
