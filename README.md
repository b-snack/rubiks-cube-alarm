# Rubik's Cube Alarm Clock

Not exactly sure how this would technically work, but:

- I'm thinking that rn, if we somehow get it to sense three sides that are solved, it should theoretically be fully solved, since its technically harder for the typical solver to solve the entire cube rather than just three sides
- Open CV should be able to detect the outline of the cube and each side, but I'm probably going to need to find an efficient way to quickly scan the whole thing and filter out noise & unnecessary details

Not working on the alarm part or raspberry pi yet - have to get the openCV working first, and then camera positioning and whatnot should be pretty easy after.
