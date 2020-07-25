import React, { FunctionComponent, useState } from "react";
import { Form, Col, Button } from "react-bootstrap";
import { validateInput } from "../public/static/helpers/validation";
import { fetchData, OutputData } from "../public/static/helpers/request";
import { Approximation } from "../public/static/helpers/interfaces";

interface InputBoxProps {
  setErrs: (errs: string[]) => void;
  setX: (x: number[]) => void;
  setY: (y: number[]) => void;
  setApproxs: (a: Approximation[]) => void;
}

const InputBox: FunctionComponent<InputBoxProps> = ({ setErrs, ...props }) => {
  const [f, setF] = useState("x**2");
  const [n, setN] = useState("1");
  const [start, setStart] = useState("1");
  const [stop, setStop] = useState("5");
  const [pts, setPts] = useState("4");

  const handleSubmit = async () => {
    const data = {
      expr: f,
      n: n,
      start: start,
      end: stop,
      points: pts,
    };
    const errs = validateInput(data);
    if (errs.length > 0) {
      setErrs(errs);
      return;
    }
    // Send to backend
    const output = (await fetchData(data, setErrs).then(
      (res) => (res as any).data
    )) as OutputData;
    props.setX(output.x);
    props.setY(output.y);
    props.setApproxs(output.approxs);
  };

  return (
    <div className="container mt-4 mb-2 p-2 border rounded">
      <Form.Row>
        <Form.Group as={Col} controlId="fcn">
          <Form.Label>Function</Form.Label>
          <Form.Control
            onChange={(evt) => setF(evt.target.value)}
            type="text"
            placeholder="Enter f(x)..."
            value={f}
          />
          <Form.Text className="text-muted">
            This should be n-differentiable
          </Form.Text>
        </Form.Group>

        <Form.Group as={Col} controlId="n">
          <Form.Label>Derivative Order</Form.Label>
          <Form.Control
            onChange={(evt) => setN(evt.target.value)}
            type="text"
            placeholder="Enter n..."
            value={n}
          />
        </Form.Group>
      </Form.Row>

      <h5>X Range</h5>
      <Form.Row>
        <Form.Group as={Col} controlId="start">
          <Form.Label>Start</Form.Label>
          <Form.Control
            onChange={(evt) => setStart(evt.target.value)}
            type="text"
            placeholder="Enter start..."
            value={start}
          />
        </Form.Group>

        <Form.Group as={Col} controlId="stop">
          <Form.Label>Stop</Form.Label>
          <Form.Control
            onChange={(evt) => setStop(evt.target.value)}
            type="text"
            placeholder="Enter stop..."
            value={stop}
          />
          <Form.Text className="text-muted">
            This value is exclusive in the range
          </Form.Text>
        </Form.Group>

        <Form.Group as={Col} controlId="pts">
          <Form.Label>Points</Form.Label>
          <Form.Control
            onChange={(evt) => setPts(evt.target.value)}
            type="text"
            placeholder="Enter point count..."
            value={pts}
          />
        </Form.Group>
      </Form.Row>
      <Button onClick={handleSubmit} variant="success">
        Submit
      </Button>
    </div>
  );
};

export default InputBox;
