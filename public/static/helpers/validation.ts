const ORDER_CAP = 10;
const PTS_CAP = 100;

interface validationInput {
  fcn: string;
  order: string;
  xStart: string;
  xStop: string;
  xPts: string;
}

export const validateInput = (input: validationInput): boolean => {
  const { order, xStart, xStop, xPts } = input;
  const orderNum = parseFloat(order);
  if (
    isNaN(orderNum) ||
    orderNum % 1 !== 0 ||
    (orderNum <= 0 && orderNum > ORDER_CAP)
  ) {
    return false;
  }
  const xPtsNum = parseFloat(xPts);
  if (
    isNaN(orderNum) ||
    xPtsNum % 1 !== 0 ||
    (xPtsNum <= 0 && xPtsNum > PTS_CAP)
  ) {
    return false;
  }
  const xStartNum = parseFloat(xStart);
  const xStopNum = parseFloat(xStop);
  if (isNaN(xStartNum) || isNaN(xStopNum)) {
    return false;
  }
  return true;
};
