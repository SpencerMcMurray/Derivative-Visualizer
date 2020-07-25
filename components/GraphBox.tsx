import React, { FunctionComponent } from "react";
import Graph from "./Graph";
import { Approximation } from "../public/static/helpers/interfaces";

interface GraphBoxPorps {
  x: number[];
  y: number[];
  approxs: Approximation[];
  show: string;
}

const GraphBox: FunctionComponent<GraphBoxPorps> = ({ x, approxs, show }) => {
  let approxLines = approxs.map((a) => ({ name: a.name, data: a.y }));
  let errLines = approxs.map((a) => ({ name: a.name, data: a.error }));

  if (show.length > 0) {
    approxLines = approxLines.filter((a) => a.name === show);
    errLines = errLines.filter((a) => a.name === show);
  }

  return (
    <div className="container-fluid mx-auto row justify-content-center flex-wrap">
      <Graph id="approx" title="Approximations" x={x} lines={approxLines} />
      <Graph id="errs" title="Relative Errors" x={x} lines={errLines} />
    </div>
  );
};

export default GraphBox;
