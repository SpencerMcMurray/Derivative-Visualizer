import React, { useState } from "react";
import { NextPage } from "next";
import { Approximation } from "../public/static/helpers/interfaces";
import GraphBox from "../components/GraphBox";
import Title from "../components/Title";
import InputBox from "../components/InputBox";
import SelectBox from "../components/SelectBox";
import Errors from "../components/Errors";

const Index: NextPage<{}> = () => {
  const [show, setShow] = useState("");
  const [errs, setErrs] = useState([]);
  const [x, setX] = useState<number[]>([]);
  const [y, setY] = useState<number[]>([]);
  const [approxs, setApproxs] = useState<Approximation[]>([]);
  return (
    <React.Fragment>
      <Title />
      <div className="d-flex justify-content-center">
        <Errors errs={errs} />
      </div>
      <div className="container">
        <InputBox
          setX={setX}
          setY={setY}
          setApproxs={setApproxs}
          setErrs={setErrs}
        />
        <SelectBox
          show={show}
          setShow={setShow}
          names={approxs.map((a) => a.name)}
        />
      </div>
      <GraphBox x={x} y={y} approxs={approxs} show={show} />
    </React.Fragment>
  );
};

export default Index;
