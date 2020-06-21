import React, { FunctionComponent } from "react";
import Graph from "./Graph";
import { Approximation } from "../public/static/helpers/interfaces";

interface GraphBoxPorps {
  x: number[];
  lines: Approximation[];
  show: string;
}

const GraphBox: FunctionComponent<GraphBoxPorps> = ({ x, lines, show }) => {
  let approxLines = lines.map((l) => ({ name: l.name, data: l.y }));
  let errLines = lines.map((l) => ({ name: l.name, data: l.error }));

  if (show.length > 0) {
    approxLines = approxLines.filter((l) => l.name === show);
    errLines = errLines.filter((l) => l.name === show);
  }

  return (
    <div className="d-flex justify-content-center flex-wrap">
      <div className="col-xl-5 px-auto">
        <Graph id="approx" title="Approximations" x={x} lines={approxLines} />
      </div>
      <div className="col-xl-5 px-auto">
        <Graph id="errs" title="Relative Error" x={x} lines={errLines} />
      </div>
    </div>
  );
};

export default GraphBox;
