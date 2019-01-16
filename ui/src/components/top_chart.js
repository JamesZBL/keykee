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
import echarts from 'echarts';
import style from './common.css';
import macaron from '../themes/macaron'


class TopChart extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      tops: [],
      total: 0,
      other: 0.0000,
      names: []
    };
  }

  componentDidMount() {
    const _this = this;
    ax.get('/top/10')
      .then(r => {
        _this.setState({
          tops: r.data.tops,
          total: r.data.total,
          other: r.data.other
        });
        let _names = [];
        for (let i = 0; i < _this.state.tops.length; i++) {
          let k = _this.state.tops[i];
          k.value = k.count;
          let name = k.name;
          _names.push(name);
        }
        _this.setState({
          names: _names
        });
        _this.initChart();
      });
  }

  initChart() {
    const top_chart = echarts.init(document.getElementById('top_chart'), macaron);
    top_chart.setOption({
        tooltip: {
          trigger: 'item',
          formatter: "<b>{b}</b><br/>按了{c}次 ({d}%)"
        },
        legend: {
          orient: 'vertical',
          x: 'left',
          data: this.state.names
        },
        toolbox: {
          show: true,
          feature: {
            mark: {show: true},
            magicType: {
              show: true,
              type: ['pie', 'funnel'],
              option: {
                funnel: {
                  x: '25%',
                  width: '50%',
                  funnelAlign: 'left',
                  max: 1548
                }
              }
            },
          }
        },
        calculable: true,
        series: [
          {
            name: 'hit times',
            type: 'pie',
            radius: '55%',
            center: ['55%', '50%'],
            data: this.state.tops
          }
        ]
      }
    )
    ;
  }

  render() {
    return (
      <div id="top_chart" style={{width: 500, height: 400}} className={style.chart}/>
    );
  }
}

export default TopChart
