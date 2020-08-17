import React, { FunctionComponent } from "react";
import Graph from "./Graph";
import { Approximation } from "../public/static/helpers/interfaces";

interface GraphBoxPorps {
  x: number[];
  y: number[];
  approxs: Approximation[];
  show: string;
  showLabel: boolean;
}

const GraphBox: FunctionComponent<GraphBoxPorps> = ({
  x,
  y,
  approxs,
  show,
  showLabel,
}) => {
  let approxLines = approxs.map((a) => ({ name: a.name, data: a.y }));
  let errLines = approxs.map((a) => ({ name: a.name, data: a.error }));

  if (show.length > 0) {
    approxLines = approxLines.filter((a) => a.name === show);
    errLines = errLines.filter((a) => a.name === show);
  }
  approxLines.push({ name: "True Derivative", data: y });

  return (
    <div className="container-fluid mx-auto row justify-content-center flex-wrap">
      <Graph
        id="approx"
        title="Approximations"
        x={x}
        lines={approxLines}
        showLabel={showLabel}
      />
      <Graph
        id="errs"
        title="Relative Errors"
        x={x}
        lines={errLines}
        showLabel={showLabel}
      />
    </div>
  );
};

export default GraphBox;
