import React, { FunctionComponent } from "react";
import Graph from "./Graph";
import { Approximation } from "../public/static/helpers/interfaces";

interface GraphBoxPorps {
  x: number[];
  lines: Approximation[];
}

const GraphBox: FunctionComponent<GraphBoxPorps> = ({ x, lines }) => {
  return (
    <div className="d-flex justify-content-center flex-wrap">
      <div className="col-xl-5">
        <Graph
          id="approx"
          title="Approximations"
          x={x}
          lines={lines.map((line) => ({ name: line.name, data: line.y }))}
        />
      </div>
      <div className="col-xl-5">
        <Graph
          id="errs"
          title="Relative Error"
          x={x}
          lines={lines.map((line) => ({ name: line.name, data: line.error }))}
        />
      </div>
    </div>
  );
};

export default GraphBox;
