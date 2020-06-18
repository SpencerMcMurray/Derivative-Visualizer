import React from "react";
import { NextPage } from "next";
import { Line } from "../public/static/helpers/interfaces";
import Graph from "../components/Graph";
import GraphBox from "../components/GraphBox";

const Index: NextPage<{}> = () => {
  // TODO: These 3 consts will come from a backend fetch
  const x: number[] = [1, 2, 3];
  const approxs: Line[] = [
    { name: "Approx A", yPoints: [4, 3, 2] },
    { name: "Approx B", yPoints: [5, 4, 7] },
  ];
  const errs: Line[] = [
    { name: "Relative Error A", yPoints: [14, 2, 0] },
    { name: "Relative Error B", yPoints: [1, 1, 4] },
  ];
  return (
    <GraphBox>
      <Graph id="approx" title="Approximations" x={x} lines={approxs} />
      <Graph id="rel-err" title="Relative Errors" x={x} lines={errs} />
    </GraphBox>
  );
};

export default Index;
