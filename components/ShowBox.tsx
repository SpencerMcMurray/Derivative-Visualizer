import React, { FunctionComponent } from "react";
import { Form } from "react-bootstrap";

interface ShowBoxProps {
  label: string;
  setter: (val: boolean) => any;
  value: boolean;
}

const ShowBox: FunctionComponent<ShowBoxProps> = ({ label, ...props }) => {
  return (
    <Form.Check
      type="checkbox"
      label={label}
      value={props.value ? "1" : "0"}
      onChange={(evt: any) => props.setter(evt.target.checked)}
    />
  );
};

export default ShowBox;
