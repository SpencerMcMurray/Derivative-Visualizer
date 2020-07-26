import { Approximation } from "./interfaces";
import Axios from "axios";

export interface InputData {
  expr: string;
  n: string;
  start: string;
  end: string;
  points: string;
}

export interface OutputData {
  x: number[];
  y: number[];
  approxs: Approximation[];
}

export const fetchData = async (
  input: InputData,
  setErrs: (errs: string[]) => void
) => {
  return Axios.get(
    `${process.env.NEXT_PUBLIC_API || "http://localhost:5000"}/derivatives`,
    {
      params: input,
    }
  ).catch(() =>
    setErrs(["Backend could not process request, please ensure validity"])
  );
};
