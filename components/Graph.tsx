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
    chart: { group: "charts", id: props.id },
    title: { text: props.title },
    xaxis: { x },
  };
  const series = lines.map((line, idx) => ({
    name: line.name,
    data: line.yPoints,
  }));
  return (
    <Chart
      options={options}
      series={series}
      type="area"
      width={props.width || 500}
      height={props.height || 500}
    />
  );
};

export default Graph;
