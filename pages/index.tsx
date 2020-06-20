import React from "react";
import { NextPage } from "next";
import { Approximation } from "../public/static/helpers/interfaces";
import Graph from "../components/Graph";
import GraphBox from "../components/GraphBox";
import Title from "../components/Title";
import InputBox from "../components/InputBox";

const Index: NextPage<{}> = () => {
  // TODO: These consts will come from a backend fetch
  const x: number[] = [1, 2, 3];
  const lines: Approximation[] = [
    {
      name: "Approx A",
      y: [4, 3, 2],
      error: [14, 2, 0],
    },
    {
      name: "Approx B",
      y: [3, 4, 3],
      error: [0, 15, 4],
    },
  ];
  return (
    <React.Fragment>
      <Title />
      <InputBox />
      <GraphBox x={x} lines={lines} />
    </React.Fragment>
  );
};

export default Index;
