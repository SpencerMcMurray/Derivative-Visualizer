import React, { useState } from "react";
import { NextPage } from "next";
import { Approximation } from "../public/static/helpers/interfaces";
import GraphBox from "../components/GraphBox";
import Title from "../components/Title";
import InputBox from "../components/InputBox";
import SelectBox from "../components/SelectBox";

const Index: NextPage<{}> = () => {
  const [show, setShow] = useState("");
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
      <div className="container">
        <InputBox />
        <SelectBox
          show={show}
          setShow={setShow}
          names={lines.map((l) => l.name)}
        />
      </div>
      <GraphBox x={x} lines={lines} show={show} />
    </React.Fragment>
  );
};

export default Index;
