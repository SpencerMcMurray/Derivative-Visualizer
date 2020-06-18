import React from "react";
import { NextPage } from "next";
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

const Graph: NextPage<GraphProps> = ({ id, title, x, lines, ...dims }) => {
  const options = {
    chart: { group: "charts", id },
    title: { text: title },
    xaxis: { x },
  };
  const series = lines.map((line) => ({ name: line.name, data: line.yPoints }));
  return (
    <Chart
      options={options}
      series={series}
      type="area"
      width={350}
      height={350}
    />
  );
};

export default Graph;
