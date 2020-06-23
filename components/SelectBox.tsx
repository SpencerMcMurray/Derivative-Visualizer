import React, { FunctionComponent } from "react";
import { Form } from "react-bootstrap";

interface SelectBoxProps {
  show: string;
  setShow: (s: string) => any;
  names: string[];
}

const SelectBox: FunctionComponent<SelectBoxProps> = (props) => {
  return (
    <Form.Group controlId="select-graphs">
      <Form.Label>Select which graph to show</Form.Label>
      <Form.Control
        as="select"
        value={props.show}
        onChange={(evt) => props.setShow(evt.target.value)}
      >
        <option value="">All</option>
        {props.names.map((name, idx) => (
          <option key={idx}>{name}</option>
        ))}
      </Form.Control>
    </Form.Group>
  );
};

export default SelectBox;
