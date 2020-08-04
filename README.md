# Derivative Visualizer

This project is a visualizer for higher order derivative approximations.

We will be using Python to create a backend which can calculate and send
the approximation and the true derivative of a given function to the frontend,
where we visualize our results.

## Examples

With low derivative order, the accurracy is quite high and produces great results:
![Good Ex](https://i.imgur.com/yZPBB9O.png)

However with increased order, we can see more and more inaccuracies:
![Badish Ex](https://i.imgur.com/nXx2H2B.png)

## Getting started

To install the dependencies you need to run

```
pip install -r requirements.txt
npm i
```

The use the following commands on individual command line instances to run the client and server

```
npm run client
npm run server
```

Finally go to localhost:3000 to try it out
