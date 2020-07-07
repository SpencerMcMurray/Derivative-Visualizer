import React, { FunctionComponent, useState, useEffect } from "react";
import { Alert } from "react-bootstrap";

const Errors: FunctionComponent<{ errs: string[] }> = ({ errs }) => {
  const [show, setShow] = useState(false);
  useEffect(() => setShow(errs.length > 0), [errs]);

  return (
    <Alert
      className="mt-4"
      show={show}
      variant="danger"
      onClose={() => setShow(false)}
      dismissible
      style={{
        zIndex: 9999,
        position: "absolute",
        top: 0,
        width: "300px",
        overflowY: "auto",
        maxHeight: "50vh",
      }}
    >
      <Alert.Heading>Uh-oh, we found some errors!</Alert.Heading>
      <hr />
      <ul className="overflow-auto">
        {errs.map((err, idx) => (
          <li key={idx}>{err}</li>
        ))}
      </ul>
    </Alert>
  );
};

export default Errors;
