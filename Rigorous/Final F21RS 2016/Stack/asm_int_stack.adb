
package body ASM_Int_Stack
  --# own State is Data, Pointer;
is
   Stack_Size: constant:=4;
   type Pointer_Range is range 0..Stack_Size;
   subtype Index_Range is Pointer_Range range 1..Stack_Size;
   type Vector is array(Index_Range) of Integer;
   Data: Vector;
   Pointer: Pointer_Range;

   function Full return Boolean
      --# global in Pointer;
   is
   begin
      return Pointer = Stack_Size;
   end Full;

   procedure Push(X: in Integer)
     --# global in out Data, Pointer;
     --# derives Data from X, Data, Pointer &
     --#         Pointer from Pointer;
   is
   begin
      Pointer:= Pointer + 1;
      Data(Pointer):= X;
   end Push;

   function Empty return Boolean
   --# global in Pointer;
   is
   begin
	return Pointer = 0;
   end Empty;

   procedure Pop(AValue: out Integer)
	--# global in Data;
	--# 	   in out Pointer;
	--# derives Pointer from Pointer &
	--#	    AValue from Data, Pointer;
   is
   begin
	AValue := Data(Pointer);
	Pointer := Pointer - 1;
   end Pop;

begin
   Pointer:= 0;
   Data:= Vector'(Index_Range => 0);
end ASM_Int_Stack;



