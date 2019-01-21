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
import React from 'react';
import WholeDayChart from "./whole_day";
import RecentChart from "./recent_chart";
import TopChart from "./top_chart";
import {Empty} from "antd";
import TrackVisibility from "react-on-screen";


const emptyLg = <Empty style={{width: 900, height: 400}}/>;
const emptySm = <Empty style={{width: 500, height: 400}}/>;
export const WholeDay = () => {
  return (
    <TrackVisibility offset={100} once={true}>
      {({isVisible}) => isVisible ? <WholeDayChart/> : emptyLg}
    </TrackVisibility>
  );
};

export const Recent = () => {
  return (
    <TrackVisibility offset={100} once={true}>
      {({isVisible}) => isVisible ? <RecentChart/> : emptyLg}
    </TrackVisibility>
  );
};

export const Top = () => {
  return (
    <TrackVisibility offset={100} once={true}>
      {({isVisible}) => isVisible ? <TopChart/> : emptySm}
    </TrackVisibility>
  );
};
