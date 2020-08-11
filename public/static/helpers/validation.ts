import { InputData } from "./request";

const ORDER_CAP = 6;
const PTS_CAP = 100;

export const validateInput = (input: InputData): string[] => {
  const errs: string[] = [];

  const { expr, n, start, end, points } = input;
  if (expr.length === 0) errs.push(`Function cannot be empty`);
  const orderNum = parseFloat(n);
  if (
    isNaN(orderNum) ||
    orderNum % 1 !== 0 ||
    orderNum <= 0 ||
    orderNum > ORDER_CAP
  )
    errs.push(`Given order of ${n} is either too large or invalid`);
  const xPtsNum = parseFloat(points);
  if (isNaN(xPtsNum) || xPtsNum % 1 !== 0 || xPtsNum < 2 || xPtsNum > PTS_CAP)
    errs.push(`Given point count of ${points} is either too large or invalid`);

  const xStartNum = parseFloat(start);
  if (isNaN(xStartNum)) errs.push(`Given start of ${start} is invalid`);

  const xStopNum = parseFloat(end);
  if (isNaN(xStopNum)) errs.push(`Given stop of ${end} is invalid`);

  return errs;
};
