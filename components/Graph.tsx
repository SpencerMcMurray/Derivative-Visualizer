import React, { FunctionComponent } from "react";
import { Line } from "../public/static/helpers/interfaces";
import loadable from "@loadable/component";
const Chart = loadable(() => import("react-apexcharts"));

interface GraphProps {
  id: string;
  title: string;
  x: number[];
  lines: Line[];
  width?: number;
  height?: number;
}

const Graph: FunctionComponent<GraphProps> = ({ x, lines, ...props }) => {
  const options = {
    title: { text: props.title },
    xaxis: { x },
  };
  return (
    <Chart
      options={options}
      series={lines}
      type="area"
      width={props.width || 500}
      height={props.height || 500}
      className="col-xl-5"
      align="center"
    />
  );
};

export default Graph;
