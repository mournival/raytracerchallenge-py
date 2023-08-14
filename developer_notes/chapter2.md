The canvas class. This is the big compromise. I made the canvas mutable.
My rationale  is that the application is
1. Read the scene model
2. Render the scene 
3. Persist the canvas

In short, step 2 is 'constructing' the canvas because each pixle is written
exactly once. Constructors nearly always violate the immutability of state.
Internally.

So, I am pretending that Canvas(R,C) is a partial constructor, and the redering
is a dependency injected constructor strategy. Don't begrudge my illusions (or
would the be delusions?).