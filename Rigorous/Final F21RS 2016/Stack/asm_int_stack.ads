
package ASM_Int_Stack
  --# own State;
   --# initializes State;
is
   function Full return Boolean;
   --# global in State;

   procedure Push(X: in Integer);
   --# global in out State;
   --# derives State from X, State;

   function Empty return Boolean;
   --# global in State;

   procedure Pop(AValue: out Integer);
   --# global in out State;
   --# derives AValue, State from State;

end ASM_Int_Stack;

