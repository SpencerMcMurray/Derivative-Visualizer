import React, { FunctionComponent } from "react";

const GraphBox: FunctionComponent<{}> = ({ children }) => {
  return (
    <div className="d-flex justify-content-center flex-wrap">
      {React.Children.map(children, (child) => (
        <div className="col-md-4">{child}</div>
      ))}
    </div>
  );
};

export default GraphBox;
