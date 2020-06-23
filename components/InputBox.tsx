import React, { FunctionComponent, useState } from "react";
import { Form, Col, Button } from "react-bootstrap";

const InputBox: FunctionComponent<{}> = () => {
  const [f, setF] = useState("x^2");
  const [n, setN] = useState("1");
  const [start, setStart] = useState("0");
  const [stop, setStop] = useState("5");
  const [pts, setPts] = useState("4");

  const handleSubmit = () => {
    const data = { f, n, start, stop, pts };
    console.log(data);
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
          />
        </Form.Group>

        <Form.Group as={Col} controlId="stop">
          <Form.Label>Stop</Form.Label>
          <Form.Control
            onChange={(evt) => setStop(evt.target.value)}
            type="text"
            placeholder="Enter stop..."
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
