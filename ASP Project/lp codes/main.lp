dims(4,4).
finalpos(3,20,2).

%program
position(6,0,0,1).
step(1..35).
action(change_orient; move_left; move_right; sit).

position(Xi+1, Yi+1, T, O) :- occurs(move_right,T), position(Xi, Yi, T-1, O), step(T), Xi+1 <= 13, Yi+1 <= 20.

position(Xi-1, Yi+1, T, O) :- occurs(move_left, T), position(Xi, Yi, T-1, O), step(T), Xi-1 >= 3, Yi+1 <= 20.

position(Xi, Yi+1, T, O+1 - 4*((O-1)/4)) :- occurs(change_o, T), step(T), position(Xi, Yi, T-1, O), Yi+1 <= 20.

position(Xi, Yi+1, T, O) :- occurs(sit, T), step(T), position(Xi, Yi, T-1, O), Yi+1 <= 20.

goal(T) :- finalpos(Xf, Yf, Of), position(Xi, Yi, T, Oi), Xi == Xf, Yi == Yf, Of == Oi.

1{occurs(A,T) : action(A)}1 :- not goal(T), step(T).

%Strategy Constraints
%:- occurs(move_left,T), action(move_left), step(T), position(Xi, Yi, T, Oi), finalpos(Xf, Yf,Of),
%   |Xf - (Xi-1)| < |Xf - Xi|.
   
%:- occurs(move_right,T), action(move_right), step(T), position(Xi, Yi, T, Oi), finalpos(Xf, Yf,Of),
%   |Xf - (Xi+1)| < |Xf - Xi|.

%:- occurs(change_o, T), action(change_o), step(T), position(Xi, Yi, T-1, Oi), finalpos(Xf, Yf,Of),
%   Oi == Of.