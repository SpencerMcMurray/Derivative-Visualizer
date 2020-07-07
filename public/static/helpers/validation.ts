const ORDER_CAP = 10;
const PTS_CAP = 100;

interface validationInput {
  fcn: string;
  order: string;
  xStart: string;
  xStop: string;
  xPts: string;
}

export const validateInput = (input: validationInput): string[] => {
  const errs: string[] = [];

  const { fcn, order, xStart, xStop, xPts } = input;
  if (fcn.length === 0) errs.push(`Function cannot be empty`);
  const orderNum = parseFloat(order);
  if (
    isNaN(orderNum) ||
    orderNum % 1 !== 0 ||
    (orderNum <= 0 && orderNum > ORDER_CAP)
  )
    errs.push(`Given order of ${order} is either too large or invalid`);
  const xPtsNum = parseFloat(xPts);
  if (
    isNaN(xPtsNum) ||
    xPtsNum % 1 !== 0 ||
    (xPtsNum <= 0 && xPtsNum > PTS_CAP)
  )
    errs.push(`Given point count of ${xPts} is either too large or invalid`);

  const xStartNum = parseFloat(xStart);
  if (isNaN(xStartNum)) errs.push(`Given start of ${xStart} is invalid`);

  const xStopNum = parseFloat(xStop);
  if (isNaN(xStopNum)) errs.push(`Given stop of ${xStop} is invalid`);

  return errs;
};
